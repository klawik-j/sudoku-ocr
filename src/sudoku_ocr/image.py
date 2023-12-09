"""Image properties."""

import logging
from os.path import isfile
from pathlib import Path

from cv2 import imread, imshow, imwrite, waitKey
from imutils import resize
from numpy import ndarray

WAIT_TIME = 2000

logging = logging.getLogger(__name__)  # type: ignore


class Image:
    """True Image class."""

    def __init__(self) -> None:
        """Initialize Image class."""
        self._data: ndarray = None
        self._path: Path = Path()

    def load_image(self, path: Path) -> None:
        """Load image from file."""
        if not isfile(path):
            raise FileNotFoundError(f"file {path} not found")
        else:
            self._data = imread(str(path))
            self._path = path
            logging.debug("Image loaded successful.")

    def save(self, path: Path) -> None:
        """Save image to file."""
        imwrite(path, self.data)
        logging.info(f"Image successful saved to path {path}")

    def resize(self, width: int = 600, height: int = None) -> None:
        """Resize image to desire width."""
        if height:
            self.data = resize(self.data, width=width, height=height)
        else:
            self.data = resize(self.data, width=width)
        logging.debug(f"Image resized to width: {width}.")

    def crop(self, x_start: int, x_end: int, y_start: int, y_end: int) -> None:
        """Crop image."""
        self.data = self.data[y_start:y_end, x_start:x_end]

    def get_cropped(
        self, x_start: int, x_end: int, y_start: int, y_end: int
    ) -> ndarray:
        """Get cropped image."""
        return self.data[y_start:y_end, x_start:x_end]

    def show(self) -> None:
        """Show visual representation of image on screen."""
        imshow("x", self.data)
        waitKey(WAIT_TIME)

    @property
    def data(self) -> ndarray:
        """Image data property."""
        return self._data

    @data.setter
    def data(self, data: ndarray) -> None:
        self._data = data

    @property
    def path(self) -> Path:
        """Image path property."""
        return self._path
