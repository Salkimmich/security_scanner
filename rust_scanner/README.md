# GitHub Security Scanner (Rust Implementation)

## 🚀 Overview

This Rust-based security scanner fetches all repositories within a GitHub 
organization and checks for **security analysis settings** (e.g., secret 
scanning, dependency scanning, and code scanning).

We migrated this tool from Python to **Rust** for **performance, 
efficiency, and reliability** in handling large-scale repository scans.

## 🔍 Features

- ✔️ Fetches all repositories from a GitHub organization
- ✔️ Checks **security scanning settings** (secret scanning, Dependabot, 
code scanning)
- ✔️ **Optimized for performance** using Rust and async handling with 
`tokio`
- ✔️ **CLI-based** for easy execution
- ✔️ Outputs **color-coded** results for better visibility

## 📥 Installation & Setup

### 1️⃣ Install Rust

Ensure you have **Rust** installed. If not, install it via Rustup:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

Verify installation:

```sh
rustc --version
cargo --version
```

🔹 Required Token Scopes:

read:org → List repositories in an organization
repo → Access repository details and security settings
admin:org → Read organization-level security settings
security_events → Read and write security events
admin:repo_hook → Manage repository webhooks (if needed for advanced scanning)

🔑 Steps to generate a GitHub token:

Go to GitHub Developer Settings
Click "Generate new token (classic)"
Select these scopes:

✅ read:org  
✅ repo  
✅ admin:org  
✅ security_events  
✅ admin:repo_hook (optional)  


Copy the generated token (you won't see it again!)

💡 Note:

These permissions ensure comprehensive access to security scanning details
For public repositories, some scopes might have reduced requirements
Always follow the principle of least privilege
💡 **Note**: If you're checking **only public repos**, `read:org` is 
enough.

### 3️⃣ Clone & Build the Project

Clone this repository and navigate into the project folder:

```sh
git clone https://github.com/YOUR_USERNAME/rust_scanner.git
cd rust_scanner
```

Build the Rust binary:

```sh
cargo build --release
```

### 4️⃣ Run the Scanner

To run the scanner, use:

```sh
./target/release/rust_scanner --org eclipse --token YOUR_GITHUB_TOKEN
```

Or, set your token as an **environment variable** (recommended):

```sh
export GITHUB_TOKEN=YOUR_GITHUB_TOKEN
./target/release/rust_scanner --org eclipse
```

## 🐞 Debugging & Troubleshooting

### ❌ Error: `403 Forbidden`

* Your GitHub token **might be missing permissions**
* Ensure `read:org` is enabled
* If scanning **private repos**, ensure `repo` is enabled

### ❌ Error: `Error fetching repositories`

* Check if the **organization name** is correct
* Your token **may have expired**—generate a new one
* Try running:

```sh
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/orgs/eclipse/repos
```

If this **fails**, the issue is with your token.

##  Future Improvements

### 🔄 Expand to Multiple Foundations

Currently, the scanner only checks **one** GitHub organization. A future 
update could scan:

* CNCF
* Eclipse Foundation
* Apache Software Foundation
* Linux Foundation
* OWASP

### 🦀 Rewrite with More Rust Optimizations

* Improve **error handling** using `thiserror`
* Add **parallel processing** using `tokio::spawn`
* Cache API results to **avoid rate limits**

## 📢 Contributing

This project is **open for contributions!** Submit a pull request or 
report issues via GitHub.

**Happy Scanning!** 🔐🚀
