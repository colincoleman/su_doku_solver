from src.sudoku.cell import Cell
from src.sudoku.group import Group


class Puzzle:
    def __init__(self):
        self.cells = {}
        self.rows = {}
        self.columns = {}
        self.boxes = {}
        for i in range(9):
            self.rows[i] = Group()
            self.columns[i] = Group()
            self.boxes[i] = Group()

        for i in range(81):
            self.cells[i] = Cell()
            this_col_no = i % 9
            this_row_no = i // 9
            this_box_no = this_col_no // 3 + (this_row_no // 3) * 3
            self.cells[i].column_number = this_col_no
            self.cells[i].row_number = this_row_no
            self.cells[i].box_number = this_box_no
            self.rows[this_row_no].cells[this_col_no] = self.cells[i]
            self.columns[this_col_no].cells[this_row_no] = self.cells[i]
            self.boxes[this_box_no].cells[this_col_no % 3 + (this_row_no % 3) * 3] = self.cells[i]

    def count_unknowns(self):
        unknowns = 0
        for this_cell in self.cells:
            if self.cells[this_cell].definite_value == '_' or self.cells[this_cell].definite_value is None:
                unknowns += 1
        return unknowns
