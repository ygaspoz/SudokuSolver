import math

class SudokuBoard:
    """
    Class that defines the Sudoku board and all the available functions to use it
    """
    def __init__(self, table, dims):
        assert (math.sqrt(dims) % 1 == 0)
        self.table = table
        self.dims = dims
        self.cell_size = int(math.sqrt(dims))
        self.fixed_positions = set(
            (i, j)
            for i, row in enumerate(table)
            for j, val in enumerate(row)
            if val != " "
        )
        self.open_positions_num = self.dims ** 2 - len(self.fixed_positions)
        self.open_positions = sorted(
            (i, j)
            for i, row in enumerate(table)
            for j, val in enumerate(row)
            if val == " "
        )

    def insert(self, row, column, value):
        """
        Function to insert a value in the given spot
        :param row: the row in which the value is inserted
        :param column: the column in which the value is inserted
        :param value: the value to insert
        :return: nothing
        """
        self.table[row][column] = value


    def get_value(self, row, column):
        """
        Function that gets the value from the board
        :param row: row of the value
        :param column: column of the value
        :return: value
        """
        return self.table[row][column]


    def check_row(self, row, value):
        """
        Function to check if a value is in a given row
        :param row: the row to test
        :param value: the value to search for
        :return: True if the value is in the row, false if not
        """
        if value in self.table[row]:
            return True
        return False


    def decrease_open_positions(self):
        """
        decreases open_positions by 1
        :return: nothing
        """
        self.open_positions_num -= 1


    def increment_open_positions(self):
        """
        increases open_positions by 1
        :return: nothing
        """
        self.open_positions_num += 1


    def get_open_positions_num(self):
        """
        Function to return remaining open positions
        :return: the remaining open positions
        """
        return self.open_positions_num


    def check_column(self, column, value):
        """
        Function to check if a value is in a given column
        :param column: the column to test
        :param value: the value to search for
        :return: True if the value is in the column, false if not
        """
        for i in self.table:
            if value == i[column]:
                return True
        return False


    def check_cell(self, row, column, value):
        """
        Function to check if a value is in a given cell
        :param row: the row
        :param column: the column
        :param value: The value to search for
        :return: True if the value is in the cell, false if not
        """
        start_row = (row // self.cell_size) * self.cell_size
        start_col = (column // self.cell_size) * self.cell_size
        for i in range(start_row, start_row + self.cell_size):
            for j in range(start_col, start_col + self.cell_size):
                if self.table[i][j] == value:
                    return True
        return False


    def check_all(self, row, column, value = None):
        """
        Function to check all the checks
        :param row: the row to check
        :param column: the column to check
        :param value: the value to check
        :return: True if value is in one of them, false if not
        """
        if value is None:
            value = self.get_value(row, column)
        return self.check_row(row, value) or self.check_column(column, value) or self.check_cell(row, column, value)


    def get_dims(self):
        """
        get the dimension
        :return: dimension
        """
        return self.dims



    def print_board(self):
        """
        Function to print the board
        :return: nothing
        """
        BLUE = "\033[94m"
        RESET = "\033[0m"
        print((self.dims + self.cell_size + 1) * '-')
        for row in range(self.dims):
            print("|", end="")
            for column in range(self.dims):
                val = self.table[row][column]
                if (row, column) in self.fixed_positions and val != " ":
                    print(f"{BLUE}{val}{RESET}", end="")
                else:
                    print(val, end="")
                if (column + 1) % self.cell_size == 0:
                    print("|", end="")
            print()
            if (row + 1) % self.cell_size == 0:
                print((self.dims + self.cell_size + 1) * '-')

