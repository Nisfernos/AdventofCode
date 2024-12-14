from Utils.Day import DayFormat
import numpy as np


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 13)

    def part_one(self):
        # self.input = self.test_input

        machines = []
        for line in self.input:
            if line[:8] == "Button A":
                buttonA = int("".join([char for char in line.split(",")[0] if char.isdigit()])), int("".join([char for char in line.split(",")[1] if char.isdigit()]))
            elif line[:8] == "Button B":
                buttonB = int("".join([char for char in line.split(",")[0] if char.isdigit()])), int("".join([char for char in line.split(",")[1] if char.isdigit()]))
            elif line[:5] == "Prize":
                prize = int("".join([char for char in line.split(",")[0] if char.isdigit()])), int("".join([char for char in line.split(",")[1] if char.isdigit()]))
                machines.append((buttonA, buttonB, prize))
        
        result = 0
        for butA, butB, prize in machines:
            a = np.array([[butA[0], butB[0]], [butA[1], butB[1]]])
            b = np.array([prize[0], prize[1]])
            presses = np.linalg.solve(a, b)
            # if (presses[0]+0.001) % 1 < 0.1 and (presses[1]+0.001) % 1 < 0.1:
            #     result += int(presses[0]+0.1)*3 + int(presses[1]+0.1)
            presses = [int(presses[0]+0.01), int(presses[1]+0.01)]
            if presses[0]*butA[0]+presses[1]*butB[0] == prize[0] and presses[0]*butA[1]+presses[1]*butB[1] == prize[1]:
                result += presses[0]*3 + presses[1]

        print(result)

    def part_two(self):
        # self.input = self.test_input

        machines = []
        for line in self.input:
            if line[:8] == "Button A":
                buttonA = int("".join([char for char in line.split(",")[0] if char.isdigit()])), int("".join([char for char in line.split(",")[1] if char.isdigit()]))
            elif line[:8] == "Button B":
                buttonB = int("".join([char for char in line.split(",")[0] if char.isdigit()])), int("".join([char for char in line.split(",")[1] if char.isdigit()]))
            elif line[:5] == "Prize":
                prize = int("".join([char for char in line.split(",")[0] if char.isdigit()]))+10000000000000, int("".join([char for char in line.split(",")[1] if char.isdigit()]))+10000000000000
                machines.append((buttonA, buttonB, prize))
        
        result = 0
        for butA, butB, prize in machines:
            a = np.array([[butA[0], butB[0]], [butA[1], butB[1]]])
            b = np.array([prize[0], prize[1]])
            presses = np.linalg.solve(a, b)
            presses = [int(presses[0]+0.01), int(presses[1]+0.01)]
            if presses[0]*butA[0]+presses[1]*butB[0] == prize[0] and presses[0]*butA[1]+presses[1]*butB[1] == prize[1]:
                result += presses[0]*3 + presses[1]

        print(result)

Day()