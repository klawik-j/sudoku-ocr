from pathlib import Path

import cv2
from numpy import ndarray


class Image:
    """Image class."""

    def __init__(self, path: Path):
        """Initialize Image class."""
        self._path = path
        self._load_img()

    def _load_img(self) -> None:
        """Load image."""
        self._data = cv2.imread(str(self.path))
        if self._data is None:
            raise OSError(f"file {self.path} not found")

    @property
    def data(self) -> ndarray:
        """Return image's data."""
        return self._data

    @property
    def path(self) -> Path:
        """Return path of image."""
        return self._path
