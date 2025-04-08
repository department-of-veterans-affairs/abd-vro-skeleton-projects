# Getting started

## Install Python 3.12
If you're on a Mac, you can use pyenv to handle multiple python versions

```
brew install pyenv
pyenv install 3.12
```

Set the global python so all further commands use installed version, or don't do this if you want a different version available globally for your system.
```
pyenv global 3.12
```

## Install Poetry
Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

```
curl -sSL https://install.python-poetry.org | python3 -
```

## Install dependencies
From your project folder, install dependencies using Poetry:

```
poetry install
```

## Activate the virtual environment
For Poetry 2.0.0+, you need to install the shell plugin first:

```
poetry self add poetry-plugin-shell
```

Then you can activate the virtual environment:

```
poetry shell
```

Alternatively, you can run commands directly without activating the virtual environment:

```
poetry run <command>
```

## Unit, Integration, & End-to-End Tests

Make sure your virtual env is activated or use `poetry run` before each command.

Navigate to the project folder and run the tests:

* Via pytest directly
    ```
    poetry run pytest .
    poetry run pytest ./integration
    poetry run pytest ./end_to_end
    ```

* Run linting and type checking
    ```
    poetry run ruff check .
    poetry run mypy src
    ```

* Format code
    ```
    poetry run ruff format .
    ```

* Run security checks
    ```
    poetry run bandit -r src
    ```
