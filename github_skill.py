import os
import requests
import base64
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("GITHUB_TOKEN")


def get_repo_files(owner, repo):

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }


    repo_url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}"
    )


    repo_response = requests.get(
        repo_url,
        headers=headers
    )


    if repo_response.status_code != 200:
        print(repo_response.json())
        return []


    branch = repo_response.json()["default_branch"]


    tree_url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/git/trees/"
        f"{branch}?recursive=1"
    )


    response = requests.get(
        tree_url,
        headers=headers
    )


    data = response.json()


    files = []


    for item in data["tree"]:
        if item["type"] == "blob":
            files.append(item["path"])


    return files



def get_file_content(owner, repo, path):

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/contents/{path}"
    )


    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {TOKEN}"
        }
    )


    if response.status_code != 200:
        return ""


    data = response.json()


    if "content" not in data:
        return ""


    return base64.b64decode(
        data["content"]
    ).decode(
        "utf-8",
        errors="ignore"
    )



def get_repository_context(owner, repo):

    files = get_repo_files(owner, repo)


    context = "FILES:\n"

    for file in files:
        context += file + "\n"


    important = [
        "README.md",
        "main.py",
        "requirements.txt"
    ]


    context += "\nFILE CONTENT:\n"


    for file in important:

        if file in files:

            content = get_file_content(
                owner,
                repo,
                file
            )


            context += (
                f"\n--- {file} ---\n"
                f"{content}\n"
            )


    return context