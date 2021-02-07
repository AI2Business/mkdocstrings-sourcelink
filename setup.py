from pathlib import Path

from setuptools import find_packages, setup

this_file = Path(__file__).resolve()
readme = this_file.parent / "README.md"


setup(
    name="mkdocstrings_sourcelink",
    version="0.3.0",
    packages=find_packages(),
    package_data={"": ["README.md"]},
    author="AI2Business",
    author_email="ai2business@protonmail.com",
    description="Automatic source link generation for mkdocstrings.",
    long_description=readme.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/AI2Business/mkdocstrings-sourcelink",
    license="Apache License 2.0",
    extras_require={"tests": ["pytest", "pytest-cov"]},
    classifiers=[
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "Topic :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
    ],
)
