from sudoku_ocr.image import Image
import pytest


class TestImage:
    def test_load_image_file_not_found(self):
        image = Image()
        with pytest.raises(FileNotFoundError):
            image.load_image("foo/path/file.py")

    def test_load_image_load_success(self):
        image = Image()
        image.load_image("tests/img/no_sudoku2.jpg")
        assert image.data is not None
        assert image.path is not None

    def test_resize_image_default_value(self):
        image = Image()
        image.load_image("tests/img/no_sudoku2.jpg")
        image.resize()
        assert image.data.shape[1] == 600

    def test_resize_image_custom_value(self):
        image = Image()
        image.load_image("tests/img/no_sudoku2.jpg")
        image.resize(width=500)
        assert image.data.shape[1] == 500

    def test_thresholding(self):
        image = Image()
        image.load_image("tests/img/sudoku1.png")
        image.resize(10)
        image.thresholding()
        assert (
            image.data
            == [
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
        ).all()
