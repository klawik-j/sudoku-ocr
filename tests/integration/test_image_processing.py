from pathlib import Path

import pytest
from cv2 import COLOR_BGR2GRAY, cvtColor
from numpy import array

from sudoku_ocr.image_processing import ImageProcessing


class TestImageProcessing:
    def test_thresholding(self) -> None:
        image = ImageProcessing()
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

    # TODO
    def test_get_contours(self) -> None:
        pass

    # TODO
    def test_get_largest_rectangle_contours(self) -> None:
        pass

    def test_adjust_perspective_to_specific_zone(self) -> None:
        zone = array(
            [
                [460, 272],
                [92, 276],
                [45, 679],
                [512, 666],
            ]
        )
        image = ImageProcessing()
        image.load_image(Path("tests/img/sudoku1.png"))
        image.resize()
        image.thresholding()
        image.adjust_perspective_to_specific_zone(zone)
        image_to_compare_with = ImageProcessing()
        image_to_compare_with.load_image(
            Path("tests/img/sudoku1_test_adjust_perspective.png")
        )
        image_to_compare_with = cvtColor(image_to_compare_with.data, COLOR_BGR2GRAY)

        assert (image.data == image_to_compare_with.data).all()

    # TODO
    def test_improve_data_quality(self) -> None:
        pass

    @pytest.mark.parametrize(
        ["path", "expected"],
        [
            pytest.param(
                Path("tests/img/cells/sudoku1_cell0.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell1.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell2.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell3.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell4.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell5.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell6.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell7.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell8.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell9.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell10.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell11.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell12.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell13.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell14.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell15.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell16.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell17.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell18.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell19.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell20.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell21.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell22.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell23.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell24.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell25.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell26.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell27.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell28.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell29.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell30.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell31.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell32.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell33.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell34.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell35.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell36.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell37.png"),
                False,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell38.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell39.png"),
                True,
            ),
            pytest.param(
                Path("tests/img/cells/sudoku1_cell40.png"),
                False,
            ),
        ],
    )
    def test_is_empty(self, path: Path, expected: bool) -> None:
        image = ImageProcessing()
        image.load_image(path)
        image.data = cvtColor(image.data, COLOR_BGR2GRAY)
        assert image.is_empty() == expected
