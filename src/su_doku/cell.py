class Cell:
    def __init__(self):
        self.possible_values = set(())
        self.impossible_values = set(())
        self.definite_value = None
        self.box_number = None
        self.column_number = None
        self.row_number = None

    def analyse_cell(self, puzzle):
        total_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        if self.definite_value != "_":
            self.possible_values = {self.definite_value}
            self.impossible_values = total_set.difference(self.definite_value)
        else:
            for i in range(9):
                space_in_same_row = puzzle.rows[self.row_number].cells[i]
                if self != space_in_same_row and space_in_same_row.definite_value != '_':
                    self.impossible_values.add(space_in_same_row.definite_value)
                space_in_same_column = puzzle.columns[self.column_number].cells[i]
                if self != space_in_same_column and space_in_same_column.definite_value != '_':
                    self.impossible_values.add(space_in_same_column.definite_value)
                space_in_same_box = puzzle.boxes[self.box_number].cells[i]
                if self != space_in_same_box and space_in_same_box.definite_value != '_':
                    self.impossible_values.add(space_in_same_box.definite_value)
                if self.definite_value == '_':
                    self.possible_values = total_set.difference(self.impossible_values)
                else:
                    self.possible_values = {self.definite_value}
                if len(self.possible_values) == 1:
                    self.definite_value = self.possible_values.copy().pop()
