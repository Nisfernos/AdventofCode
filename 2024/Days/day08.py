from Utils.Day import DayFormat
import re


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 8)

    def part_one(self):
        # self.input  = self.test_input
        self.height = len(self.input)
        self.width = len(self.input[0])
        locations = {}
        for i, row in enumerate(self.input):
            for j, val in enumerate(row):
                if re.match("[\d\w]", val):
                    if val in locations.keys():
                        locations[val].append((i,j))
                    else:
                        locations[val] = [(i,j)]

        antinodes = set()
        for locs in locations.values():
            for x in range(len(locs)-1):
                for y in range(x+1, len(locs)):
                    antinodes.update(self.in_bounds(locs[x], locs[y]))

        result = len(antinodes)
        print(result)

    def step(self, x, step):
        return x[0]+step[0], x[1]+step[1]

    def in_bounds(self, x, y):
        diff = (y[0] - x[0], y[1] - x[1])
        idiff = -diff[0], -diff[1]

        antinodes = []
        # Check x + idiff
        pos_loc = self.step(x, idiff)
        if 0 <= pos_loc[0] < self.height and 0 <= pos_loc[1] < self.width:
            antinodes.append(pos_loc)
        # Check y + diff
        pos_loc = self.step(y, diff)
        if 0 <= pos_loc[0] < self.height and 0 <= pos_loc[1] < self.width:
            antinodes.append(pos_loc)
        return antinodes

    def part_two(self):
        self.input  = self.test_input
        self.height = len(self.input)
        self.width = len(self.input[0])
        locations = {}
        for i, row in enumerate(self.input):
            for j, val in enumerate(row):
                if re.match("[\d\w]", val):
                    if val in locations.keys():
                        locations[val].append((i,j))
                    else:
                        locations[val] = [(i,j)]

        antinodes = set()
        for locs in locations.values():
            for x in range(len(locs)-1):
                for y in range(x+1, len(locs)):
                    antinodes.update(self.in_bounds2(locs[x], locs[y]))

        result = len(antinodes)
        print(result)

    def in_bounds2(self, x, y):
        diff = (y[0] - x[0], y[1] - x[1])
        idiff = -diff[0], -diff[1]
        nodes = [x,y]
        diffs = [diff, idiff]

        antinodes = set()
        for i, node in enumerate(nodes):
            diff = diffs[i]
            pos_loc = [0,0]
            j = 1
            while 0 <= pos_loc[0] < self.height and 0 <= pos_loc[1] < self.width:
                cdiff = diff[0]*j, diff[1]*j
                pos_loc = self.step(node, cdiff)
                if 0 <= pos_loc[0] < self.height and 0 <= pos_loc[1] < self.width:
                    antinodes.add(pos_loc)
                j += 1
        if antinodes:
            antinodes.update([x,y])
        return antinodes

Day()