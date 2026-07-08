import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")


def get_repo_files(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error:", response.json())
        return []

    data = response.json()

    files = []

    for item in data["tree"]:
        if item["type"] == "blob":
            files.append(item["path"])

    return files