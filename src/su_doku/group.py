class Group:
    def __init__(self):
        self.cells = {}

    def analyse_group(self):
        total_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        all_possibles = []
        for cell in self.cells:
            all_possibles.append(list(self.cells[cell].possible_values))
        for i in range(9):
            number = i + 1
            times_found = 0
            index_found = None
            for j in range(9):
                if str(number) in all_possibles[j]:
                    times_found += 1
                    index_found = j
            if times_found == 1:
                cell_index = index_found
                self.cells[cell_index].definite_value = str(number)
                self.cells[cell_index].possible_values = {str(number)}
                self.cells[cell_index].impossible_values = total_set.difference(self.cells[cell_index].possible_values)

    def find_pairs(self):
        total_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for first_cell in self.cells:
            set_1 = self.cells[first_cell].possible_values
            if len(set_1) == 2:
                intersection_count = 0
                pair_found = False
                found_pair = None
                for second_cell in self.cells:
                    if second_cell != first_cell:
                        set_2 = self.cells[second_cell].possible_values
                        intersection = set_1.intersection(set_2)
                        if len(intersection) > 0:
                            intersection_count += 1
                            if len(intersection) == 2:
                                found_pair = second_cell
                                pair_found = True
                if intersection_count == 1 and pair_found:
                    self.cells[found_pair].possible_values = self.cells[first_cell].possible_values
                    self.cells[found_pair].impossible_values = total_set.difference(
                        self.cells[found_pair].possible_values)
                    self.eliminate_pair(self.cells[first_cell].possible_values)

    def eliminate_pair(self, pair):
        for cell in self.cells:
            if self.cells[cell].possible_values != pair:
                self.cells[cell].possible_values.difference(pair)
                self.cells[cell].impossible_values.union(pair)
                if len(self.cells[cell].possible_values) == 1:
                    self.cells[cell].definite_value = self.cells[cell].possible_values.copy().pop()
