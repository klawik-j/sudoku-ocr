import logging
from pathlib import Path

import mock
import pytest
from numpy import array, zeros

from sudoku_ocr.board import Board

LOGGER = logging.getLogger(__name__)
CORRECT_OCR_PERCENT_THRESHOLD = 50
CNN_PATH = Path("sudoku_ocr/cnn.h5")
CORRECT_IMAGE_PATH = Path("tests/img/sudoku1.png")
INCORRECT_FILE_PATH = Path("incorrect/file/path")
INCORRECT_SUDOKU = array(
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
CORRECT_SOLVED_SUDOKU_1 = [
    [5, 6, 7, 1, 2, 4, 8, 3, 9],
    [8, 3, 2, 9, 7, 6, 4, 1, 5],
    [4, 9, 1, 3, 5, 8, 6, 2, 7],
    [1, 4, 9, 2, 8, 7, 3, 5, 6],
    [6, 5, 8, 4, 3, 9, 1, 7, 2],
    [7, 2, 3, 5, 6, 1, 9, 4, 8],
    [2, 1, 5, 8, 9, 3, 7, 6, 4],
    [9, 7, 4, 6, 1, 5, 2, 8, 3],
    [3, 8, 6, 7, 4, 2, 5, 9, 1],
]
CORRECT_OCR = {
    "1": array(
        [
            [0, 0, 7, 0, 0, 4, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 1, 5],
            [4, 0, 0, 3, 5, 8, 0, 0, 7],
            [1, 0, 0, 2, 0, 0, 3, 0, 6],
            [0, 5, 0, 0, 3, 0, 0, 7, 2],
            [0, 0, 3, 0, 0, 1, 0, 0, 8],
            [0, 0, 0, 8, 9, 3, 0, 0, 4],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 7, 0, 0, 5, 0, 1],
        ]
    ),
    "2": array(
        [
            [8, 5, 0, 0, 0, 0, 0, 0, 2],
            [1, 0, 4, 0, 7, 0, 0, 0, 3],
            [6, 0, 0, 3, 0, 0, 0, 0, 0],
            [2, 3, 0, 0, 5, 0, 8, 0, 1],
            [0, 8, 0, 0, 3, 0, 0, 2, 0],
            [4, 0, 1, 0, 9, 0, 0, 3, 6],
            [0, 0, 0, 0, 0, 2, 0, 0, 5],
            [3, 0, 0, 0, 6, 0, 2, 0, 9],
            [5, 0, 0, 0, 0, 0, 0, 4, 7],
        ]
    ),
    "3": array(
        [
            [0, 0, 0, 2, 3, 0, 0, 0, 0],
            [0, 6, 7, 0, 0, 0, 9, 2, 0],
            [0, 9, 0, 0, 0, 7, 0, 3, 0],
            [0, 0, 4, 0, 7, 0, 0, 0, 8],
            [6, 0, 0, 4, 0, 2, 0, 0, 1],
            [7, 0, 0, 0, 1, 0, 6, 0, 0],
            [0, 7, 0, 6, 0, 0, 0, 1, 0],
            [0, 1, 8, 0, 0, 0, 3, 7, 0],
            [0, 0, 0, 0, 5, 1, 0, 0, 0],
        ]
    ),
}
TEST_CASE = [
    pytest.param(
        {
            "board_img_path": Path("tests/img/sudoku1.png"),
            "correct_ocr": CORRECT_OCR["1"],
        },
        id="img:1",
    ),
    pytest.param(
        {
            "board_img_path": Path("tests/img/sudoku2.jpg"),
            "correct_ocr": CORRECT_OCR["2"],
        },
        id="img:2",
    ),
    pytest.param(
        {
            "board_img_path": Path("tests/img/sudoku3.jpg"),
            "correct_ocr": CORRECT_OCR["3"],
        },
        id="img:3",
    ),
]


class TestBoard:
    """Test Board class."""

    def setup(self) -> None:
        """Set up test env."""
        self.board = Board()

    @pytest.mark.parametrize("data", TEST_CASE)
    def test_ocr_sudoku(self, data) -> None:
        """Test ocr_sudoku method."""
        self.board.prepare_img(data["board_img_path"])
        self.board.ocr_sudoku()

        number_of_digits_in_sudoku: int = 0
        number_of_correct_ocr_digits: int = 0

        for y in range(0, 9):
            for x in range(0, 9):
                if data["correct_ocr"][y][x] != 0:
                    number_of_digits_in_sudoku += 1
                if not self.board.board_value[y][x] == data["correct_ocr"][y][x]:
                    LOGGER.warning(
                        f"({x}, {y}) is {self.board.board_value[y][x]} should be {data['correct_ocr'][y][x]}"  # noqa: E501
                    )
                elif data["correct_ocr"][y][x] != 0:
                    number_of_correct_ocr_digits += 1
        correct_ocr_percent: int = number_of_correct_ocr_digits * 100 // number_of_digits_in_sudoku
        LOGGER.info(f"Correct ocr percent is: {correct_ocr_percent}%")

        assert correct_ocr_percent >= CORRECT_OCR_PERCENT_THRESHOLD

    def test_prepare_img_non_existing_file(self) -> None:
        """Test prepare_img public method with existing file path."""
        with pytest.raises(OSError):
            self.board.prepare_img(INCORRECT_FILE_PATH)

    def test_prepare_img_existing_file(self) -> None:
        """Test prepare_img public method with non existing file path."""
        self.board.prepare_img(CORRECT_IMAGE_PATH)
        assert self.board.resize_img.shape[1] == 600

    def test_load_SNN_model_non_existing_file(self) -> None:
        """Test load_SNN_model public method with existing file path."""
        with pytest.raises(OSError):
            self.board.load_SNN_model(INCORRECT_FILE_PATH)

    def test_load_SNN_model_existing_file(self) -> None:
        """Test load_SNN_model public method with non existing file path."""
        self.board.load_SNN_model(CNN_PATH)
        assert self.board.model is not None

    def test_solve_correct_board_value(self) -> None:
        """Test solve public method for correct board value."""
        with mock.patch(
            "sudoku_ocr.board.Board.board_value", new_callable=mock.PropertyMock, return_value=CORRECT_OCR["1"]
        ):
            self.board.solve()
            assert self.board.solved_board == CORRECT_SOLVED_SUDOKU_1

    def test_solve_incorrect_board_value(self) -> None:
        """Test solve public methos for incorrect board value."""
        with mock.patch(
            "sudoku_ocr.board.Board.board_value", new_callable=mock.PropertyMock, return_value=INCORRECT_SUDOKU
        ):
            self.board.solve()
            assert (self.board.solved_board == zeros((9, 9), int)).tolist()
