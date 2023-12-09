"""Image processing."""

import logging

from cv2 import (
    ADAPTIVE_THRESH_GAUSSIAN_C,
    CHAIN_APPROX_SIMPLE,
    COLOR_BGR2GRAY,
    COLOR_GRAY2BGR,
    RETR_EXTERNAL,
    THRESH_BINARY,
    GaussianBlur,
    adaptiveThreshold,
    approxPolyDP,
    arcLength,
    bitwise_not,
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

from sudoku_ocr.image import WAIT_TIME, Image

logging = logging.getLogger(__name__)  # type: ignore


class ImageProcessing(Image):
    """ImageProcessing class."""

    def __init__(self) -> None:
        """Initialize ImageProcessing class."""
        super().__init__()

    def thresholding(self) -> None:
        """Apply thresholding on image."""
        grayscale = cvtColor(self.data, COLOR_BGR2GRAY)
        blurred = GaussianBlur(grayscale, (7, 7), 3)
        thresh = adaptiveThreshold(
            blurred,
            255,
            ADAPTIVE_THRESH_GAUSSIAN_C,
            THRESH_BINARY,
            11,
            2,
        )
        inverse = bitwise_not(thresh)
        self.data = inverse
        logging.debug("Thresholding successful.")

    def get_contours(self) -> ndarray:
        """Get contours present in image."""
        contours = findContours(
            self.data,
            RETR_EXTERNAL,
            CHAIN_APPROX_SIMPLE,
        )
        contours = grab_contours(contours)
        logging.debug(f"Found {len(contours)} contours.")
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
                logging.debug(f"Largest rectangle contours are:\n {approx}")
                return approx
        raise Exception("Largest rectangle have not been found.")

    def adjust_perspective_to_specific_zone(self, zone: ndarray) -> None:
        """Adjust perspective to specific zone."""
        self.data = four_point_transform(self.data, zone.reshape(4, 2))
        logging.debug(f"Perspective adjusted to zone:\n {zone}")

    def improve_data_quality(self) -> None:
        """Improve image data quality for better ocr."""
        self.data = clear_border(self.data)
        logging.debug("Data quality have been improved.")

    def is_empty(self, threshold: int = 5) -> bool:
        """Determine if data does not contain any information."""
        mask = inRange(self.data, 254, 255)
        height, width = mask.shape[:2]
        number_of_pixels = height * width
        count_white = countNonZero(mask)
        percent_white = count_white * 100 / number_of_pixels
        if percent_white < threshold:
            logging.debug(f"Empty: TRUE with {percent_white}% white pixels.")
            return True
        else:
            logging.debug(f"Empty: FALSE with {percent_white}% white pixels.")
            return False

    def show_with_contours(self, contours: ndarray) -> None:
        """Show image with contours marked."""
        image_with_contours = cvtColor(self.data, COLOR_GRAY2BGR)
        drawContours(image_with_contours, [contours], -1, (0, 255, 0), 5)
        imshow("Contours", image_with_contours)
        waitKey(WAIT_TIME)
