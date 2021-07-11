from typing import List

from imutils.perspective import four_point_transform
from imutils import grab_contours, resize
from skimage.segmentation import clear_border
from numpy import ndarray
import cv2

WAIT_TIME = 1000


class Board:
    """Class of a sudoku board"""

    def __init__(self, img_path):
        self._img_path = img_path
        self.original_img = self.load_img(self._img_path)
        self.board_thresh = self.thresholding(self.original_img)
        self.board_contours = self.find_board_contour(
            self.find_contours(self.board_thresh),
        )
        self.board = self.adjust_perspective(
            self.original_img,
            self.board_contours,
        )
        self.cells_cords = self.find_cells(self.board)

    @staticmethod
    def load_img(img_path: str) -> ndarray:
        """Loads image

        Args:
            img_path (str): path to file

        Raises:
            OSError: file no found

        Returns:
            ndarray: image
        """
        image = cv2.imread(img_path)
        if image is None:
            raise OSError(f"file {img_path} not found")
        return image

    @staticmethod
    def thresholding(img: ndarray) -> ndarray:
        """Function apply thresholding on image

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
    def find_contours(img: ndarray) -> ndarray:
        """Finds contours

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
    def find_board_contour(contours: ndarray) -> ndarray:
        """Looks for contours of sudoku board

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
    def adjust_perspective(img: ndarray, board_contours: ndarray) -> ndarray:
        """Adjust perspective
        Use four point transformation

        Args:
            img (ndarray): image
            board_contours (ndarray): contours fo board

        Returns:
            ndarray: image of board and nothing else
        """
        board = four_point_transform(
            cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), board_contours.reshape(4, 2)
        )
        return board

    @staticmethod
    def find_cells(board: ndarray) -> List:
        """Looks for cells coordinates

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

    def print_img(self):
        """Prints original image"""
        cv2.imshow("original image", self.original_img)
        cv2.waitKey(WAIT_TIME)

    def print_thresh_board(self):
        """Prints treshold on image"""
        cv2.imshow("board after thresholding", self.board_thresh)
        cv2.waitKey(WAIT_TIME)

    def print_board_contours(self):
        """Prints image with board contours marked"""
        board_on_img = self.original_img
        cv2.drawContours(
            board_on_img,
            [self.board_contours],
            -1,
            (255, 255, 0),
            2,
        )
        cv2.imshow("Board contours", board_on_img)
        cv2.waitKey(WAIT_TIME)

    def print_board(self):
        """Prints only board"""
        cv2.imshow("Board", self.board)
        cv2.waitKey(WAIT_TIME)

    def print_cells(self):
        """Print cells one by one"""
        for cell in self.cells_cords:
            cv2.imshow(
                "cells",
                self.board[
                    cell[2] : cell[3],
                    cell[0] : cell[1],
                ],
            )
            cv2.waitKey(WAIT_TIME)


if __name__ == "__main__":
    img_path = "./img/sudoku1.jpg"
    board = Board(img_path)
    # print("original")
    # board.print_board()
    # print("thresh")
    # board.print_thresh_board()
    # print("contours")
    # board.print_board_contours()
    # print("board")
    # board.print_board()
    print("cells")
    board.print_cells()
