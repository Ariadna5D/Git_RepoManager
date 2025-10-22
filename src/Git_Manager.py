import json
import subprocess

try:
    # Read the JSON file and get the list of repositories
    with open('repos.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        repos = data['repos']

    def show_menu():
        print("--= GIT REPOSITORY MANAGER =--")
        print("1. Pull ALL repositories")
        print("2. Pull selected repositories")
        print("3. Push selected repositories")
        # print("4. Push selected repositories with different commits") (Not implemented yet)
        # print("5. Add repository") (Not implemented yet)
        # print("6. Remove selected repositories") (Not implemented yet)
        # print("7. Change language") (Not implemented yet)
        print("4. Exit")
        print("--------------------------------")

    """
    Function that commits and pushes to the desired repositories

    repo: repo object
    message: commit message
    """
    def git_commit_push(repo, message):
        folder = repo['folder']
        subprocess.run(["git", '-C', folder, "add", "."])
        subprocess.run(["git", '-C', folder, "commit", "-m", message])
        result = subprocess.run(["git", '-C', folder, "push"], capture_output=True, text=True)
        print(result.stdout)
        print(f"----- COMMIT AND PUSH {repo['name']} COMPLETED -----")

    """
    Function that pulls the repository

    repo: repo object
    """
    def git_pull(repo):
        folder = repo['folder']
        result = subprocess.run(["git", '-C', folder, "pull"], capture_output=True, text=True)
        print(result.stdout)
        print(f"----- PULL {repo['name']} COMPLETED -----")

    """
    Function that shows every repo in the repos file, and lets the user select which ones to use

    repos: array of repo objects in file

    return: array of selected repo objects
    """
    def menu_repos(repos):
        for i, repo in enumerate(repos):
            print(f"{i + 1}. {repo['name']} ({repo['folder']})")
        selection = input("Select numbers separated by comma: ")
        indices = [int(x) - 1 for x in selection.split(",")]
        repos_selected = [repos[i] for i in indices]
        return repos_selected

    while True:
        show_menu()
        option = input("Choose an option: ")
        if option == "4":
            break
        if option == "1":
            for repo in repos:
                git_pull(repo)
        elif option == "2":
            selected = menu_repos(repos)
            for repo in selected:
                git_pull(repo)
        elif option == "3":
            selected = menu_repos(repos)
            message = input("Enter the commit message: ")
            for repo in selected:
                git_commit_push(repo, message)

except Exception as e:
    print("An error occurred:", e)

input("Press ENTER to exit...")
