"""Image operation to ocr sudoku out of it."""

from cv2 import (
    CHAIN_APPROX_SIMPLE,
    COLOR_GRAY2BGR,
    RETR_EXTERNAL,
    approxPolyDP,
    arcLength,
    contourArea,
    cvtColor,
    drawContours,
    findContours,
    imshow,
    waitKey,
)
from imutils import grab_contours
from numpy import ndarray

from sudoku_ocr.image import WAIT_TIME, Image, ImageAdapter


class ImageOcrAdapter(ImageAdapter):
    """ImageOcr adapter."""

    def get_contours_in_image(self) -> None:
        """Get contours present in image."""
        ...

    @staticmethod
    def get_largest_rectangle_contours(contours: ndarray) -> ndarray:
        """Look for largest rectangle contours."""
        ...


class ImageOcr(Image, ImageOcrAdapter):
    """ImageOcr class."""

    def __init__(self) -> None:
        """Initialize ImageOcr class."""
        super().__init__()

    def get_contours(self) -> ndarray:
        """Get contours present in image."""
        contours = findContours(
            self.data,
            RETR_EXTERNAL,
            CHAIN_APPROX_SIMPLE,
        )
        contours = grab_contours(contours)
        return sorted(contours, key=contourArea, reverse=True)

    @staticmethod
    def get_largest_rectangle_contours(contours: ndarray) -> ndarray:
        """Look for largest rectangle contours."""
        for cnt in contours:
            approx = approxPolyDP(
                cnt,
                0.02 * arcLength(cnt, True),
                True,
            )
            if len(approx) == 4:
                return approx
        raise Exception("Largest rectangle have not been found.")

    def show_with_contours(self, contours: ndarray) -> None:
        """Show image with contours marked."""
        image_with_contours = cvtColor(self.data, COLOR_GRAY2BGR)
        drawContours(image_with_contours, [contours], -1, (0, 255, 0), 5)
        imshow("Contours", image_with_contours)
        waitKey(WAIT_TIME)
