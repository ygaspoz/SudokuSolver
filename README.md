# Sudoku Solver

A Python project to solve Sudoku puzzles using the backtracking algorithm. Includes a command-line interface (CLI) and optional Pygame visualization.

## Algorithm

The solver uses the **backtracking** algorithm:
- It searches for empty cells and tries all possible numbers (1-9).
- For each number, it checks if the placement is valid (row, column, and 3x3 box).
- If valid, it fills the cell and recursively solves the rest of the board.
- If stuck, it backtracks and tries the next number.
- Continues until the board is solved or no solution exists.

## Usage

### Requirements

- Python 3.x
- (Optional) Pygame for visualization

### Command-Line Interface

Run the CLI tool to interact with Sudoku puzzles stored in `sudoku.txt`.

#### Available Commands

- `-l`, `--list`  
  Show how many Sudoku puzzles are available in `sudoku.txt`.

- `-p N`, `--print N`  
  Print the N-th Sudoku puzzle.

- `-s N`, `--solve N`  
  Solve the N-th Sudoku puzzle and display the time taken.

#### Example Usage

```sh
python cli.py --list
python cli.py --print 2
python cli.py --solve 3
```

### File Format

Each line in `sudoku.txt` should be a Python list representing a 9x9 Sudoku board, e.g.:
```python
[' ', 7, ' ', 4, ' ', ' ', ' ', 1, ' '], [5, ' ', ...]
```

## Visualization

To run the Pygame visualizer, use:
```sh
python pygame_visual/main.py
```

## Project Structure

- `main.py` — Run the solver on a hardcoded board.
- `helper.py` — CLI for loading, printing, and solving puzzles from file.
- `pygame_visual/main.py` — Visual interface using Pygame.
- `SudokuBoard.py` — Board representation and utilities.
- `algorithms/backtracking.py` — Backtracking algorithm.

## License

MIT License
