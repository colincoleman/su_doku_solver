import logging
total_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


class Cell:
    def __init__(self, puzzle):
        self.possible_values = total_set
        self.impossible_values = set(())
        self.definite_value = "_"
        self.box_number = None
        self.column_number = None
        self.row_number = None
        self.puzzle = puzzle

    def set_definite(self, value):
        self.possible_values = {value}
        self.definite_value = value
        self.impossible_values = total_set.difference(value)
        logging.info("Unknowns: %s \n%s", self.puzzle.count_unknowns(), self.puzzle.create_visualisation())

    def analyse_cell(self, puzzle):
        for i in range(9):
            cell_in_same_row: Cell = puzzle.get_row(self.row_number).get_cell(i)
            if self != cell_in_same_row and cell_in_same_row.definite_value != '_':
                self.impossible_values.add(cell_in_same_row.definite_value)
            cell_in_same_column: Cell = puzzle.get_column(self.column_number).get_cell(i)
            if self != cell_in_same_column and cell_in_same_column.definite_value != '_':
                self.impossible_values.add(cell_in_same_column.definite_value)
            cell_in_same_box: Cell = puzzle.get_box(self.box_number).get_cell(i)
            if self != cell_in_same_box and cell_in_same_box.definite_value != '_':
                self.impossible_values.add(cell_in_same_box.definite_value)
            if self.definite_value == '_':
                self.possible_values = self.possible_values.difference(self.impossible_values)
            if len(self.possible_values) == 1:
                if self.definite_value != self.possible_values.copy().pop():
                    self.set_definite(self.possible_values.copy().pop())
