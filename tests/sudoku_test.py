from src.sudoku.puzzle import Puzzle
from src.sudoku.sudoku import init_puzzle, parse_input_file

input_file = './example_puzzle.txt'


def test_init_puzzle():
    this_puzzle = Puzzle()
    assert this_puzzle.cells[0].definite_value == "_"
    init_puzzle(this_puzzle)
    assert this_puzzle.cells[0].definite_value == '4'


def test_parse_input_file():
    file_content = parse_input_file(input_file)
    assert file_content[1] == '1'
