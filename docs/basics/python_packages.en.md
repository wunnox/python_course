# Python Packages

To create a package in Python, follow these steps:

## Create a directory structure

Create a directory structure for your package. A simple example might look like this:

```text
my_package/
    ├── my_package/
    │   ├── __init__.py
    │   ├── module1.py  
    │   └── module2.py
    ├── tests/
    ├── README.md
    ├── LICENSE
    └── pyproject.toml
```

## Create the __init__.py file

The `__init__.py` file in the root directory of your package is crucial. It can be empty or contain code that is executed when the package is imported.

## Create modules

Create Python files (.py) as the various modules of your package.

## Create the pyproject.toml file

The `pyproject.toml` file is important for configuring the build system and the package’s metadata. Here is an example:

```text
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mein_paket"
version = "0.0.1"
authors = [
  { name="Ihr Name", email="ihre.email@example.com" },
]
description = "Eine kurze Beschreibung Ihres Pakets"
readme = "README.md"
requires-python = ">=3.10"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/mein_paket"
"Bug Tracker" = "https://github.com/yourusername/mein_paket/issues"
```

Download: [pyproject.toml](../examples/basics/pyproject.toml)

## Create README.md and LICENSE files

Create a `README.md` file with a description of your package and usage instructions. Also include a `LICENSE` file that sets out the terms of use for your package.

## Build the package

Use the build module to create distribution files:

```bash
python -m pip install --upgrade build
python -m build
```

This creates a .whl file (Wheel) and a .tar.gz file in the dist/ directory.

## Testing the package

Test your package locally by installing it in a virtual environment:

```bash
python -m venv test_env
source test_env/bin/activate # On Windows: test_env\Scripts\activate
pip install dist/my_package-0.0.1-py3-none-any.whl
```

## Publish the package (optional)

If you wish to publish your package on PyPI, you can use the twine tool:

```bash
python -m pip install --upgrade twine
python -m twine upload dist/*
```

> NOTE:
> Please note that you will need an account on PyPI for this step.
