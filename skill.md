# GitHub Repository Analyzer Skill

## Description

This skill connects to GitHub using a Personal Access Token (PAT) and retrieves information about a repository through the GitHub API.

## Features

- Authenticate using GitHub PAT
- Connect to a remote GitHub repository
- Retrieve repository structure
- List all files recursively
- Support retrieving file contents for further analysis

## Inputs

- GitHub repository owner
- Repository name

## Usage

```bash
python3 main.py <owner> <repository>
```

Example:

```bash
python3 main.py andriikanta7-ux git-repo-analyzer
```

## Output

The skill prints a list of files available in the repository.

Example:

```text
README.md
main.py
github_skill.py
```

## Authentication

The skill uses a GitHub Personal Access Token stored in `.env`.

Example:

```text
GITHUB_TOKEN=your_token_here
```