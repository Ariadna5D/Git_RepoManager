# Git RepoManager

A simple Python application to manage multiple Git repositories from a single menu. Perfect for keeping your projects up to date across multiple devices!

## 🚀 Features

- Pull updates from all or selected repositories at once.
- Push changes (with commit message) to selected repositories.
- Simple menu interface in the console.
- Easy configuration using a JSON file.
- Multiple languages support (in progress)
- Push multiple repositories with different commits (in progress)
- Add/remove repositories using the app (in progress)
- Select and edit branches to push into them (in progress)

## 🛠️ Configuration

Edit the `repos.json` file to add your local repositories. Example:



```
{
"repos": [
    {
      "name": "Repository Name 1",
      "folder": "C:\\file\\repository1"
    },
    {
      "name": "Repository Name 2",
      "folder": "C:\\file\\repository2"
    },
    {
      "name": "Repository Name 3",
      "folder": "C:\\file\\repository3"
    },
    {
      "name": "Repository Name 4",
      "folder": "C:\\file\\repository4"
    },
    {
      "name": "Repository Name 5",
      "folder": "C:\\file\\repository5"
    }
// Add more repositories as needed
]
}
```

- `name`: A descriptive name for your repository.
- `folder`: The absolute path to the local repository folder.


