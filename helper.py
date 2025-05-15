from SudokuBoard import SudokuBoard
from backtracking import backtracking
import time
import ast


def load_sudoku_from_file(sudoku_number: int):
    with open('sudoku.txt', 'r') as f:
        sudoku = f.readlines()
        line = sudoku[sudoku_number - 1].strip()
        board = ast.literal_eval(line)
    return SudokuBoard(board, 9)


def available_sudoku():
    with open('sudoku.txt', 'r') as f:
        return len(f.readlines())


def print_sudoku(sudoku_number: int):
    load_sudoku_from_file(sudoku_number).print_board()


def solve_sudoku(sudoku_number: int):
    board = load_sudoku_from_file(sudoku_number)
    start_time = time.time()
    backtracking(board)
    end_time = time.time()
    print()
    print('Sudoku solver took {} seconds'.format(end_time - start_time))
