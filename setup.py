from pathlib import Path

from setuptools import find_packages, setup

BASE_PROJECT_DIR = Path(__file__).absolute().parent


def get_long_description() -> str:
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
    python_requires=">=3.10",
    setup_requires=["setuptools_scm >= 6.2"],
    install_requires=[
        "imutils  == 0.5.4",
        "opencv-python == 4.8.0.76",
        "scikit-image == 0.18.2",
        "tensorflow == 2.8.0",
        "py-sudoku == 1.0.2",
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
