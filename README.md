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
board.solve()
```
User have access to public properties:
* `board_value` - sudoku image representation as 2D array
* `solved_board` - solved board_value. In case board_value is invalid, solved_board will be 2D array filled with 0.

### Usage without ocr
It is possible to set `board_value` as 2D array directly and than call
```
board.solve()
```
In case user just want to solve sudoku, without need to ocr it first.

