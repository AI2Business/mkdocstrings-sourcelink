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

## Example

A `generate_docs.py` file like for `mkdocstrings-sourcelink` can look like:

```python
from pathlib import Path

from mkdocstrings_sourcelink import MkDocGenerator

pages = {
    "Documentation": {
        "auto_generator.md": [
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator.__init__",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator.render_to_markdown",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator.initialize_generate",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator.generate_docs",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator.generate_static",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator.generate",
        ]
    },
    "Tools": {
        "toolbox.md": [
            "mkdocstrings_sourcelink.toolbox.Utilities.insert_in_file",
            "mkdocstrings_sourcelink.toolbox.Utilities.element_to_mkdocstrings",
            "mkdocstrings_sourcelink.toolbox.Utilities.make_source_link",
            "mkdocstrings_sourcelink.toolbox.Utilities.make_title",
            "mkdocstrings_sourcelink.toolbox.Utilities.import_object",
            "mkdocstrings_sourcelink.toolbox.Utilities.return_as_Path",
        ],
    },
    "API": {
        "api.md": [
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator",
            "mkdocstrings_sourcelink.toolbox.Utilities",
        ],
    },
}
markdown_files = {"HOME": {"index.md": ["../README.md"]}}
root = Path(__file__).resolve().parents[1]
MkDocGenerator(
    root / "docs" / "src",
    pages,
    "https://github.com/AI2Business/mkdocstrings-sourcelink/blob/main",
    markdown_files=markdown_files,
    underline_title=True,
    source=":material-github::material-source-branch:",
).generate
```

And will generate the [docs](https://ai2business.github.io/mkdocstrings-sourcelink/)
