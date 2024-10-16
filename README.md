# abd-vro-skeleton-projects
Repo for skeletons for new VRO projects.


## How to use
1. Copy-paste the skeleton directory into the desired location and rename the directory.
2. Modify the `README.md` to show the project title and add any additional project information after the 'Getting Started' level 2 header.
3. Modify the `pyproject.toml` to change the name of the application to the name of the project. 
4. Add more options to `build.gradle`, add the project to a `docker-compose.yml`, and add to repository's `settings.gradle`.
5. Build and create your application!


## Python-Skeleton
### File-Folder Structure
```
python-skeleton
└── end_to_end
    ├── __init__.py
    ├── conftest.py
    └── test_end_to_end.py
└── integration
    ├── __init__.py
    ├── conftest.py
    └── test_integration.py
└── src
    └── app
        ├── __init__.py
        ├── app.py
        └── config.py
    ├── dev-requirements.txt
    └── requirements.txt
└── test
    ├── __init__.py
    ├── conftest.py
    └── test_app.py
├── build.gradle
├── docker-entrypoint.sh
├── getting_started.md
├── gradle.properties
├── pyproject.toml
└── README.md
```

#### File Purposes:
* `README.md` provides an overview and documentation for the project, typically containing instructions, usage examples, and relevant information for developers and users
* `getting_started.md` contains the directions to get started contributing to the project, and is included as a link in the README.md
* `pyproject.toml` defines project metadata, dependencies, and build system requirements for Python projects, enabling standardized project configuration and packaging
* `build.gradle` defines a project's build configuration, dependencies, and tasks for automation using the Gradle build system
* `gradle.properties` defines configuration properties and settings that customize the behavior of the Gradle build system, such as system variables, JVM arguments, and project-wide settings
* `docker-entrypoint.sh` provides a very simple docker entrypoint to use with docker-compose
* `/src/dev-requirements.txt` contains project dependencies needed for running tests
* `/src/requirements.txt` contains project dependencies needed for running the application
* `**/__init__.py` marks a directory as a Python package, allowing its modules to be imported, and optionally to execute initialization code for the package

#### Folder Purposes
* `/` root directory
* `/src` contains the app module and the dependency requirement files `dev-requirements.txt` and `requirements.txt`
* `/src/app` this module contains the application source code
* `/test` contains all self contained unit tests for the code contained within the `app` module`
* `/integration` contains tests where one or more outside resources, such as postgres or RabbitMQ, are needed, but some interactions with the outside resources still need to be mocked
* `/end_to_end` contains tests that validate the functionality and integration of the application from start to finish without mocking any interaction with any of the outside resources
