from pathlib import Path

from mkdocstrings_sourcelink import MkDocGenerator

pages = {
    "Documentation": {
        "auto_generator.md": [
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator.__init__",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator._render",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator._initialize_generate",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator._generate_docs",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator._generate_static",
            "mkdocstrings_sourcelink.auto_generator.MkDocGenerator.generate",
        ]
    },
    "Tools": {
        "toolbox.md": [
            # "mkdocstrings_sourcelink.toolbox.Utilities",
            "mkdocstrings_sourcelink.toolbox.Utilities.insert_in_file",
            "mkdocstrings_sourcelink.toolbox.Utilities.element_to_mkdocstrings",
            "mkdocstrings_sourcelink.toolbox.Utilities.make_source_link",
            "mkdocstrings_sourcelink.toolbox.Utilities.make_title",
            "mkdocstrings_sourcelink.toolbox.Utilities.ismethod",
            "mkdocstrings_sourcelink.toolbox.Utilities.import_object",
            "mkdocstrings_sourcelink.toolbox.Utilities.return_as_Path",
        ],
    },
}
markdown_files = {"HOME": {"index.md": ["../README.md"]}}
root = Path(__file__).resolve().parents[1]
MkDocGenerator(
    root / "docs" / "src",
    pages,
    "https://github.com",
    markdown_files=markdown_files,
    underline_title=True,
    source=":material-github::material-source-branch:",
).generate
