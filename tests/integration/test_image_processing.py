from pathlib import Path

from cv2 import COLOR_BGR2GRAY, cvtColor
from numpy import array

from sudoku_ocr.image_processing import ImageProcessing


class TestImageProcessing:
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

    # TODO
    def test_is_empty_true(self) -> None:
        pass

    # TODO
    def test_is_empty_false(self) -> None:
        pass
