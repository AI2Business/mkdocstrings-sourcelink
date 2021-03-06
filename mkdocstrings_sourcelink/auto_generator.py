"""Automatic source link generation for mkdocstrings."""
import shutil
from abc import ABC, abstractmethod, abstractproperty
from pathlib import Path
from typing import Dict, List, Union

from mkdocstrings_sourcelink.toolbox import Utilities


class BuilderMkDoc(ABC):
    """BuilderMkDoc is the Metaclass of `MkDocGenerator`.

    Args:
        ABC (class): Helper class that provides a standard way to create an ABC using
             inheritance.
    """

    @abstractmethod
    def render_to_markdown(self, element: str) -> str:
        """Abstract the internal method of `render_to_markdown`."""

    @abstractmethod
    def initialize_generate(self) -> None:
        """Abstract the internal method of `initialize_generate`."""

    @abstractmethod
    def generate_docs(self) -> None:
        """Abstract the internal method of `generate_docs`."""

    @abstractmethod
    def generate_static(self) -> None:
        """Abstract the internal method of `generate_static`."""

    @abstractproperty
    def generate(self) -> None:
        """Abstract the property of `generate`."""


class MkDocGenerator(Utilities, BuilderMkDoc):
    """The `MkDocGenerator` generates the documentation with the links to the source code.

    Args:
        Utilities (class): [description]
        BuilderMkDoc (class): Builder class of the abstract methods and property of
             `MkDocGenerator`.
    """

    def __init__(
        self,
        dest_dir: Union[str, Path],
        documentation: Dict[str, Dict[str, List[str]]],
        project_url: Union[str, Dict[str, str]] = None,
        template_dir: Union[str, Path] = None,
        example_dir: Union[str, Path] = None,
        markdown_files: Dict[str, Dict[str, List[str]]] = None,
        titles_size: str = "#",
        underline_title: bool = False,
        source: str = "**source code**",
    ) -> None:
        """Generates the documentation via `MkDocGenerator` with the links to the source.

        Args:
            dest_dir (Union[str, Path]): Destination of the generated documentation.
            documentation (Dict[str, Dict[str, List[str]]], optional): A nested dictionary with the
                 page title, the page filename, and the functions /classes / methods names of the
                 page. The dictionary should look like:
                 `pages = {'page_title':{'filename.md': ['package.module.function']}}`.
            project_url (Union[str, Dict[str, str]], optional): The URL, where the project is
                 hosted and where it should be linked to (including branch and storage).
            template_dir (Union[str, Path], optional): Directory of template files. If template has
                 to be automatically filled out, then the keyword **{{autogenerated}}** has to be
                 used.
            example_dir (Union[str, Path], optional): Directory of example files, especially
                 suitable for `Jupyter-Notebooks`.
            markdown_files (Dict[str, Dict[str, List[str]]], optional): A nested dictionary with
                 the page title, the page filename, and the link to already existing markdown files
                 like **README.md** or **LICENSE**. The dictionary should look like:
                 `pages = {'page_title':{'filename.md': ['existing_file.md']}}`.
            titles_size (str, optional): Defines the initial title size for the headings, which are
                 scaled down by the factor of one "#".
            underline_title (bool, optional): Underline titles of classes, functions, and methods.
            source (str, optional): Name of the source link.

        !!! info "About *documentation*"
            In terms of linking to the project_url, it has to be separated between *specific* and
             *general* linking. If functions or method has to be separately linked, then each
             module of the class `Documentation` has to be called individually like:
            ```python
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
                    }
                }
            ```
            If functions or method has to be generally linked, then just call the class
             `Documentation` is enough. It will be only generated one single link to the start of
              the class.
              ```python
                  pages = {
                      "Documentation": {
                          "auto_generator.md": [
                              "mkdocstrings_sourcelink.auto_generator.MkDocGenerator",
                      }
                  }
              ```
            For more information, please check: **mkdocstrings**
            https://github.com/pawamoy/mkdocstrings

        !!! tip "About *source*"
            Instead of using a string for `source = "**source code**"`, icons can be used instead
             or as combination of string + icon(s) like.
            ```python
                source = ":material-github::material-source-branch: source-code"
            ```
            In case of using material-icons, please check https://pictogrammers.github.io/@mdi/font/5.4.55/
            and replace `mdl` by `material`.

        !!! warning "About *project_url*"
            Keep in mind, that the name of the branch like *master*, *main*, or *dev*, as well as,
             the name of the storage like *blob* for GitHub has to be included.
        """
        self.dest_dir = Path(dest_dir)
        self.documentation = documentation
        self.project_url = project_url
        self.template_dir = Utilities.return_as_Path(template_dir)
        self.example_dir = Utilities.return_as_Path(example_dir)
        self.markdown_files = markdown_files
        self.titles_size = titles_size
        self.underline_title = underline_title
        self.source = source

    def render_to_markdown(self, element: str) -> str:
        """Rendering the element path to mkdocstrings.

        Args:
            element (str): String of they python class, function, or method, which has to be
                 converted to a string in the mkdocstrings format.

        Returns:
            str: Return of the initial string which looks like
                 `mkdocstrings_sourcelink.auto_generator.MkDocGenerator.__init__` into a markdown
                 conformed string.
        """
        object_ = Utilities.import_object(element)
        subblocks = []
        if self.project_url:
            subblocks.append(
                Utilities.make_source_link(object_, self.project_url, self.source)
            )

        subblocks.append(
            Utilities.make_title(object_, self.titles_size, self.underline_title)
        )
        subblocks.append(Utilities.element_to_mkdocstrings(element, self.titles_size))
        return "\n\n".join(subblocks) + "\n\n"

    def initialize_generate(self) -> None:
        """Initialization of the auto documentation generatorion.

        1. Firs removing a possible existing target directory (`dest_dir`).
        2. Copy templates from the template directory the target directory(`dest_dir`).
        3. Copy example from the example directory the target directory (`dest_dir`).
        """
        if self.dest_dir.exists():
            print(f"Cleaning up existing sources directory '{self.dest_dir}'.")
            shutil.rmtree(self.dest_dir)

        if self.template_dir:
            print(
                f"...copying existing sources directory '{self.template_dir}' to '{self.dest_dir}'."
            )
            shutil.copytree(self.template_dir, self.dest_dir)

        if self.example_dir:
            print(
                f"...copying existing sources directory '{self.example_dir}' to '{self.dest_dir}'."
            )
            shutil.copytree(self.example_dir, self.dest_dir)

    def generate_docs(self) -> None:
        """Generated *dynamic* documentation based on calling the elements via dictionary."""
        for title, documentation in self.documentation.items():
            markdown_text = f"{self.titles_size} {title}\n\n---\n\n"
            for file_path, elements in documentation.items():
                markdown_text += "".join(
                    self.render_to_markdown(element) for element in elements
                )
            Utilities.insert_in_file(markdown_text, self.dest_dir.joinpath(file_path))

    def generate_static(self) -> None:
        """Generate *static* documentation based on existing markdown files."""
        if self.markdown_files:
            for _, markdown_files in self.markdown_files.items():
                markdown_text = ""
                for file_path, elements in markdown_files.items():
                    markdown_text += "".join(
                        Path(element).read_text() for element in elements
                    )
                Utilities.insert_in_file(
                    markdown_text, self.dest_dir.joinpath(file_path)
                )

    @property
    def generate(self) -> None:
        """The property `generate` of `MkDocGenerator` creates the final markdown files.

        !!! note "Example: How to use"

            ```python
            >>> from pathlib import Path
            # Import mkdocstrings-sourcelink
            >>> from mkdocstrings_sourcelink import MkDocGenerator
            # Define the dictionary for the documentation
            >>> pages = {
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
            }
            # Define the dictionary for the importing existing markdown files.
            >>> markdown_files = {
                "HOME": {"index.md": ["../README.md"]},
                "CONTRIBUTING": {"contributing.md": ["../CONTRIBUTING.md"]},
                "LICENSE": {"license.md": ["../LICENSE"]},
            }
            >>> root = Path(__file__).resolve().parents[1]
            # Make use of the generate poperty of MkDocGenerator
            >>> MkDocGenerator(
                root / "docs" / "src",
                pages,
                "https://github.com/AI2Business/mkdocstrings-sourcelink/blob/main",
                markdown_files=markdown_files,
                underline_title=True,
                source=":material-github::material-source-branch:",
            ).generate
            >>> ...
            ```
        """
        self.initialize_generate()
        self.generate_docs()
        self.generate_static()
