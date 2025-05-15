from SudokuBoard import SudokuBoard
import sys
from visual import update_board_display, display_board_gui


def recursive(position, open_positions, board: SudokuBoard):
    if position == len(open_positions):
        update_board_display(board, delay=0.5)
        return True

    if position < 0 or position >= len(open_positions):
        return False

    row, column = open_positions[position]
    current_pos = (row, column)

    update_board_display(board, current_pos)

    for value in range(1, 10):
        if not board.check_all(row, column, value):
            board.insert(row, column, value)
            update_board_display(board, current_pos, try_value=value)

            if recursive(position + 1, open_positions, board):
                return True

    board.insert(row, column, " ")
    update_board_display(board, current_pos, try_value="backtracking")
    return False


def backtracking(board: SudokuBoard):
    sys.setrecursionlimit(2000)
    open_positions = list(board.open_positions)

    if recursive(0, open_positions, board):
        display_board_gui(board, solution=True)
        return True
    return False