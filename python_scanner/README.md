# GitHub Security Scanner

## 📌 Motivation

This script was built to **automate the security audit of GitHub repositories** by checking if **secret scanning and security features** are enabled across an entire **organization**.

The **goal of this project** is to:

* **Enhance security posture** by ensuring repositories have secret scanning enabled.
* **Provide flexibility** for scanning via both **Classic PATs** and **Fine-Grained Tokens**.
* **Support automation** for security scanning in **open-source organizations**.

## 🚀 Features

- ✔️ Fetches all repositories in a **GitHub organization**
- ✔️ Checks whether **secret scanning, Dependabot, and code scanning** are enabled
- ✔️ Works **with or without authentication**
- ✔️ Supports **color-coded CLI output**
- ✔️ Saves results to **JSON** for further analysis

## 🛠️ Setup & GitHub Token Configuration

To run this script with **full access**, you need a **GitHub Personal Access Token (PAT)** with the following permissions:

### ✅ Option 1: Classic PAT (Recommended for Full Org Scans)

- ✅ `read:org` → To list repositories in an **organization**
- ✅ `security_events` → To check **security settings** like **secret scanning**
- ✅ `repo` (Optional) → If you want to check **private repositories**

### ✅ Option 2: Fine-Grained Token (Recommended for Specific Repos)

Fine-grained tokens **require manual repository selection** and work best if you **only need to scan specific repositories**.

1. **Go to** GitHub Fine-Grained Token Setup.
2. Click **"Generate new fine-grained token"**.
3. **Under "Repository Access"**, select **"Only Select Repositories"**.
4. **Search for "eclipse/"** to filter and select all Eclipse Foundation repositories.
   * ⚠️ **You can only select 50 repositories per token.**
   * If there are **more than 50 repositories**, create **additional tokens**.
   * If repositories **don't appear**, **request admin approval**.
5. **Set the following permissions**:
   * ✅ `Read access to repository metadata`
   * ✅ `Read access to security events`
   * ✅ `Read access to code scanning alerts`
   * ✅ `Read access to Dependabot alerts`
   * ✅ `Read access to secret scanning alerts`
6. Click **"Generate Token"** and **copy it immediately!**
   * **⚠️ You won't be able to see it again after leaving the page.**

## ▶️ How to Run the Script

### Option 1: With Authentication (Recommended)

Run the script with your **GitHub token**:

```sh
python repo_scan.py --org eclipse --token YOUR_GITHUB_TOKEN
```

Or, set your token as an **environment variable** and run:

```sh
export GITHUB_TOKEN=YOUR_GITHUB_TOKEN python repo_scan.py --org eclipse
```

For Rust:

```sh
export GITHUB_TOKEN=YOUR_GITHUB_TOKEN ./target/release/rust_scanner --org eclipse
```

### Option 2: Without Authentication (Limited)

If you don't provide a token, the script will only scan **public repositories**:

```sh
python repo_scan.py --org eclipse
```

⚠️ **Warning**: GitHub's API rate limits **unauthenticated requests**.

## 📝 Understanding the Output

| Repository | Secret Scanning | Dependabot | Code Scanning |
|-----------|-----------------|------------|--------------|
| `repo1`   | ✅ Enabled      | ✅ Enabled | ❌ Not Enabled |
| `repo2`   | ❌ Not Enabled  | ❌ Not Enabled | ❌ Not Enabled |
| `repo3`   | ⚠️ 403 Forbidden | ✅ Enabled | ✅ Enabled |

**Results are also saved to a JSON file**:

```sh
security_scan_results.json
```

## 🚀 Future Improvements

### 🔄 Expand to All Open Source Foundations

Currently, the script is limited to **a single GitHub organization**. A future version could scan multiple organizations at once, covering:

- CNCF
- Eclipse Foundation
- Apache Software Foundation
- Linux Foundation
- OWASP

### 🔒 Add GitHub App-Based Authentication

Using a **GitHub App** instead of a **PAT** would:

* Provide **higher security**
* Eliminate **manual token rotation**
* Allow **scaling across organizations**

## 💡 Contributing

This project is open for contributions! Submit a **pull request** or suggest an improvement in **GitHub Issues**.