This is a project for updating the punishment database for chexie.net.

---
## Requirements
- [`uv`](https://github.com/astral-sh/uv)

## Usage
1. Clone the repository
2. Fetch the file `params.toml` from the former owner of the punishment database (You can always contact the author: thywquake@foxmail.com)
3. Paste the file to the repository directory
4. Run the following command in the repository directory:
```bash
uv venv # create a virtual environment with .python-version
uv sync # install dependencies
uv run main.py # run the script
```