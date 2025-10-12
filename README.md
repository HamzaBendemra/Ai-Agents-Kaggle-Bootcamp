# Notebooks

Python Notebooks - AdHoc Mini-Projects

This repository contains multiple independent Python mini-projects managed under a single Poetry environment.

## Structure

```
Notebooks/
├── project-1/
│   ├── requirements.txt
│   └── src/
├── project-2/
│   ├── requirements.txt
│   └── src/
├── pyproject.toml        # Single Poetry config for all projects
├── poetry.lock           # Single lock file
└── README.md
```

## Prerequisites

- Python 3.11.6 or higher
- [Poetry](https://python-poetry.org/) - for dependency management

### Installing Poetry

```bash
# Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -

# Alternative: using pip
pip install poetry
```

## Initial Setup

1. Clone the repository and install all dependencies:
   ```bash
   git clone <repository-url>
   cd Notebooks
   poetry install
   ```

2. Activate the shared virtual environment:
   ```bash
   poetry shell
   ```

## Creating a New Mini-Project

1. Create a new folder for your project:
   ```bash
   mkdir my-new-project
   cd my-new-project
   ```

2. Create a `requirements.txt` file listing your project's dependencies:
   ```bash
   echo "requests>=2.25.0" > requirements.txt
   echo "pandas>=1.3.0" >> requirements.txt
   ```

3. Install your project's dependencies to the shared environment:
   ```bash
   poetry add $(cat requirements.txt | tr '\n' ' ')
   ```

## Working with Projects

### Using the Shared Virtual Environment

```bash
# Activate the shared environment (from root directory)
poetry shell

# Run any project
python project-name/src/main.py
```

### Adding Dependencies for a Project

1. Add the dependency to your project's `requirements.txt`:
   ```bash
   echo "numpy>=1.21.0" >> my-project/requirements.txt
   ```

2. Install it to the shared environment:
   ```bash
   poetry add numpy
   ```

### Managing Dependencies

```bash
# Install all dependencies from root
poetry install

# Add a new dependency to shared environment
poetry add <package-name>

# Update all dependencies
poetry update
```

## Project Guidelines

- Each mini-project should have its own `requirements.txt` file
- All projects share the same Poetry virtual environment
- Include a README.md in each project folder explaining what it does
- Dependencies are managed at the repository level through Poetry
- Project-specific requirements are documented in individual `requirements.txt` files

## License

MIT License - See LICENSE file for details
