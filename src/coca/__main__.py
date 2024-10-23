import sys
import subprocess
import os
import platform

def open_new_terminal_and_activate_venv(repo_path):
    """
    Opens a new terminal, navigates to the repository folder,
    and activates the virtual environment.
    """
    venv_activate = os.path.join(repo_path, "venv", "bin", "activate")

    # Platform-specific commands to open a new terminal and activate venv
    if platform.system() == "Darwin":  # macOS
        command = f"""osascript -e 'tell application "Terminal" to do script "cd {repo_path} && source {venv_activate} && exec bash"'"""
        subprocess.run(command, shell=True)

    elif platform.system() == "Linux":  # Linux
        command = f"""gnome-terminal -- bash -c "cd {repo_path} && source {venv_activate} && exec bash" """
        subprocess.run(command, shell=True)

    elif platform.system() == "Windows":  # Windows
        activate_script = os.path.join(repo_path, "venv", "Scripts", "activate.bat")
        command = f'start cmd /K "cd {repo_path} && {activate_script}"'
        subprocess.run(command, shell=True)

    else:
        print("Unsupported OS. Please activate the virtual environment manually.")


def clone_github_repo(repo_name):
    if not repo_name:
        print("Usage: coca install <github_repo_name>")
        sys.exit(1)

    # Construct the GitHub URL from the repo name
    github_url = f"https://github.com/{repo_name}.git"
    repo_folder = repo_name.split('/')[-1]  # Extract folder name from repo name

    print(f"Cloning repository from {github_url}...")

    try:
        # Run `git clone` command
        subprocess.run(["git", "clone", github_url], check=True)
        print(f"Successfully cloned {repo_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        sys.exit(1)

    # Change directory into the cloned repository
    os.chdir(repo_folder)
    print(f"Changed directory to {os.getcwd()}")

    # Create a virtual environment
    print("Creating a virtual environment...")
    try:
        subprocess.run(["python3", "-m", "venv", "venv"], check=True)
        print("Virtual environment created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        sys.exit(1)

    # Activate the virtual environment
    activate_venv = os.path.join(os.getcwd(), "venv", "bin", "activate")
    print(f"Activating virtual environment: {activate_venv}")
    try:
        # Ensure the virtual environment is activated for installation
        subprocess.run(f"source {activate_venv} && pip install -r requirements.txt", 
                       shell=True, executable="/bin/bash", check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)
        
    # Open a new terminal and activate the virtual environment
    open_new_terminal_and_activate_venv(os.getcwd())
        
    

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
