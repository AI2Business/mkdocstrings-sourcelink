""" [summary] [extended_summary] """
import shutil
from abc import ABC, abstractmethod, abstractproperty
from pathlib import Path
from typing import Dict, List, Union

from mkdocstrings_sourcelink.toolbox import Utilities


class BuilderMkDoc(ABC):
    """BuilderMkDoc [summary]

    [extended_summary]

    Args:
        ABC ([type]): [description]
    """

    @abstractmethod
    def _render(self, element: str) -> str:
        """Abstract the internal method of `_render`."""

    @abstractmethod
    def _initialize_generate(self) -> None:
        """Abstract the internal method of `_initialize_generate`."""

    @abstractmethod
    def _generate_docs(self) -> None:
        """Abstract the internal method of `_generate_docs`."""

    @abstractmethod
    def _generate_static(self) -> None:
        """Abstract the internal method of `_generate_static`."""

    @abstractproperty
    def generate(self) -> None:
        """Abstract the property of `generate`."""


class MkDocGenerator(Utilities, BuilderMkDoc):
    """Generates the documentation."""

    def __init__(
        self,
        dest_dir: str,
        documentation: Dict[str, Dict[str, List[str]]] = {},
        project_url: Union[str, Dict[str, str]] = None,
        template_dir: str = None,
        examples_dir: str = None,
        markdown_files: Dict[str, Dict[str, List[str]]] = None,
        titles_size: str = "##",
        source: str = "**source code**",
        icon: str = None,
    ) -> None:
        """__init__ [summary]

        [extended_summary]

        Args:
            dest_dir (str): [description]
            documentation (Dict[str, Dict[str, List[str]]], optional): [description]. Defaults to {}.
            project_url (Union[str, Dict[str, str]], optional): [description]. Defaults to None.
            template_dir (str, optional): [description]. Defaults to None.
            examples_dir (str, optional): [description]. Defaults to None.
            markdown_files (Dict[str, Dict[str, List[str]]], optional): [description]. Defaults to None.
            titles_size (str, optional): [description]. Defaults to "##".
            source (str, optional): [description]. Defaults to "**source code**".
            icon (str, optional): [description]. Defaults to None.
        """
        self.dest_dir = Path(dest_dir)
        self.documentation = documentation
        self.project_url = project_url
        self.template_dir = Utilities.return_as_Path(template_dir)
        self.examples_dir = Utilities.return_as_Path(examples_dir)
        self.markdown_files = markdown_files
        self.titles_size = titles_size
        self.source = source
        self.icon = icon

    def _render(self, element: str) -> str:
        """_render [summary]

        [extended_summary]

        Args:
            element (str): [description]

        Returns:
            str: [description]
        """
        if isinstance(element, str):
            object_ = Utilities.import_object(element)
            if Utilities.ismethod(object_):
                # we remove the modules when displaying the methods
                signature_override = ".".join(element.split(".")[-2:])
            else:
                signature_override = element
        else:
            signature_override = None
            object_ = element

        subblocks = []
        if self.project_url:
            subblocks.append(
                Utilities.make_source_link(
                    object_, self.project_url, self.icon, self.source
                )
            )

        subblocks.append(Utilities.make_title(object_, self.titles_size))
        subblocks.append(Utilities.element_to_mkdocstrings(signature_override))
        return "\n\n".join(subblocks) + "\n\n----\n\n"

    def _initialize_generate(self) -> None:
        """_initialize_generate [summary]

        [extended_summary]
        """
        if self.dest_dir.exists():
            print(f"Cleaning up existing sources directory '{self.dest_dir}'.")
            shutil.rmtree(self.dest_dir)

        if self.template_dir:
            print(
                f"...copying existing sources directory '{self.template_dir}' to '{self.dest_dir}'."
            )
            shutil.copytree(self.template_dir, self.dest_dir)

        if self.examples_dir:
            print(
                f"...copying existing sources directory '{self.examples_dir}' to '{self.dest_dir}'."
            )
            shutil.copytree(self.example_dir, self.dest_dir)

    def _generate_docs(self) -> None:
        """_generate_docs [summary]

        [extended_summary]
        """
        for title, documentation in self.documentation.items():
            markdown_text = f"# {title}\n\n---\n\n"
            for file_path, elements in documentation.items():
                markdown_text += "".join(self._render(element) for element in elements)
            Utilities.insert_in_file(markdown_text, self.dest_dir.joinpath(file_path))

    def _generate_static(self) -> None:
        """_generate_static [summary]

        [extended_summary]
        """
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
        """generate [summary]

        [extended_summary]
        """

        self._initialize_generate()
        self._generate_docs()
        self._generate_static()
