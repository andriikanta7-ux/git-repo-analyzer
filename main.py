import sys
from github_skill import get_repo_files


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <owner> <repository>")
        return

    owner = sys.argv[1]
    repo = sys.argv[2]

    files = get_repo_files(owner, repo)

    print("\nRepository files:\n")

    for file in files:
        print(file)


if __name__ == "__main__":
    main()

