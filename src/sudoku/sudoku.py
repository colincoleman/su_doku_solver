#!/usr/bin/env python3

"""Usage: sudoku.py [INPUT] [--log]

Solve a Su Doku puzzle
Arguments:
  INPUT     filename of Su Doku puzzle to solve (default ./example_puzzle.txt)
Options:
  -h --help     Show this screen
  --log         Record working to log file
"""

from docopt import docopt
import logging

from src.sudoku.puzzle import Puzzle


def run():
    this_puzzle = Puzzle()
    init_puzzle(this_puzzle)
    previous_unknowns = 81
    current_unknowns = this_puzzle.count_unknowns()
    logging.info("Unknowns: %s \n%s", this_puzzle.count_unknowns(), this_puzzle.create_visualisation())
    while 0 < current_unknowns != previous_unknowns:
        previous_unknowns = current_unknowns

        for cell in range(81):
            this_cell = this_puzzle.get_cell(cell)
            if this_cell.definite_value is None or this_cell.definite_value == '_':
                this_cell.analyse_cell(this_puzzle)

        for group in range(9):
            this_box = this_puzzle.get_box(group)
            this_box.analyse_group()
            this_box.find_pairs()

            this_column = this_puzzle.get_column(group)
            this_column.analyse_group()
            this_column.find_pairs()

            this_row = this_puzzle.get_row(group)
            this_row.analyse_group()
            this_row.find_pairs()

        current_unknowns = this_puzzle.count_unknowns()
    print(this_puzzle.create_visualisation())


def init_puzzle(this_puzzle):
    puzzle_data = parse_input_file(input_file)
    for count in range(81):
        this_puzzle.cells[count].definite_value = puzzle_data[count]


def parse_input(puzzle_input_list):
    puzzle_array = []
    for line in puzzle_input_list:
        puzzle_array += (list(line))
    return puzzle_array


def parse_input_file(file_name):
    with open(file_name) as f:
        file_content = f.read().splitlines()
    return parse_input(file_content)


arguments = docopt(__doc__)
if arguments['INPUT']:
    input_file = arguments['INPUT']
else:
    input_file = './example_puzzle.txt'
if arguments['--log']:
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
if __name__ == '__main__':
    run()
