# Python Skeleton

A skeleton project for Python projects using Poetry for dependency management.

## How to use
1. Copy-paste the skeleton directory into the desired location and rename the directory.
2. Modify the `README.md` to show the project title and add any additional project information after the 'Getting Started' level 2 header.
3. Modify the `pyproject.toml` to change the name of the application to the name of the project.
4. Build and create your application!

## Project Structure
```
python-skeleton
├── end_to_end
│   ├── __init__.py
│   ├── conftest.py
│   └── test_end_to_end.py
├── integration
│   ├── __init__.py
│   ├── conftest.py
│   └── test_integration.py
├── src
│   └── app
│       ├── __init__.py
│       ├── app.py
│       └── config.py
├── test
│   ├── __init__.py
│   ├── conftest.py
│   └── test_app.py
├── docker-entrypoint.sh
├── getting_started.md
├── pyproject.toml
└── README.md
```

### File Purposes:
* `README.md` provides an overview and documentation for the project, typically containing instructions, usage examples, and relevant information for developers and users
* `getting_started.md` contains the directions to get started contributing to the project, and is included as a link in the README.md
* `pyproject.toml` defines project metadata, dependencies, and build system requirements using Poetry
* `docker-entrypoint.sh` provides a simple docker entrypoint to use with docker-compose
* `**/__init__.py` marks a directory as a Python package, allowing its modules to be imported

### Folder Purposes
* `/` root directory
* `/src` contains the app module
* `/src/app` contains the application source code
* `/test` contains all self-contained unit tests for the code contained within the `app` module
* `/integration` contains tests where one or more outside resources, such as postgres or RabbitMQ, are needed, but some interactions with the outside resources still need to be mocked
* `/end_to_end` contains tests that validate the functionality and integration of the application from start to finish without mocking any interaction with any of the outside resources

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

## Project Title

## Points of Contact

## Getting Started
Set up your environment and gather dependencies by following the directions laid out in [Getting Started](getting_started.md).

## Project Specific Information
