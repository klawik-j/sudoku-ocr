"""Image properties."""

from os.path import isfile
from pathlib import Path

from cv2 import imread, imshow, imwrite, waitKey
from imutils import resize
from numpy import ndarray

WAIT_TIME = 2000


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

    def save(self, path: Path) -> None:
        """Save image to file."""
        imwrite(path, self.data)

    def resize(self, width: int = 600) -> None:
        """Resize image to desire width."""
        self.data = resize(self.data, width=width)

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
