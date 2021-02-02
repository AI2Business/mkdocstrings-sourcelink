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
_dir = root / "test" / "docs" / "src"


def test_basic_1():

    MkDocGenerator(
        _dir,
        pages,
        "https://github.com/AI2Business/mkdocstrings-sourcelink",
    ).generate
    assert len(list(_dir.glob("*.md"))) == 3


def test_basic_2():

    MkDocGenerator(
        _dir,
        pages,
        "https://github.com/AI2Business/mkdocstrings-sourcelink",
        underline_title=True,
    ).generate
    assert len(list(_dir.glob("*.md"))) == 3


def test_dict_url():

    MkDocGenerator(
        _dir,
        pages,
        {
            "mkdocstrings_sourcelink": "https://github.com/AI2Business/mkdocstrings-sourcelink"
        },
    ).generate
    assert len(list(_dir.glob("*.md"))) == 3