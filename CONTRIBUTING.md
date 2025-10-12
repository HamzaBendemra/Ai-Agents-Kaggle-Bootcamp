# Contributing Guide

This guide helps you create new mini-projects in this repository.

## Quick Start: Creating a New Project

### Option 1: Using the Template (Recommended)

```bash
# Copy the template
cp -r .templates/mini-project-template/ your-project-name/

# Navigate to your project
cd your-project-name/

# Update pyproject.toml with your project details (name, description, author)
# Edit the README.md to describe your project

# Initialize Poetry (this will create poetry.lock)
poetry install
```

### Option 2: From Scratch

```bash
# Create project directory
mkdir your-project-name
cd your-project-name

# Initialize Poetry interactively
poetry init

# Add dependencies
poetry add <package-name>

# Add development dependencies
poetry add --group dev pytest black flake8

# Install dependencies
poetry install
```

## Project Structure Best Practices

Each mini-project should follow this structure:

```
your-project-name/
├── README.md              # Project documentation
├── pyproject.toml         # Poetry configuration
├── poetry.lock            # Locked dependencies (auto-generated)
├── src/                   # Source code
│   ├── __init__.py
│   └── main.py
└── tests/                 # Tests (optional)
    └── test_main.py
```

## Poetry Commands Reference

### Managing Dependencies

```bash
# Add a package
poetry add requests

# Add a development dependency
poetry add --group dev pytest

# Remove a package
poetry remove requests

# Update all dependencies
poetry update

# Update a specific package
poetry update requests
```

### Working with Virtual Environments

```bash
# Activate virtual environment
poetry shell

# Deactivate (when inside poetry shell)
exit

# Run a command in the virtual environment
poetry run python src/main.py

# Show virtual environment info
poetry env info

# List available virtual environments
poetry env list
```

### Other Useful Commands

```bash
# Show installed packages
poetry show

# Show dependency tree
poetry show --tree

# Check for dependency conflicts
poetry check

# Export requirements.txt (if needed)
poetry export -f requirements.txt --output requirements.txt
```

## Commit Guidelines

- **DO** commit `pyproject.toml` and `poetry.lock`
- **DO** commit your source code
- **DON'T** commit virtual environments (`.venv/`)
- **DON'T** commit `__pycache__/` or `.pyc` files (already in .gitignore)

## Tips

1. **Keep projects independent**: Each project should have its own dependencies and not rely on other projects in the repo
2. **Use meaningful names**: Name your project folders descriptively
3. **Document your project**: Always include a README.md explaining what your project does
4. **Pin Python version**: Use `python = "^3.8"` or specify the version your code requires
5. **Use development dependencies**: Add testing, linting tools as dev dependencies with `--group dev`
