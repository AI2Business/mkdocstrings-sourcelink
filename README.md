[![Python Package](https://github.com/AI2Business/mkdocstrings-sourcelink/workflows/Python%20Package/badge.svg)](https://github.com/AI2Business/mkdocstrings-sourcelink/actions)
[![GitHub branch checks state](https://img.shields.io/github/checks-status/ai2business/mkdocstrings-sourcelink/gh-pages?label=docs&logo=github%20actions)](https://ai2business.github.io/mkdocstrings-sourcelink/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/AI2Business/mkdocstrings-sourcelink/main.svg)](https://results.pre-commit.ci/latest/github/AI2Business/mkdocstrings-sourcelink/main)
[![codecov](https://codecov.io/gh/AI2Business/mkdocstrings-sourcelink/branch/main/graph/badge.svg?token=DKE0SHCRF7)](https://codecov.io/gh/AI2Business/mkdocstrings-sourcelink)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/ambv/black)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/AI2Business/mkdocstrings-sourcelink.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/AI2Business/mkdocstrings-sourcelink/context:python)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocstrings-sourcelink?logo=python&logoColor=yellow)](https://pypi.org/project/mkdocstrings-sourcelink/)
[![PyPI](https://img.shields.io/pypi/v/mkdocstrings-sourcelink?logo=PyPi&logoColor=yellow)](https://pypi.org/project/mkdocstrings-sourcelink/)

# mkdocstrings-sourcelink

![_](https://github.com/AI2Business/mkdocstrings-sourcelink/blob/main/docs/assets/img/export.png?raw=true)

> Automatic source link generation for [mkdocstrings](https://github.com/pawamoy/mkdocstrings)

## Overview

`mkdocstrings-sourcelink` is a source link generator for [mkdocstrings](https://github.com/pawamoy/mkdocstrings), which allows connecting the source code to a repository independent of the host ([GitHub](https://github.com), [GitLab](https://github.com), own Services).

The original idea of `mkdocstrings-sourcelink` was coming from [keras-autodoc](https://github.com/keras-team/keras-autodoc) and used as inspiration. However, this implementation focuses on using straight [mkdocstrings](https://github.com/pawamoy/mkdocstrings) and not rephrase docstrings into the documentation. Furthermore, `mkdocstrings-sourcelink` also allows:

1. Generating API list
2. Using templates and examples
3. Importing existing markdown files like [README.md](https://github.com/AI2Business/mkdocstrings-sourcelink/blob/main/README.md)

## Installation

``` shell
pip install mkdocstrings-sourcelink
```

## Usage

The usage requires just three steps:

1. `❯ python generate_docs.py`
2. `❯ mkdocs.yml`
3. `❯ mkdocs deploy`
