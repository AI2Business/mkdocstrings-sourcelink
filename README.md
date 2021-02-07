[![Python Package](https://github.com/AI2Business/mkdocstrings-sourcelink/workflows/Python%20Package/badge.svg)](https://github.com/AI2Business/mkdocstrings-sourcelink/actions)
[![Docs](https://github.com/AI2Business/mkdocstrings-sourcelink/workflows/Python%20Package/badge.svg)](https://ai2business.github.io/mkdocstrings-sourcelink/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/AI2Business/mkdocstrings-sourcelink/main.svg)](https://results.pre-commit.ci/latest/github/AI2Business/mkdocstrings-sourcelink/main)
[![codecov](https://codecov.io/gh/AI2Business/mkdocstrings-sourcelink/branch/main/graph/badge.svg?token=DKE0SHCRF7)](https://codecov.io/gh/AI2Business/mkdocstrings-sourcelink)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/ambv/black)

# mkdocstrings-sourcelink

![_](https://github.com/AI2Business/mkdocstrings-sourcelink/blob/main/docs/assets/img/export.png?raw=true)

> Automatic source link generation for [mkdocstrings](https://github.com/pawamoy/mkdocstrings)

## Overview

`mkdocstrings-sourcelink` is a source link generator for [mkdocstrings](https://github.com/pawamoy/mkdocstrings), which allows connecting the source code to a repository independent of the host ([GitHub](https://github.com), [GitLab](https://github.com), own Services).

The original idea of is coming from [keras-autodoc](https://github.com/keras-team/keras-autodoc) and strongly modified to use [mkdocstrings](https://github.com/pawamoy/mkdocstrings) as well as `class properties` . In this regards, `mkdocstrings-sourcelink` is a pure python implementation, which not requires any additional packages.

## Installation

``` shell
pip install mkdocstrings-sourcelink
```

## Usage

The usage requires just three steps:

1. `❯ python generate_docs.py`
2. `mkdocs.yml`
3. `❯ mkdocs deploy`
