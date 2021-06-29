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
    logging.info(create_visualisation(this_puzzle))
    previous_unknowns = 81
    current_unknowns = this_puzzle.count_unknowns()
    logging.info(current_unknowns)
    while 0 < current_unknowns != previous_unknowns:
        previous_unknowns = current_unknowns

        for cell in range(81):
            this_puzzle.cells[cell].analyse_cell(this_puzzle)
        logging.info(create_visualisation(this_puzzle))
        current_unknowns = this_puzzle.count_unknowns()
        logging.info(current_unknowns)

        for group in range(9):
            this_puzzle.boxes[group].analyse_group()
            this_puzzle.boxes[group].find_pairs()
            this_puzzle.rows[group].analyse_group()
            this_puzzle.rows[group].find_pairs()
            this_puzzle.columns[group].analyse_group()
            this_puzzle.columns[group].find_pairs()
        current_unknowns = this_puzzle.count_unknowns()
    print(create_visualisation(this_puzzle))


def format_row(this_row):
    output = ['']
    for i in this_row.cells:
        if i % 3 == 0:
            output.append('|')
        next_value = this_row.cells[i].definite_value
        if next_value == '_':
            output.append(' ')
        else:
            output.append(next_value)
    output.append('|')
    return ''.join(output)


def create_visualisation(this_puzzle):
    builder = []
    first_and_last = '.-----------.\n'
    mid_grid = '|---+---+---|\n'
    builder.append(first_and_last)
    for row in range(9):
        if row % 3 == 0 and row != 0:
            builder.append(mid_grid)
        builder.append(format_row(this_puzzle.rows[row]))
        builder.append('\n')
    builder.append(first_and_last)
    return ''.join(builder)


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
    logging.basicConfig(level=logging.INFO,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
if __name__ == '__main__':
    run()
