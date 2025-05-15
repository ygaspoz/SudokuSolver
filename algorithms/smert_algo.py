from SudokuBoard import SudokuBoard

class SmartAlgo:
    def __init__(self, board: SudokuBoard):
        self.board = board
        self.possibilities = []


    def process_possibilities(self):
        self.possibilities = []
        for i in range(self.board.dims):
            row_possibilities = []
            for j in range(self.board.dims):
                cell_possibilities = []
                for k in range(1, 10):
                    if self.board.get_value(i, j) == " ":
                        if not self.board.check_all(i, j, k):
                            cell_possibilities.append(k)
                row_possibilities.append(cell_possibilities)
            self.possibilities.append(row_possibilities)

    def unique_values_per_cell(self):
        cell_size = self.board.cell_size
        dims = self.board.dims
        cell_uniques = {}
        for cell_row in range(0, dims, cell_size):
            for cell_col in range(0, dims, cell_size):
                value_positions = []
                value_count = {}
                for i in range(cell_row, cell_row + cell_size):
                    for j in range(cell_col, cell_col + cell_size):
                        for val in self.possibilities[i][j]:
                            value_positions.append((val, (i, j)))
                            value_count[val] = value_count.get(val, 0) + 1
                uniques = set((val, pos) for val, pos in value_positions if value_count[val] == 1)
                cell_uniques[(cell_row // cell_size, cell_col // cell_size)] = uniques
        return cell_uniques


    def process_cell_possibilities(self):
        cell_uniques = self.unique_values_per_cell()
        for _, value in cell_uniques.items():
            for i in value:
                if i:
                    self.board.insert(i[1][0], i[1][1], i[0])
                    self.board.decrease_open_positions()


    def process_singles(self):
        for i in range(self.board.dims):
            for j in range(self.board.dims):
                if len(self.possibilities[i][j]) == 1:
                    self.board.insert(i, j, self.possibilities[i][j][0])
                    self.board.decrease_open_positions()


    def run_algo(self):
        changed = []
        while len(changed) < 3:
            old_open = self.board.get_open_positions_num()
            self.process_possibilities()
            self.process_cell_possibilities()
            self.process_singles()
            if self.board.get_open_positions_num() == old_open:
                changed.append(False)
            else:
                changed = []
            print(self.board.get_open_positions_num())
