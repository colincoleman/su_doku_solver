from src.sudoku.puzzle import Puzzle


def test_puzzle_structure():
    this_puzzle = Puzzle()
    assert this_puzzle.get_cell(21) == this_puzzle.get_row(2).get_cell(3)
    assert this_puzzle.cells[21] == this_puzzle.columns[3].cells[2]
    assert this_puzzle.cells[21] != this_puzzle.rows[0].cells[0]
    assert this_puzzle.cells[0] != this_puzzle.columns[3].cells[2]


def test_count_unknowns():
    this_puzzle = Puzzle()
    assert Puzzle.count_unknowns(this_puzzle) == 81
