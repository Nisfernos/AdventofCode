from Utils.Day import DayFormat
import copy


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 6)

    def part_one(self):
        self.input1 = [[val for column in row for val in column] for row in self.input]
        for i, row in enumerate(self.input1):
            if "^" in row:
                self.position = i, row.index("^")

        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        self.direction = directions[0]

        # position row, column or y,x
        new_position = self.move()
        while 0 <= new_position[0] < len(self.input1) and 0 <= new_position[1] < len(self.input1[0]):
            if self.input1[new_position[0]][new_position[1]] == "#":
                self.direction = directions[(directions.index(self.direction) + 1) % len(directions)]
            else:
                self.input1[self.position[0]][self.position[1]] = "X"
                self.position = new_position
            new_position = self.move()
        self.input1[self.position[0]][self.position[1]] = "X"
        result = sum([1 for row in self.input1 for column in row if column == "X"])
        print(result)

    def move(self):
        return self.position[0]+self.direction[0], self.position[1]+ self.direction[1]

    def next_move(self, position, direction):
        return position[0] + direction[0], position[1] + direction[1]

    def part_two(self):
        self.input = [[val for column in row for val in column] for row in self.input]
        for i, row in enumerate(self.input):
            if "^" in row:
                start_position = i, row.index("^")

        self.position = start_position
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        anns = ["^", ">", "v", "<"]
        self.direction = directions[0]

        # position row, column or y,x
        new_position = self.next_move(self.position, self.direction)
        blockades = set()
        # i = 0
        while 0 <= new_position[0] < len(self.input) and 0 <= new_position[1] < len(self.input[0]):
            if (self.input[new_position[0]][new_position[1]] != "#" and new_position != start_position # ChatGPT self.input[newpos] -> newpos
                and new_position not in blockades):
                # Make playing field with new block
                # input2 = [llist[:] for llist in self.input]
                input2 = copy.deepcopy(self.input)
                input2[new_position[0]][new_position[1]] = "#"
                if self.check_if_loop(input2, self.position, self.direction):
                    blockades.add(new_position)

            # If standing in front of #, turn 90 degrees
            if self.input[new_position[0]][new_position[1]] == "#":
                self.direction = directions[(directions.index(self.direction) + 1) % len(directions)]
                self.input[self.position[0]][self.position[1]] = "+"
            else:
                if self.input[self.position[0]][self.position[1]] != "+":
                    self.input[self.position[0]][self.position[1]] = anns[directions.index(self.direction)]
                self.position = new_position
            new_position = self.next_move(self.position, self.direction)
            i += 1
            # print(self.position)
            print(i)

        # for x in self.input:
        #     print(x)
        # print(i)

        result = len(blockades)
        print(result)

    def check_if_loop(self, input, position, direction):
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        anns = ["^", ">", "v", "<"]
        direction = directions[(directions.index(direction) + 1) % len(directions)]
        new_position = self.next_move(position, direction)
        # turns it makes. list[(position, direction)]
        turns = []
        while 0 <= new_position[0] < len(input) and 0 <= new_position[1] < len(input[0]):
            # if input[position[0]][position[1]] == "+" and input[new_position[0]][new_position[1]] == "#":
            #     return True
            if input[new_position[0]][new_position[1]] == "#":
                # If encounter a # from same direction again -> loop
                if (position, direction) in turns:
                    return True
                turns.append((position, direction))
                direction = directions[(directions.index(direction) + 1) % len(directions)]
                input[position[0]][position[1]] = "+"
            else:
                if input[position[0]][position[1]] != "+":
                    input[position[0]][position[1]] = anns[directions.index(direction)]
                position = new_position
            new_position = self.next_move(position, direction)
        return False

Day()