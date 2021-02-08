from pathlib import Path

from setuptools import find_packages, setup

this_file = Path(__file__).resolve()
readme = this_file.parent / "README.md"


setup(
    name="mkdocstrings_sourcelink",
    version="0.3.1",
    packages=find_packages(),
    package_data={"": ["README.md"]},
    url="https://ai2business.github.io/mkdocstrings-sourcelink/",
    download_url="https://github.com/AI2Business/mkdocstrings-sourcelink",
    author="AI2Business",
    author_email="ai2business@protonmail.com",
    description="Automatic source link generation for mkdocstrings.",
    long_description=readme.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    extras_require={"tests": ["pytest", "pytest-cov"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Topic :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="markdown, mkdocs, mkdocstrings, docstrings, auto-doc, development",
    python_requires=">=3.6, <4",
    project_urls={
        "Bug Reports": "https://github.com/AI2Business/mkdocstrings-sourcelink/issues",
        "Source": "https://github.com/AI2Business/mkdocstrings-sourcelink/tree/main/mkdocstrings_sourcelink",
    },
)
