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

    def test_resize_image_custom_width_value(self) -> None:
        image = Image()
        image.load_image(Path("tests/img/no_sudoku2.jpg"))
        image.resize(width=500)
        assert image.data.shape[1] == 500

    # TODO
    def test_resize_image_custom_heigh_value(self) -> None:
        pass

    # TODO
    def test_crop(self) -> None:
        pass

    # TODO
    def test_get_cropped(self) -> None:
        pass
