import os
import subprocess

def push_updates():
    # Get the current directory
    repo_path = os.getcwd()

    # Change directory to the repository
    os.chdir(repo_path)

    # Stage all changes
    subprocess.run(["git", "add", "."])

    # Prompt user for commit message
    commit_message = input("Enter commit message: ")

    # Commit changes with the provided message
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push changes to the remote repository
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    # Call the function to push updates
    push_updates()
