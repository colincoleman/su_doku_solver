from src.sudoku.puzzle import Puzzle
from src.sudoku.sudoku import init_puzzle


def test_analyse_cell():
    this_puzzle = Puzzle()
    init_puzzle(this_puzzle)
    this_cell = this_puzzle.cells[40]
    assert this_cell.definite_value == '_'
    this_cell.analyse_cell(this_puzzle)
    assert this_cell.definite_value == '9'
