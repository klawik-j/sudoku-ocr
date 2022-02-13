from pathlib import Path
import logging

import pytest
from numpy import array

from sudoku_ocr.board import Board

LOGGER = logging.getLogger(__name__)

CNN_PATH = Path("sudoku_ocr/cnn.h5")

CORRECT_OCR = {
    "1": array(
        [
            [0, 0, 0, 6, 0, 4, 7, 0, 0],
            [7, 0, 6, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 5, 0, 8, 0],
            [0, 7, 0, 0, 2, 0, 0, 9, 3],
            [8, 0, 0, 0, 0, 0, 0, 0, 5],
            [4, 3, 0, 0, 1, 0, 0, 7, 0],
            [0, 5, 0, 2, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 2, 0, 8],
            [0, 0, 2, 3, 0, 1, 0, 0, 0],
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
    pytest.param({
        "board_img_path": Path("tests/img/sudoku1.jpg"),
        "correct_ocr": CORRECT_OCR["1"],
        },
        id="img:1"),
    pytest.param({
        "board_img_path": Path("tests/img/sudoku2.jpg"),
        "correct_ocr": CORRECT_OCR["2"],
        },
        id="img:2"),
    pytest.param({
        "board_img_path": Path("tests/img/sudoku3.jpg"),
        "correct_ocr": CORRECT_OCR["3"],
        },
        id="img:3"),
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
        self.board.load_SNN_model(CNN_PATH)
        self.board.ocr_sudoku()

        for y in range(0, 9):
            for x in range(0, 9):
                if not self.board.board_value[y][x] == data["correct_ocr"][y][x]:
                    LOGGER.error(
                        f"({x}, {y}) is {self.board.board_value[y][x]} should be {data['correct_ocr'][y][x]}"  # noqa: E501
                    )
        comparision = self.board.board_value == data["correct_ocr"]
        assert comparision.all()
