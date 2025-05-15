from SudokuBoard import SudokuBoard
import sys

def recursive(position, open_positions, board: SudokuBoard):
    if position == len(open_positions):
        board.print_board()
        return True

    if position < 0 or position >= len(open_positions):
        return False

    row, column = open_positions[position]
    current_pos = (row, column)


    for value in range(1, 10):
        if not board.check_all(row, column, value):
            board.insert(row, column, value)

            if recursive(position + 1, open_positions, board):
                return True

    board.insert(row, column, " ")
    return False


def backtracking(board: SudokuBoard):
    sys.setrecursionlimit(2000)
    open_positions = list(board.open_positions)

    if recursive(0, open_positions, board):
        return True
    return False