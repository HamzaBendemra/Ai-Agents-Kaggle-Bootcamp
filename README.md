# Notebooks

Python Notebooks - AdHoc Mini-Projects

This repository contains multiple independent Python mini-projects, each in its own folder with separate dependencies managed by Poetry.

## Structure

Each folder in this repository represents a standalone mini-project with:
- Its own `pyproject.toml` (Poetry configuration)
- Its own virtual environment (managed by Poetry)
- Independent dependencies

```
Notebooks/
├── project-1/
│   ├── pyproject.toml
│   ├── poetry.lock
│   └── src/
├── project-2/
│   ├── pyproject.toml
│   ├── poetry.lock
│   └── src/
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) - for dependency management

### Installing Poetry

```bash
# Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -

# Alternative: using pip
pip install poetry
```

## Creating a New Mini-Project

1. Create a new folder for your project:
   ```bash
   mkdir my-new-project
   cd my-new-project
   ```

2. Initialize Poetry:
   ```bash
   poetry init
   ```
   Follow the interactive prompts to set up your project.

3. Add dependencies:
   ```bash
   poetry add <package-name>
   ```

4. Install dependencies and create virtual environment:
   ```bash
   poetry install
   ```

## Working with a Project

### Activating the Virtual Environment

```bash
cd your-project
poetry shell
```

### Running Python Scripts

```bash
# Using poetry run
poetry run python your_script.py

# Or activate the shell first
poetry shell
python your_script.py
```

### Adding Dependencies

```bash
cd your-project
poetry add numpy pandas matplotlib
```

### Adding Development Dependencies

```bash
poetry add --group dev pytest black flake8
```

### Updating Dependencies

```bash
poetry update
```

## Project Guidelines

- Each mini-project should be self-contained
- Include a README.md in each project folder explaining what it does
- Commit `pyproject.toml` and `poetry.lock` to version control
- Virtual environments (`.venv` folders) are ignored by git

## License

MIT License - See LICENSE file for details
