"""Image operation to ocr sudoku out of it."""

from cv2 import (
    CHAIN_APPROX_SIMPLE,
    COLOR_GRAY2BGR,
    RETR_EXTERNAL,
    GaussianBlur,
    approxPolyDP,
    arcLength,
    contourArea,
    countNonZero,
    cvtColor,
    drawContours,
    findContours,
    imshow,
    inRange,
    waitKey,
)
from imutils import grab_contours
from imutils.perspective import four_point_transform
from numpy import ndarray
from skimage.segmentation import clear_border

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

    def adjust_perspective_to_specific_zone(self, zone: ndarray) -> None:
        """Adjust perspective to specific zone."""
        self.data = four_point_transform(self.data, zone.reshape(4, 2))

    def improve_data_quality(self) -> None:
        """Improve image data quality for better ocr."""
        blurred = GaussianBlur(self.data, (7, 7), 1)
        self.data = clear_border(blurred)

    def is_empty(self, threshold: int = 5) -> bool:
        """Determine if data does not contain any information."""
        mask = inRange(self.data, 254, 255)
        height, width = mask.shape[:2]
        number_of_pixels = height * width
        count_white = countNonZero(mask)
        percent_white = count_white * 100 / number_of_pixels
        if percent_white < threshold:
            return True
        else:
            return False

    def show_with_contours(self, contours: ndarray) -> None:
        """Show image with contours marked."""
        image_with_contours = cvtColor(self.data, COLOR_GRAY2BGR)
        drawContours(image_with_contours, [contours], -1, (0, 255, 0), 5)
        imshow("Contours", image_with_contours)
        waitKey(WAIT_TIME)
