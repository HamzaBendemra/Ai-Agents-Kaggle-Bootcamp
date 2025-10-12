# AI Foundry SDK

AI Foundry SDK integration mini-project.

## Setup

This project uses the shared Poetry environment. From the root directory:

```bash
# Install all dependencies (if not already done)
poetry install

# Activate shared virtual environment
poetry shell
```

## Usage

```bash
# From the root directory with Poetry environment activated
python ai-foundry-sdk/main.py

# Or using poetry run from root
poetry run python ai-foundry-sdk/main.py
```

## Dependencies

This project's dependencies are listed in `requirements.txt`. To add new dependencies:

1. Add to `requirements.txt`:
   ```bash
   echo "new-package>=1.0.0" >> requirements.txt
   ```

2. Install to shared environment from root directory:
   ```bash
   poetry add new-package
   ```