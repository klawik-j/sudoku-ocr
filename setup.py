from pathlib import Path
from typing import List

from setuptools import find_packages, setup

BASE_PROJECT_DIR = Path(__file__).absolute().parent


def get_requirements() -> List[str]:
    """Load requirements."""
    requirements_path = BASE_PROJECT_DIR.joinpath("requirements.txt")
    with open(requirements_path, "r") as stream:
        return [pkg.strip("\n") for pkg in stream if pkg != ""]


def get_long_description() -> List[str]:
    """Load long description."""
    with open("README.md", "r", encoding="utf-8") as stream:
        return stream.read()


setup(
    name="sudoku-ocr",
    author="Jakub Klawikowski",
    author_email="klawik.j@gmail.com",
    description="Package to ocr sudoku",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/klawik-j/sudoku-ocr",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    setup_requires=["setuptools_scm >= 6.2"],
    install_requires=get_requirements(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
