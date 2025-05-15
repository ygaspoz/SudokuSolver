import argparse
from helper import *

def main():
    parser = argparse.ArgumentParser(description='Sudoku solver')
    parser.add_argument(
        "-l", "--list", action="store_true", help="show how many Sudoku are available"
    )
    parser.add_argument(
        "-p", "--print", type=int, metavar="number", help="print the specified Sudoku by its number"
    )
    parser.add_argument(
        "-s", "--solve", type=int, metavar="number", help="solve the sudoku by its number"
    )
    args = parser.parse_args()
    if args.list:
        print("Listing available Sudoku puzzles...")
        print(available_sudoku())
        return
    if args.print is not None:
        print(f"Printing Sudoku number {args.print}")
        print_sudoku(args.print)
        return
    if args.solve is not None:
        print(f"Solving Sudoku number {args.solve}")
        solve_sudoku(args.solve)
        return

if __name__ == "__main__":
    main()