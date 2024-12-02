from Utils.Day import DayFormat


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 2)

    def part_one(self):
        reports = [[int(y) for y in line.split(" ")] for line in self.input]
        differences = [[rep[i+1]-rep[i] for i in range(len(rep)-1)] for rep in reports]
        cond = [[(abs(rep[i]) <= 3) and (rep[i] > 0 if rep[0] > 0 else rep[i] < 0) for i in range(len(rep))] for rep in differences]
        result = sum([int(not False in rep) for rep in cond])
        print(result)

    def part_two(self):
        reports = [[int(y) for y in line.split(" ")] for line in self.input]
        differences = [[rep[i+1]-rep[i] for i in range(len(rep)-1)] for rep in reports]
        cond = [[(abs(rep[i]) <= 3) and (rep[i] > 0 if rep[0] > 0 else rep[i] < 0) for i in range(len(rep))] for rep in differences]
        result = sum([int(rep.count(False) <= 1) for rep in cond])
        print(result)

Day()