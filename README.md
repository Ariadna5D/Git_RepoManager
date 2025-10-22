# Git_RepoManager

Git_RepoManager is a small Python application that allows you to easily do `git pull` and `git push` operations on multiple local repositories from a single menu.

## Features

- Pull updates from all or selected repositories at once.
- Push changes (with commit message) to selected repositories.
- Simple menu interface in the console.
- Easy configuration using a JSON file.

## Usage

Run the main script: `/src/Git_Manager.py` or `/build/Git_Manager.exe`

## Configuration

Edit the `repos.json` file to add your local repositories.  
Example:

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


