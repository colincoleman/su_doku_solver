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
            self.cells[i] = Cell(self)
            this_col_no = i % 9
            this_row_no = i // 9
            this_box_no = this_col_no // 3 + (this_row_no // 3) * 3
            self.get_cell(i).column_number = this_col_no
            self.get_cell(i).row_number = this_row_no
            self.get_cell(i).box_number = this_box_no
            self.get_row(this_row_no).cells[this_col_no] = self.get_cell(i)
            self.get_column(this_col_no).cells[this_row_no] = self.get_cell(i)
            self.get_box(this_box_no).cells[this_col_no % 3 + (this_row_no % 3) * 3] = self.get_cell(i)

    def get_row(self, index: int) -> Group:
        return self.rows[index]

    def get_column(self, index: int) -> Group:
        return self.columns[index]

    def get_box(self, index: int) -> Group:
        return self.boxes[index]

    def get_cell(self, index: int) -> Cell:
        return self.cells[index]

    def count_unknowns(self):
        unknowns = 0
        for this_cell in self.cells:
            if self.cells[this_cell].definite_value == '_' or self.cells[this_cell].definite_value is None:
                unknowns += 1
        return unknowns

    def create_visualisation(self):
        builder = []
        first_and_last = '.-----------.\n'
        mid_grid = '|---+---+---|\n'
        builder.append(first_and_last)
        for row in range(9):
            if row % 3 == 0 and row != 0:
                builder.append(mid_grid)
            builder.append(self.format_row(row))
            builder.append('\n')
        builder.append(first_and_last)
        return ''.join(builder)

    def format_row(self, row_number: int):
        output = ['']
        this_row = self.get_row(row_number)
        for i in this_row.cells:
            if i % 3 == 0:
                output.append('|')
            next_value = this_row.get_cell(i).definite_value
            if next_value == '_':
                output.append(' ')
            else:
                output.append(next_value)
        output.append('|')
        return ''.join(output)
