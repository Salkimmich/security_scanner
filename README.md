# GitHub Security Scanner 🔐🚀

## 📌 Project Overview

This repository contains two implementations of a GitHub organization 
security scanning tool designed to automatically audit and verify security 
settings across repositories.

### 🌟 Key Objectives

- **Automate security configuration checks** across GitHub organizations
- Provide **multiple language implementations** for flexibility
- **Enhance security posture** for open-source projects
- Support comprehensive security scanning

## 🚀 Implementations

### 1. Python Implementation 🐍

Located in the `/python` directory:
- Traditional implementation
- First version of the security scanner
- Suitable for quick deployments and scripting

**[👉 Navigate to Python README](https://github.com/Salkimmich/security_scanner/tree/main/python_scanner)**

### 2. Rust Implementation 🦀

Located in the `/rust` directory:
- Performance-optimized version
- Async handling with `tokio`
- Enhanced efficiency for large-scale scans

**[👉 Navigate to Rust README]([/rust/README.md](https://github.com/Salkimmich/security_scanner/tree/main/rust_scanner))**

## 🔍 Features (Common to Both Implementations)

- Fetch all repositories in a GitHub organization
- Check security scanning settings:
  * Secret scanning
  * Dependabot
  * Code scanning
- Support for both authenticated and unauthenticated scans
- Color-coded CLI output
- JSON result generation

## 🛠️ Quick Start

### Choose Your Implementation

1. **Python Users**: 
   ```sh
   cd python
   # Follow Python README instructions
   ```

2. **Rust Users**:
   ```sh
   cd rust
   # Follow Rust README instructions
   ```

## 🔑 Authentication

Both implementations support:
- Classic Personal Access Tokens (PATs)
- Fine-Grained Tokens
- Scanning public repositories without authentication

**⚠️ Recommended Permissions:**
- `read:org`
- `security_events`
- `repo` (for private repository scans)

## 💡 Contributing

We welcome contributions to both implementations!

- Improve existing code
- Add new features
- Optimize performance
- Expand scanning capabilities

**How to Contribute:**
1. Choose Python or Rust implementation
2. Read the specific README
3. Submit pull requests
4. Report issues

## 📢 Future Roadmap

- Support scanning multiple organizations
- Implement GitHub App-based authentication
- Add more comprehensive security checks
- Expand to other open-source foundations

## 🌐 Supported Foundations (Potential Future Expansion)

- CNCF
- Eclipse Foundation
- Apache Software Foundation
- Linux Foundation
- OWASP

## 📄 License


This project is released under the Eclipse Public License - v 2.0.
For more details about the terms and conditions of use, please review the 
full license text at the provided link.
Happy Secure Scanning! 🔐🚀

**Happy Secure Scanning!** 🔐🚀
