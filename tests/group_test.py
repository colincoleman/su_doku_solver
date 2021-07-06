from src.sudoku.cell import Cell
from src.sudoku.group import Group


def test_analyse_group():
    this_group = Group()
    for i in range(9):
        this_group.cells[i] = Cell({})
        this_group.cells[i].definite_value = str(i)
    this_group.cells[3].definte_value = '_'
    this_group.analyse_group()
    assert this_group.cells[3].definite_value == '3'
    for i in range(9):
        this_group.cells[i] = Cell({})
        this_group.cells[i].definite_value = str(i)
    this_group.cells[3].definte_value = '_'
    this_group.cells[4].definte_value = '_'
    this_group.analyse_group()
    this_group.cells[3].definte_value == '_'





