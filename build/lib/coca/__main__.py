import sys
import subprocess

def clone_github_repo(repo_name):
    if not repo_name:
        print("Usage: coca install <github_repo_name>")
        sys.exit(1)

    # Construct the GitHub URL from the repo name
    github_url = f"https://github.com/{repo_name}.git"
    print(f"Cloning repository from {github_url}...")

    try:
        # Run `git clone` command
        subprocess.run(["git", "clone", github_url], check=True)
        print(f"Successfully cloned {repo_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        sys.exit(1)

def main():
    # Ensure the command is called as 'install'
    if len(sys.argv) < 3 or sys.argv[1] != 'install':
        print("Usage: coca install <github_repo_name>")
        sys.exit(1)

    # Extract the repository name
    repo_name = sys.argv[2]
    clone_github_repo(repo_name)

if __name__ == "__main__":
    main()
