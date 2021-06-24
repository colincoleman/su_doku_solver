import group
import cell


class Puzzle:
    def __init__(self):
        self.cells = {}
        self.rows = {}
        self.columns = {}
        self.boxes = {}
        for i in range(9):
            self.rows[i] = group.Group()
            self.columns[i] = group.Group()
            self.boxes[i] = group.Group()

        for i in range(81):
            self.cells[i] = cell.Cell()
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
            if self.cells[this_cell].definite_value == '_':
                unknowns += 1
        return unknowns
