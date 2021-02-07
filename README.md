# mkdocstrings-sourcelink

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

