import logging
from pathlib import Path

import pytest

from sudoku_ocr.image import Image

CORRECT_FILE_PATH = Path("tests/img/sudoku1.png")
INCORRECT_FILE_PATH = Path("incorrect/file/path")

def test_load_existing_file():
    """Test load existing file."""
    image = Image(CORRECT_FILE_PATH)
    assert image.path == CORRECT_FILE_PATH
    assert image.data.any()

def test_load_non_existing_file():
    "Test load non existing file."
    with pytest.raises(OSError) as err:
        Image(INCORRECT_FILE_PATH)