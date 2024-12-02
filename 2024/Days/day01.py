# from Utils.Day import DayFormat
from Utils.Day import DayFormat


class Day01(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 1)

    def part_one(self):
        list1, list2 = zip(*[(int(x), int(y)) for line in self.input for x,y in [line.strip().split()]])
        result = sum(abs(x-y) for x,y in zip(sorted(list1), sorted(list2)))
        print(result)

    def part_two(self):
        list1, list2 = zip(*[(int(x), int(y)) for line in self.input for x,y in [line.strip().split()]])
        result = sum([i*list2.count(i) for i in list1])
        print(result)

Day01()