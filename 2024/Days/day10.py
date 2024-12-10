from Utils.Day import DayFormat


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 10)


    def part_one(self):
        # self.input = self.test_input
        self.height = len(self.input)
        self.width = len(self.input[0])

        result = 0
        for row, line in enumerate(self.input):
            for col, val in enumerate(line):
                if val == "0":
                    result += len(self.step((row,col)))
        print(result)

    def cheight(self, pos, dir=(0,0)):
        return self.input[pos[0]+dir[0]][pos[1]+dir[1]]

    def neighbours(self, pos):
        cards = [(-1,0), (0,1), (1,0), (0,-1)]

        neighbours = []
        for dir in cards:
            if 0 <= pos[0]+dir[0] < self.height and 0 <= pos[1]+dir[1] < self.width:
                neighbours.append(dir)
        return neighbours

    def step(self, pos):
        if self.cheight(pos) == "9":
            positions = {pos}
            return positions
        positions = set()
        for neighbour in self.neighbours(pos):
            if str(int(self.cheight(pos))+1) == self.cheight(pos, neighbour):
                positions.update(self.step((pos[0]+neighbour[0],pos[1]+neighbour[1])))
        return positions

    def part_two(self):
        # self.input = self.test_input
        self.height = len(self.input)
        self.width = len(self.input[0])

        result = 0
        for row, line in enumerate(self.input):
            for col, val in enumerate(line):
                if val == "0":
                    result += self.step2((row,col))
        print(result)

    def step2(self, pos):
        if self.cheight(pos) == "9":
            return 1
        paths = 0
        for neighbour in self.neighbours(pos):
            if str(int(self.cheight(pos))+1) == self.cheight(pos, neighbour):
                paths += self.step2((pos[0]+neighbour[0],pos[1]+neighbour[1]))
        return paths

Day()