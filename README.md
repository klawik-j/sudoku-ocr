# Sudoku Ocr
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

## About
sudoku-ocr is a package that deliver class and methods to ocr sudoku image

## Getting started
### Installation
```
pip install sudoku-ocr
```

### Usage example
```python
from sudoku_ocr import Board

board = Board()
board.prepare_img("/path/to/sudoku/image")
board.ocr_sudoku()
print(board.board_value)
#  [[0 0 7 0 0 4 0 0 9]
#  [0 0 0 0 0 0 0 1 5]
#  [4 0 0 3 5 8 0 0 7]
#  [1 0 0 2 0 0 3 0 6]
#  [0 5 0 0 3 0 0 7 2]
#  [0 0 3 0 0 1 0 0 8]
#  [0 0 0 8 9 3 0 0 4]
#  [0 7 0 0 0 0 0 0 3]
#  [3 0 0 7 0 0 5 0 1]]

board.solve()
print(board.solved_board)
#  [[5 6 7 1 2 4 8 3 9]
#  [8 3 2 9 7 6 4 1 5]
#  [4 9 1 3 5 8 6 2 7]
#  [1 4 9 2 8 7 3 5 6]
#  [6 5 8 4 3 9 1 7 2]
#  [7 2 3 5 6 1 9 4 8]
#  [2 1 5 8 9 3 7 6 4]
#  [9 7 4 6 1 5 2 8 3]
#  [3 8 6 7 4 2 5 9 1]]

```
User have access to public properties:
* `board_value` - sudoku image representation as 2D array
* `solved_board` - solved board_value. In case board_value is invalid, solved_board will be 2D array filled with 0.

### Usage without ocr
In case user just wants to solve sudoku, without need to ocr it first or ocr is incorrect.
It is possible to set `board_value` as 2D array directly and than call solve() e.g.
```python
board = Board()
board.board_value = [
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
board.solve()
print(board.solved_board)
#  [[5 6 7 1 2 4 8 3 9]
#  [8 3 2 9 7 6 4 1 5]
#  [4 9 1 3 5 8 6 2 7]
#  [1 4 9 2 8 7 3 5 6]
#  [6 5 8 4 3 9 1 7 2]
#  [7 2 3 5 6 1 9 4 8]
#  [2 1 5 8 9 3 7 6 4]
#  [9 7 4 6 1 5 2 8 3]
#  [3 8 6 7 4 2 5 9 1]]
```

