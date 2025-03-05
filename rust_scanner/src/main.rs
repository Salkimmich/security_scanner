use reqwest::{Client, StatusCode};
use serde_json::Value;
use std::{env, error::Error};
use tokio;

const GITHUB_API_URL: &str = "https://api.github.com";

/// 🚀 **Main function: Initializes and runs the GitHub scanning script**
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // ✅ Read arguments from CLI
    let args: Vec<String> = env::args().collect();
    let org = args.iter().position(|x| x == "--org").map(|i| args[i + 1].clone()).unwrap_or_else(|| {
        eprintln!("❌ Missing `--org` argument. Usage: --org <organization_name>");
        std::process::exit(1);
    });

    let token = args.iter().position(|x| x == "--token").map(|i| args[i + 1].clone()).unwrap_or_else(|| {
        eprintln!("❌ Missing `--token` argument. Usage: --token <your_github_token>");
        std::process::exit(1);
    });

    // ✅ Initialize HTTP client
    let client = Client::new();

    // ✅ Fetch list of repositories in the organization
    let repos = fetch_repositories(&client, &org, &token).await?;

    if repos.is_empty() {
        eprintln!("⚠️ No repositories found for '{}'.", org);
        return Ok(());
    }

    println!("✅ Found {} repositories.\n", repos.len());

    // ✅ Check security settings for each repository
    for repo in repos {
        let security_status = check_security_features(&client, &org, &repo, &token).await?;
        println!("📂 Repo: {} | Security: {}", repo, security_status);
    }

    Ok(())
}

/// 🔍 **Fetch repositories for a GitHub organization**
async fn fetch_repositories(client: &Client, org: &str, token: &str) -> Result<Vec<String>, Box<dyn Error>> {
    let url = format!("{}/orgs/{}/repos", GITHUB_API_URL, org);

    let response = client.get(&url)
        .header("Authorization", format!("token {}", token))
        .header("User-Agent", "rust_scanner")
        .send()
        .await?;

    match response.status() {
        StatusCode::OK => {
            let repos: Vec<Value> = response.json().await?;
            let repo_names: Vec<String> = repos.iter().filter_map(|r| r["name"].as_str().map(String::from)).collect();
            Ok(repo_names)
        }
        StatusCode::FORBIDDEN => {
            eprintln!("🚨 API Forbidden (403) - Check token permissions for `read:org`.");
            Err("Failed to fetch repositories".into())
        }
        _ => {
            eprintln!("❌ Error fetching repositories: {}", response.status());
            Err("Failed to fetch repositories".into())
        }
    }
}

/// 🔍 **Check security features for a repository**
async fn check_security_features(client: &Client, org: &str, repo: &str, token: &str) -> Result<String, Box<dyn Error>> {
    let url = format!("{}/repos/{}/{}/code-scanning/alerts", GITHUB_API_URL, org, repo);

    let response = client.get(&url)
        .header("Authorization", format!("token {}", token))
        .header("User-Agent", "rust_scanner")
        .send()
        .await?;

    match response.status() {
        StatusCode::OK => Ok("✅ Secure".to_string()),
        StatusCode::FORBIDDEN => {
            eprintln!("🚨 API Forbidden: Ensure `security_events` permission is enabled in token.");
            Ok("⚠️ Forbidden (Check Token)".to_string())
        }
        StatusCode::NOT_FOUND => Ok("❌ No Security Scans".to_string()),
        _ => {
            eprintln!("❌ Error checking security status for '{}': {}", repo, response.status());
            Ok("❌ Error".to_string())
        }
    }
}
