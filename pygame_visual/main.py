from SudokuBoard import SudokuBoard
from smert_algo import SmartAlgo
from dummy_algo import dummy_algo
from backtracking import backtracking
from visual import display_interactive_board, initialize_gui

table_easy = [
    [" ", " ", 1, " ", " ", 4, " ", " ", 2],
    [" ", 5, " ", " ", " ", 3, " ", 1, 9],
    [4, 7, " ", " ", " ", " ", " ", " ", 5],
    [" ", " ", " ", " ", 8, " ", 2, " ", 7],
    [" ", " ", 4, " ", 9, " ", 8, " ", " "],
    [8, " ", 6, " ", 3, " ", " ", " ", " "],
    [2, " ", " ", " ", " ", " ", " ", 6, 8],
    [1, 8, " ", 2, " ", " ", " ", 4, " "],
    [5, " ", " ", 3, " ", " ", 9, " ", " "]
]

table_hard = [
    [4, 9, " ", 6, " ", " ", " ", " ", 1],
    [" ", " ", 8, " ", " ", 9, " ", " ", " "],
    [" ", " ", " ", " ", 8, " ", " ", " ", " "],
    [" ", 5, " ", 2, 1, 8, " ", " ", " "],
    [" ", " ", 1, " ", 6, " ", 8, " ", " "],
    [2, " ", " ", " ", " ", 7, " ", 6, " "],
    [5, " ", 6, 3, " ", " ", " ", 1, 8],
    [" ", 2, " ", 4, " ", " ", 5, " ", " "],
    [" ", 3, " ", " ", " ", " ", " ", " ", 2]
]

board = SudokuBoard(table_hard, 9)
display_interactive_board(board, backtracking)