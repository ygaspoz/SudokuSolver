from SudokuBoard import *
def dummy_algo(board: SudokuBoard):
    board.print_board()
    iteration = 0
    changed = True
    while changed:
        old_o_p = board.get_open_positions_num()
        for i in range(board.get_dims()):
            for j in range(board.get_dims()):
                candidates = []
                for k in range(1, 10):
                    if board.get_value(i, j) == " ":
                        if board.check_cell(i, j, k) or board.check_row(i, k) or board.check_column(j, k):
                            continue
                        candidates.append(k)
                if len(candidates) == 1:
                    board.insert(i, j, candidates[0])
                    board.decrease_open_positions()
        if old_o_p == board.get_open_positions_num():
            changed = False
        board.print_board()
        iteration += 1
        print(f"Current Iteration: {iteration}")
        print("-" * 50)
        print()