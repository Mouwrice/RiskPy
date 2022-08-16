# Contributing to RiskPy

## Local development setup

### Poetry

We use Poetry for dependency management so that you don't have to install the packages system wide

1. Make sure you have poetry installed: https://python-poetry.org/docs/master/#installation
2. Run `poetry install`

### pre-commit

pre-commit allows us to apply some checks before commiting. As to ensure code style and commit message conventions

1. Install pre-commit: https://pre-commit.com/#install
2. Run: `poetry run pre-commit install`

### Black

[black](https://github.com/psf/black) is the Python formatter we use. It will format your code upon commit.

### flake8

[flake8](https://flake8.pycqa.org/en/latest/) checks if your code conforms to most of the PEP8 rules

### conventional-commits

[conventional-commits](https://github.com/compilerla/conventional-pre-commit) ensures your commit message comply
to the conventional commits formatting, which can be used for semantic versioning.

## Pull Requests

You are free to create pull requests. They will tell you when your code format is not following the black style
or the flake8 rules. Also enforces you to use the conventional commit structure for your PR title.
