from pathlib import Path

import pytest

from sudoku_ocr.image import Image


class TestImage:
    def test_load_image_file_not_found(self) -> None:
        image = Image()
        with pytest.raises(FileNotFoundError):
            image.load_image(Path("foo/path/file.py"))

    def test_load_image_load_success(self) -> None:
        image = Image()
        image.load_image(Path("tests/img/no_sudoku2.jpg"))
        assert image.data is not None
        assert image.path is not None

    # TODO
    def test_save_image(self) -> None:
        pass

    def test_resize_image_default_value(self) -> None:
        image = Image()
        image.load_image(Path("tests/img/no_sudoku2.jpg"))
        image.resize()
        assert image.data.shape[1] == 600

    def test_resize_image_custom_value(self) -> None:
        image = Image()
        image.load_image(Path("tests/img/no_sudoku2.jpg"))
        image.resize(width=500)
        assert image.data.shape[1] == 500

    def test_thresholding(self) -> None:
        image = Image()
        image.load_image(Path("tests/img/sudoku1.png"))
        image.resize(10)
        image.thresholding()
        proper_data = [
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [255, 255, 255, 255, 0, 0, 255, 255, 255, 255],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        assert (image.data == proper_data).all()
