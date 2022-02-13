# from board import Board


# if __name__ == "__main__":
#     img_path = "/home/kuba/Desktop/sudoku-ocr/code/img/sudoku4.jpg"
#     board = Board()
#     # board.prepare_img(img_path)
#     # board.load_SNN_model("WideResNet")
#     # board.ocr_sudoku()
#     # print(board.board_value)
#     board.board_value = [
#         [0, 0, 0, 2, 3, 0, 0, 0, 0],
#         [0, 6, 7, 0, 0, 0, 9, 2, 0],
#         [0, 9, 0, 0, 0, 7, 0, 3, 0],
#         [0, 0, 4, 0, 7, 0, 0, 0, 8],
#         [6, 0, 0, 4, 0, 2, 0, 0, 1],
#         [7, 0, 0, 0, 1, 0, 6, 0, 0],
#         [0, 7, 0, 6, 0, 0, 0, 1, 0],
#         [0, 1, 8, 0, 0, 0, 3, 7, 0],
#         [0, 0, 0, 0, 5, 1, 0, 0, 0],
#     ]
#     print(board.board_value)
#     board.solve()
#     print(board.solved_board)
