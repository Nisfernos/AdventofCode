from Utils.Day import DayFormat
import re


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 3)

    def part_one(self):
        valid_muls = [re.findall("mul\(\d{1,3},\d{1,3}\)", line) for line in self.input]
        flat_muls = [val for mul_list in valid_muls for val in mul_list]
        result = sum([int(multip[4:-1].split(",")[0])*int(multip[4:-1].split(",")[1]) for multip in flat_muls])
        print(result)

    def part_two(self):
        valid_muls = [re.findall("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", line) for line in self.input]
        flat_muls = [val for mul_list in valid_muls for tp in mul_list for val in tp if val]
        enabled = True
        result = 0
        for operation in flat_muls:
            if operation[0] == "d":
                enabled = False if operation == "don't()" else True
                continue
            if enabled:
                result += int(operation[4:-1].split(",")[0])*int(operation[4:-1].split(",")[1])
        print(result)
            

Day()