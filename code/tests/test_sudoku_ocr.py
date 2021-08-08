import pytest
from ocr import Board
from numpy import array

IMG_PATHS = {
    "1": "/home/kuba/Desktop/sudoku-ocr/code/img/sudoku1.jpg",
    "2": "/home/kuba/Desktop/sudoku-ocr/code/img/sudoku2.jpg",
    "3": "/home/kuba/Desktop/sudoku-ocr/code/img/sudoku3.jpg",
    "4": "/home/kuba/Desktop/sudoku-ocr/code/img/sudoku4.jpg",
}

BOARDS_SOLUTIONS = {
    "1": array(
        [
            [8, 0, 0, 0, 1, 0, 0, 0, 9],
            [0, 5, 0, 8, 0, 7, 0, 1, 0],
            [0, 0, 4, 0, 9, 0, 7, 0, 0],
            [0, 6, 0, 7, 0, 1, 0, 2, 0],
            [5, 0, 8, 0, 6, 0, 1, 0, 7],
            [0, 1, 0, 5, 0, 2, 0, 9, 0],
            [0, 0, 7, 0, 4, 0, 6, 0, 0],
            [0, 8, 0, 3, 0, 9, 0, 4, 0],
            [3, 0, 0, 0, 5, 0, 0, 0, 8],
        ]
    ),
    "2": array(
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
    "3": array(
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
    "4": array(
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
    pytest.param({"board_img": "1", "SNN_model": "kuba"}, id="img:1, cnn:kuba"),
    pytest.param({"board_img": "1", "SNN_model": "WideResNet"}, id="img:1, cnn:WideResNet"),
    # pytest.param({"board_img": "1", "SNN_model": "ResNet164"}, id="img:1, cnn:ResNet164"),
    # pytest.param({"board_img": "1", "SNN_model": "MobileNet"}, id="img:1, cnn:MobileNet"),
    # pytest.param({"board_img": "1", "SNN_model": "VGG16"}, id="img:1, cnn:VGG16"),
    pytest.param({"board_img": "2", "SNN_model": "kuba"}, id="img:2, cnn:kuba"),
    pytest.param({"board_img": "2", "SNN_model": "WideResNet"}, id="img:2, cnn:WideResNet"),
    # pytest.param({"board_img": "2", "SNN_model": "ResNet164"}, id="img:2, cnn:ResNet164"),
    # pytest.param({"board_img": "2", "SNN_model": "MobileNet"}, id="img:2, cnn:MobileNet"),
    # pytest.param({"board_img": "2", "SNN_model": "VGG16"}, id="img:2, cnn:VGG16"),
    pytest.param({"board_img": "3", "SNN_model": "kuba"}, id="img:3, cnn:kuba"),
    pytest.param({"board_img": "3", "SNN_model": "WideResNet"}, id="img:3, cnn:WideResNet"),
    # pytest.param({"board_img": "3", "SNN_model": "ResNet164"}, id="img:3, cnn:ResNet164"),
    # pytest.param({"board_img": "3", "SNN_model": "MobileNet"}, id="img:3, cnn:MobileNet"),
    # pytest.param({"board_img": "3", "SNN_model": "VGG16"}, id="img:3, cnn:VGG16"),
    pytest.param({"board_img": "4", "SNN_model": "kuba"}, id="img:4, cnn:kuba"),
    pytest.param({"board_img": "4", "SNN_model": "WideResNet"}, id="img:4, cnn:WideResNet"),
    # pytest.param({"board_img": "4", "SNN_model": "ResNet164"}, id="img:4, cnn:ResNet164"),
    # pytest.param({"board_img": "4", "SNN_model": "MobileNet"}, id="img:4, cnn:MobileNet"),
    # pytest.param({"board_img": "4", "SNN_model": "VGG16"}, id="img:4, cnn:VGG16"),
]


class TestBoard:
    """Test Board class."""

    def setup(self) -> None:
        """Set up test env."""
        self.board = Board()

    @pytest.mark.parametrize("data", TEST_CASE)
    def test_ocr_sudoku(self, data) -> None:
        """Test ocr_sudoku method."""
        self.board.prepare_img(IMG_PATHS[data["board_img"]])
        self.board.load_SNN_model(data["SNN_model"])
        self.board.ocr_sudoku()
        err_msg = []

        for y in range(0, 9):
            for x in range(0, 9):
                if not self.board.board_value[y][x] == BOARDS_SOLUTIONS[data["board_img"]][y][x]:
                    err_msg.append(
                        f"({x}, {y}) is {self.board.board_value[y][x]} sholud be {BOARDS_SOLUTIONS[data['board_img']][y][x]}"  # noqa: E501
                    )

        print("### result ###")
        print(self.board.board_value)
        print("### correct ###")
        print(BOARDS_SOLUTIONS[data["board_img"]])
        for err in err_msg:
            print(err)

        comparision = self.board.board_value == BOARDS_SOLUTIONS[data["board_img"]]
        assert comparision.all()
