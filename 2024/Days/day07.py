from Utils.Day import DayFormat
from itertools import product


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 7)

    def part_one(self):
        # self.input = self.test_input
        input = [(int(line.split(":")[0]), [int(part) for part in line.split(":")[1].strip().split(" ")]) for line in self.input]
        operators = ["+", "*"]

        result = 0
        for eq in input:
            solu, parts = eq[0], eq[1]
            op_combs = product(operators, repeat=len(parts)-1)
            for oc in op_combs:
                ttr = self.solve(parts[0], parts[1], oc[0])
                for i in range(2, len(parts)):
                    ttr = self.solve(ttr, parts[i], oc[i-1])
                if ttr == solu:
                    result += solu
                    break

        print(result)

    def solve(self, one, two, operator):
        match operator:
            case "*":
                return one*two
            case "+":
                return one+two
            case "||":
                return int(str(one)+str(two))

    def part_two(self):
        # self.input = self.test_input
        input = [(int(line.split(":")[0]), [int(part) for part in line.split(":")[1].strip().split(" ")]) for line in self.input]
        operators = ["+", "*", "||"]

        result = 0
        for eq in input:
            solu, parts = eq[0], eq[1]
            op_combs = product(operators, repeat=len(parts)-1)
            for oc in op_combs:
                ttr = self.solve(parts[0], parts[1], oc[0])
                for i in range(2, len(parts)):
                    ttr = self.solve(ttr, parts[i], oc[i-1])
                if ttr == solu:
                    result += solu
                    break

        print(result)

Day()