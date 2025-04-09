# Python Project Skeleton

A skeleton project for Python applications using Poetry for dependency management.

## How to use
1. Clone this repository and rename it to your project name.
2. Modify this `README.md` to show your project title and add any additional project information after the 'Getting Started' level 2 header.
3. Modify the `pyproject.toml` to change the name of the application to the name of your project.
4. Build and create your application!

## Project Structure
```
.
├── end_to_end/          # End-to-end tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_end_to_end.py
├── integration/         # Integration tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_integration.py
├── src/                # Source code
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       └── config.py
├── test/               # Unit tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_app.py
├── docker-entrypoint.sh
├── getting_started.md
├── pyproject.toml
└── README.md
```

### File Purposes
* `README.md` - Project overview, documentation, instructions, and usage examples
* `getting_started.md` - Detailed setup instructions for development
* `pyproject.toml` - Project metadata, dependencies, and build configuration using Poetry
* `docker-entrypoint.sh` - Simple docker entrypoint for use with docker-compose
* `**/__init__.py` - Marks directories as Python packages

### Folder Purposes
* `/src` - Contains the application source code
* `/test` - Contains unit tests that don't require external resources
* `/integration` - Contains tests that interact with external resources (e.g., databases, message queues) with some mocking
* `/end_to_end` - Contains tests that validate the entire application without mocking

## Development Setup

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
# For Poetry 2.0.0+, you need to install the shell plugin first:
poetry self add poetry-plugin-shell

# Then you can activate the virtual environment:
poetry shell
```

4. Set up pre-commit hooks:
```bash
pre-commit install
```

## Available Commands

- Run tests:
```bash
poetry run pytest
```

- Run integration tests:
```bash
poetry run pytest integration
```

- Run end-to-end tests:
```bash
poetry run pytest end_to_end
```

- Run linting:
```bash
poetry run ruff check .
```

- Run type checking:
```bash
poetry run mypy src
```

- Format code:
```bash
poetry run ruff format .
```

- Run security checks:
```bash
poetry run bandit -r src
```

## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. The following checks are performed automatically before each commit:

- Code formatting (ruff)
- Type checking (mypy)
- Security checks (bandit)
- YAML validation
- Poetry dependency validation
- And more...

To run pre-commit checks manually:
```bash
pre-commit run --all-files
```

## Code Quality Tools

This project uses several tools to maintain code quality:

- **Ruff**: Fast Python linter and formatter
- **Mypy**: Static type checker
- **Bandit**: Security linter
- **Pytest**: Testing framework
- **Pre-commit**: Git hook manager

Configuration for these tools can be found in `pyproject.toml` and `.pre-commit-config.yaml`.

## Getting Started
Set up your environment and gather dependencies by following the directions laid out in [Getting Started](getting_started.md).

## Project Specific Information
<!-- Add your project specific information here -->
