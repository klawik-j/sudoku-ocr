"""Image properties."""

from pathlib import Path
from numpy import ndarray
from typing import Protocol
from cv2 import (
    imread,
    cvtColor,
    GaussianBlur,
    adaptiveThreshold,
    ADAPTIVE_THRESH_GAUSSIAN_C,
    THRESH_BINARY,
    bitwise_not,
    COLOR_BGR2GRAY,
    imshow,
    waitKey,
)
from os.path import isfile
from imutils import resize

WAIT_TIME = 2000


class ImageAdapter(Protocol):
    """Image adapter."""

    def load_image(self) -> None:
        ...

    def resize(self) -> None:
        ...

    def thresholding(self) -> None:
        ...

    @property
    def data(self) -> ndarray:
        ...

    @data.setter
    def data(self, data: ndarray) -> None:
        ...

    @property
    def path(self) -> Path:
        ...


class Image(ImageAdapter):
    """True Image class."""

    def __init__(self):
        self._data: ndarray = None
        self._path: Path = None

    def load_image(self, path: Path) -> None:
        """Load image from file."""
        if not isfile(path):
            raise FileNotFoundError(f"file {path} not found")
        else:
            self._data = imread(str(path))
            self._path = path

    def resize(self, width: int = 600) -> None:
        """Resize image to desire width."""
        self.data = resize(self.data, width=width)

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

    def show(self):
        """Show visual representation of image on screen."""
        imshow("x", self.data)
        waitKey(WAIT_TIME)

    @property
    def data(self) -> ndarray:
        return self._data

    @data.setter
    def data(self, data: ndarray) -> None:
        self._data = data

    @property
    def path(self) -> Path:
        return self._path
