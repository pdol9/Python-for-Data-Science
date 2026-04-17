ft_package
==========

## Description

Lightweight Python package example showing namespaces, packages, and modules
plus build/install workflow. It is part of the 42 projects: Python for
data science.

## Ecosystem of Python packages

### Project structure
```
    ft_package/
    ├── ft_package/
    │   ├── __init__.py
    │   └── module.py
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.md
    ├── pyproject.toml
    ├── setup.cfg
    └── tests/
        └── test.py
```

### Packages

A Python package typically includes:

- Source code (modules)
- Metadata (name, version, dependencies)
- Build configuration files

Packages are distributed via repositories such as PyPI and installed using tools
like pip.

Package is a directory that contains Python modules and an importable
```__init__.py``` (or implicit namespace). A package controls what is visible
externally and exposes a public API via ```__init__.py```. By defining imports
in ```__init__.py```, you expose selected functions as part of the package’s
public interface.

#### Example

ft_package/__init__.py

```py
from .module import count_in_list
```

This allows:

```py
from ft_package import count_in_list
```

Without this, users would need:

```py
from ft_package.module import count_in_list
```

### Modules

Modules are single .py files (e.g., module.py). Each module contains functions,
classes, constants and internal helpers. Modules should be kept focused (single
responsibility) and document public functions with docstrings and typing.

### Namespaces

A namespace in Python is a mapping between names (identifiers) and objects. It
determines how names like functions, variables, and classes are resolved when
referenced in code.

There are several layers of namespaces:

* Local namespace: inside a function
* Global namespace: within a module
* Built-in namespace: Python’s predefined names

#### Example

Given:

```py
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto"))
```

Explanation:

- ft_package is a package namespace
- count_in_list is exposed through that namespace (typically via __init__.py)
- Python resolves ```count_in_list``` by looking inside the package namespace

When working with packages, namespaces become important because they define how
code is accessed across files and directories.

## Build system overview

Python packaging uses:

- pyproject.toml → defines build system and dependencies
- setup.cfg → declarative configuration (metadata, options)

Backend vs frontend
- Build backend: tool that actually builds the package (e.g., setuptools)
- Frontend: tool that invokes the build (e.g., pip, build)

In Python packaging, “frontend” and “backend” tools refer to two different
roles in the build and installation process. They are not interchangeable; each
solves a separate problem.

### Build backend

The backend is responsible for how your package is built.

It:

* Converts your source code into distributable formats (.whl, .tar.gz)
* Reads configuration (usually from pyproject.toml or setup.cfg)
* Decides how files are packaged and included

Examples:

* setuptools.build_meta (from setuptools)
* hatchling
* poetry-core
* flit_core

### Build frontend

The frontend is responsible for running the build and installing the package.

It:

* Calls the backend
* Handles dependency resolution
* Installs packages into environments

Examples:

* pip
* build (for building distributions)
* poetry (acts as both frontend and partially backend manager)


#### Example

```py
# Example pyproject.toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

# Example setup.cfg
[metadata]
name = ft_package
version = 0.1.0
description = Example Python package

[options]
packages = find:
install_requires =
    # dependencies here
```

## Installation

```bash
python3 -m build
```

Local install:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Editable install (development mode):

```bash
pip install -e .
```

## REFERENCES
    [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
    [Build System Support](https://setuptools.pypa.io/en/latest/build_meta.html)
