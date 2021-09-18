from src.sudoku.cell import Cell

total_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

class Group:
    def __init__(self):
        self.cells = {}

    def get_cell(self, index) -> Cell:
        return self.cells[index]

    def analyse_group(self):
        all_possibles = []
        for cell in self.cells:
            all_possibles.append(list(self.get_cell(cell).possible_values))
        for i in range(9):
            number = i + 1
            times_found = 0
            found_at = []
            for j in range(9):
                if str(number) in all_possibles[j]:
                    times_found += 1
                    found_at.append(j)
            if times_found == 1:
                cell_index = found_at[0]
                this_cell = self.get_cell(cell_index)
                if this_cell.definite_value != str(number):
                    this_cell.set_definite(str(number))
            if 2 <= times_found <= 3 and self.cells[0].box_number != self.cells[8].box_number:
                self.all_in_one_subgroup(number, found_at)

    def all_in_one_subgroup(self, number, found_at_list):
        subgroup_1 = []
        subgroup_2 = []
        subgroup_3 = []
        for member in found_at_list:
            if 0 <= member <= 2:
                subgroup_1.append(self.cells[member])
            if 3 <= member <= 5:
                subgroup_2.append(self.cells[member])
            if 6 <= member <= 8:
                subgroup_3.append(self.cells[member])
        if subgroup_2 == [] and subgroup_3 == []:
            self.eliminate_from_rest_of_box(subgroup_1, number)
        else:
            if subgroup_1 == [] and subgroup_3 == []:
                self.eliminate_from_rest_of_box(subgroup_2, number)
            else:
                if subgroup_1 == [] and subgroup_2 == []:
                    self.eliminate_from_rest_of_box(subgroup_3, number)

    @staticmethod
    def eliminate_from_rest_of_box(part_of_group, number):
        if part_of_group[0].box_number == part_of_group[1].box_number:
            target_box = part_of_group[0].puzzle.boxes[part_of_group[0].box_number]
        for cell in target_box.cells:
            this_cell = target_box.cells[cell]
            keep = False
            for keep_cell in part_of_group:
                if this_cell == keep_cell:
                    keep = True
            if not keep:
                if this_cell.definite_value == "_":
                    this_cell.impossible_values.add(str(number))
                    this_cell.possible_values = total_set.difference(this_cell.impossible_values)

    def find_pairs(self):
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
                    self.cells[found_pair].impossible_values = self.cells[found_pair].impossible_values.difference(
                        self.cells[found_pair].possible_values)
                    self.eliminate_pair(self.cells[first_cell].possible_values)

    def eliminate_pair(self, pair):
        for cell in self.cells:
            this_cell = self.get_cell(cell)
            if this_cell.possible_values != pair:
                this_cell.possible_values.difference(pair)
                this_cell.impossible_values.union(pair)
                if len(this_cell.possible_values) == 1:
                    if this_cell.definite_value != this_cell.possible_values.copy().pop():
                        this_cell.set_definite(this_cell.possible_values.copy().pop())
