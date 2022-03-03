import logging
from math import sqrt
from pathlib import Path
from typing import List

import cv2
from imutils import grab_contours, resize
from imutils.perspective import four_point_transform
from numpy import array, expand_dims, fromstring, ndarray, uint8, zeros
from skimage.segmentation import clear_border
from sudoku import Sudoku, sudoku
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

from sudoku_ocr.image import Image

LOGGER = logging.getLogger(__name__)
WAIT_TIME = 2000


class Board:
    """Class of a sudoku board."""

    def __init__(self) -> None:
        """Init Board class."""
        self.load_SNN_model(Path(__file__).absolute().parent.joinpath("cnn.h5"))

    def prepare_img(self, img_path: Path) -> None:
        """Load board img.

        Args:
            img_path (Path): path to board img

        Raises:
            err: no board image have been found
        """
        self.original_img = Image(img_path).data
        self._img_path = img_path
        self.resize_img = resize(self.original_img, width=600)

    def prepare_img_from_data(self, img_file: bytes) -> None:
        """Load board image from file.

        Args:
            img_file (ndarray): img data
        """
        self.original_img = cv2.imdecode(fromstring(img_file, uint8), cv2.IMREAD_UNCHANGED)
        self.resize_img = resize(self.original_img, width=600)

    def load_SNN_model(self, model_path: Path) -> None:
        """Load SNN model.

        Args:
            model_name (str): name of SNN model

        Raises:
            err: SNN model file have not been found
        """
        self.model = load_model(model_path)

    def ocr_sudoku(self) -> None:
        """OCR sudoku."""
        if not self._img_path or not self.original_img.any():
            raise ValueError("image not loaded")

        self.image_thresh = self._thresholding_image(self.resize_img)
        self.board_contours = self._find_board_contour(
            self._find_contours(self.image_thresh),
        )
        self.board = self._adjust_perspective(
            self.resize_img,
            self.board_contours,
        )
        self.cells_cords = self._find_cells(self.board)
        self._board_value = self._board_img_to_board_value()

    def solve(self) -> None:
        """Sove sudoku."""
        puzzle = Sudoku(3, 3, board=self.board_value.tolist())
        try:
            self._solved_board = puzzle.solve(raising=True).board
        except sudoku.UnsolvableSudoku:
            self._solved_board = zeros((9, 9), int).tolist()

    @property
    def solved_board(self) -> list:
        """Return solved board."""
        return self._solved_board

    @property
    def board_value(self) -> array:
        """Return board representation as array."""
        return self._board_value

    @board_value.setter
    def board_value(self, value: array) -> None:
        """Set board value."""
        self._board_value = array(value)

    def _board_img_to_board_value(self) -> array:
        """Return board represetation as array from img."""
        board_value = []
        for cell_cords in self.cells_cords:
            cell = self.board[
                cell_cords[2] : cell_cords[3],  # noqa: E203
                cell_cords[0] : cell_cords[1],  # noqa: E203
            ]
            improved_cell = self._cell_image_impovement(cell)
            if not self._cell_is_empty(improved_cell):
                digit = self._find_digit(improved_cell)
                if digit == 0:
                    digit = 8
                board_value.append(digit)
            else:
                board_value.append(0)
        board_size = int(sqrt(len(board_value)))
        board_value = array(board_value)
        return board_value.reshape(board_size, board_size)

    @staticmethod
    def _thresholding_image(img: ndarray) -> ndarray:
        """Apply thresholding_image on image.

        Args:
            img (ndarray): image

        Returns:
            ndarray: treshold of image
        """
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(grayscale, (7, 7), 3)
        thresh = cv2.adaptiveThreshold(
            blurred,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2,
        )
        inverse = cv2.bitwise_not(thresh)
        return inverse

    @staticmethod
    def _find_contours(img: ndarray) -> ndarray:
        """Find contours.

        Args:
            img (ndarray): image

        Returns:
            ndarray: all contours in image
        """
        contours = cv2.findContours(
            img,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )
        contours = grab_contours(contours)
        return sorted(contours, key=cv2.contourArea, reverse=True)

    @staticmethod
    def _find_board_contour(contours: ndarray) -> ndarray:
        """Look for contours of sudoku board.

        Args:
            contours (ndarray): all contours in image

        Raises:
            Exception: contours in image are not sudoku board

        Returns:
            ndarray: sudoku board contours
        """
        const = 0.02
        for cnt in contours:
            approx = cv2.approxPolyDP(
                cnt,
                const * cv2.arcLength(cnt, True),
                True,
            )
            if len(approx) == 4:
                return approx
        raise Exception("Sudoku board have not been found")

    @staticmethod
    def _adjust_perspective(img: ndarray, board_contours: ndarray) -> ndarray:
        """Adjust perspective.

        Use four point transformation

        Args:
            img (ndarray): image
            board_contours (ndarray): contours fo board

        Returns:
            ndarray: image of board and nothing else
        """
        board = four_point_transform(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), board_contours.reshape(4, 2))
        return board

    @staticmethod
    def _find_cells(board: ndarray) -> List:
        """Look for cells coordinates.

        Args:
            board (ndarray): image of board

        Returns:
            List: list of coordinates

        +---+---+---+---+---+---+---+---+---+
        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        +---+---+---+---+---+---+---+---+---+
        | 9 | 10| 11| 12| 13| 14| 15| 16| 17|
        +---+---+---+---+---+---+---+---+---+

        .
        .
        .
        +---+---+---+---+---+---+---+---+---+
        | 80| 81| 82| 83| 84| 85| 86| 87| 88|
        +---+---+---+---+---+---+---+---+---+
        """
        cell_width = board.shape[1] // 9
        cell_height = board.shape[0] // 9

        cells_cords = []

        for y in range(0, 9):
            for x in range(0, 9):
                cell_x_start = x * cell_width
                cell_x_end = (x + 1) * cell_width
                cell_y_start = y * cell_height
                cell_y_end = (y + 1) * cell_height

                cell = (cell_x_start, cell_x_end, cell_y_start, cell_y_end)
                cells_cords.append(cell)

        return cells_cords

    @staticmethod
    def _cell_image_impovement(cell: ndarray) -> ndarray:
        """Improve cell's img."""
        # blurred = cv2.GaussianBlur(cell, (7, 7), 1)
        thresh = cv2.threshold(cell, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        thresh = clear_border(thresh)

        return thresh

    @staticmethod
    def _cell_is_empty(cell: ndarray) -> bool:
        """Determine if cell is empty or not."""
        mask = cv2.inRange(cell, 254, 255)
        height, width = mask.shape[:2]
        number_of_pixels = height * width
        count_white = cv2.countNonZero(mask)
        percent_white = count_white * 100 / number_of_pixels

        if percent_white < 5:
            return True
        else:
            return False

    def _find_digit(self, cell: ndarray) -> int:
        """Recognise digit on img."""
        cell_ = cv2.resize(cell, (28, 28))
        cell_ = cell_.astype("float") / 255.0
        cell_ = img_to_array(cell_)
        cell_ = expand_dims(cell_, axis=0)
        prediction = self.model.predict(cell_).argmax(axis=1)[0]

        return prediction

    def print_img(self) -> None:
        """Print original image."""
        cv2.imshow("original image", self.resize_img)
        cv2.waitKey(WAIT_TIME)

    def print_thresh_board(self) -> None:
        """Print treshold on image."""
        cv2.imshow("board after thresholding", self.image_thresh)
        cv2.waitKey(WAIT_TIME)

    def print_board_contours(self) -> None:
        """Print image with board contours marked."""
        board_on_img = self.resize_img
        cv2.drawContours(
            board_on_img,
            [self.board_contours],
            -1,
            (255, 255, 0),
            2,
        )
        cv2.imshow("Board contours", board_on_img)
        cv2.waitKey(WAIT_TIME)

    def print_board(self) -> None:
        """Print only board."""
        cv2.imshow("Board", self.board)
        cv2.waitKey(WAIT_TIME)

    def print_raw_cells(self) -> None:
        """Print cells one by one."""
        for cell_cords in self.cells_cords:
            cell = self.board[
                cell_cords[2] : cell_cords[3],  # noqa: E203
                cell_cords[0] : cell_cords[1],  # noqa: E203
            ]
            cv2.imshow("cells", cell)
            cv2.waitKey(WAIT_TIME)

    def print_improved_cells(self) -> None:
        """Print improved img of cells one by one."""
        for cell_cords in self.cells_cords:
            cell = self.board[
                cell_cords[2] : cell_cords[3],  # noqa: E203
                cell_cords[0] : cell_cords[1],  # noqa: E203
            ]
            improved_cell = self._cell_image_impovement(cell)
            LOGGER.info(self._cell_is_empty(improved_cell))
            cv2.imshow("cells", improved_cell)
            cv2.waitKey(WAIT_TIME)

    def print_digits(self) -> None:
        """Print img of cell and digit interpretation."""
        for cell_cords in self.cells_cords:
            cell = self.board[
                cell_cords[2] : cell_cords[3],  # noqa: E203
                cell_cords[0] : cell_cords[1],  # noqa: E203
            ]
            improved_cell = self._cell_image_impovement(cell)
            if not self._cell_is_empty(improved_cell):
                digit = self._find_digit(improved_cell)
                LOGGER.info(digit)
                cv2.imshow("cells", improved_cell)
                cv2.waitKey(WAIT_TIME)
