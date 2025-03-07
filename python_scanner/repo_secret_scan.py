#!/usr/bin/env python3
import requests, argparse, sys, json, os

# Optional: use colorama for Windows terminal color support
try:
    from colorama import Fore, Style, init
    init()  # initialize colorama
except ImportError:
    # Define Fore and Style as empty attributes if colorama isn't installed
    class Dummy:
        def __getattr__(self, name):
            return ''
    Fore = Style = Dummy()

DEFAULT_ORG = "eclipse-bci"

def fetch_repositories(org, token):
    """Fetch all repositories for the given organization using GitHub REST API."""
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?per_page=100&page={page}"
        headers = {"Authorization": f"token {token}"} if token else {}
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            print(f"❌ Error: Organization '{org}' not found or access denied.")
            sys.exit(1)
        if response.status_code == 401:
            print("❌ Error: Invalid API token. Please check your credentials.")
            sys.exit(1)
        if response.status_code != 200:
            error_msg = response.json().get('message', response.text)
            print(f"❌ Error fetching repositories: {response.status_code} - {error_msg}")
            sys.exit(1)
        data = response.json()
        if not data:
            break  # no more repos (end of pagination)
        repos.extend(data)
        if len(data) < 100:  # If fewer than 100 repos were returned, we've reached the last page
            break
        page += 1
    return repos

def check_secret_scanning(org, repo_name, token):
    """Check the secret scanning status of a single repository. Returns status string."""
    url = f"https://api.github.com/repos/{org}/{repo_name}"
    headers = {"Authorization": f"token {token}"} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return "Not Found"
    if response.status_code != 200:
        return f"Error {response.status_code}"
    settings = response.json()
    return settings.get("secret_scanning", {}).get("status", "disabled")

def main():
    parser = argparse.ArgumentParser(description="Check if secret scanning is enabled for all repos in a GitHub organization.")
    parser.add_argument("--org", help="GitHub organization to scan (default: 'eclipse-bci')", default=DEFAULT_ORG)
    parser.add_argument("--token", help="GitHub PAT with read access (optional)", default=None)
    args = parser.parse_args()

    org = args.org
    token = args.token or os.getenv("GITHUB_TOKEN")  # use provided token or fall back to env variable

    if not token:
        print("ℹ️ No token provided. Scanning publicly accessible repos only (unauthenticated).")

    print(f"\n🚀 Fetching repositories from '{org}'...\n")
    repos = fetch_repositories(org, token)
    if not repos:
        print(f"⚠️ No repositories found for organization '{org}'.")
        sys.exit(1)

    print(f"✅ Found {len(repos)} repositories in '{org}'.\n")
    results = []
    max_name_len = max(len(repo.get('name', '')) for repo in repos) if repos else 0
    header_name = "Repository"
    header_status = "Secret Scanning"
    max_name_len = max(max_name_len, len(header_name))

    print(header_name.ljust(max_name_len) + "   " + header_status)
    print("-" * max_name_len + "   " + "-" * len(header_status))

    for repo in repos:
        name = repo.get("name", "(unknown)")
        status = check_secret_scanning(org, name, token)
        results.append({"repository": name, "secret_scanning": status})
        if isinstance(status, str):
            status_display = status
            if status.lower() == "enabled":
                status_display = Fore.GREEN + status + Style.RESET_ALL
            elif status.lower() in ("disabled", "not enabled"):
                status_display = Fore.YELLOW + status + Style.RESET_ALL
            elif status.lower().startswith("error") or status.lower() == "not found":
                status_display = Fore.RED + status + Style.RESET_ALL
        else:
            status_display = str(status)
        symbol = "✅" if status.lower() == "enabled" else ("❌" if status.lower() == "not found" else "⚠️")
        print(f"{name.ljust(max_name_len)}   {symbol} {status_display}")

    output_file = f"secret_scanning_status_{org}.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)
    print(f"\n📄 Results saved to '{output_file}'.")

if __name__ == "__main__":
    main()
