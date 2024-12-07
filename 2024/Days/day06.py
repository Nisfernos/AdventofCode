from Utils.Day import DayFormat


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
        input = [[val for column in row for val in column] for row in self.input]
        for i, row in enumerate(input):
            if "^" in row:
                start_position = i, row.index("^")
                break

        position = start_position
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        direction = directions[0]

        # position row, column or y,x
        new_position = self.next_move(position, direction)
        blockades = set()
        i = 0
        while (0 <= new_position[0] < len(input) and 0 <= new_position[1] < len(input[0])):
            # if (self.input[new_position[0]][new_position[1]] != "#" and new_position != start_position # ChatGPT self.input[newpos] -> newpos
            #     and new_position not in blockades):
            #     # Make playing field with new block
            #     input2 = [llist[:] for llist in self.input]
            #     input2[new_position[0]][new_position[1]] = "#"
            #     if self.check_if_loop(input2, self.position, self.direction):
            #         blockades.add(new_position)
            if input[new_position[0]][new_position[1]] == "." and new_position != start_position:
                blockades.add(new_position)

            # If standing in front of #, turn 90 degrees
            if input[new_position[0]][new_position[1]] == "#":
                direction = directions[(directions.index(direction) + 1) % len(directions)]
            else:
                position = new_position
                # i += 1
            new_position = self.next_move(position, direction)
            # if i % 1000 == 0:
            #     print(i)

        result = 0
        for blockade in blockades:
            # Make playing field with new block
            input2 = [llist[:] for llist in input]
            input2[blockade[0]][blockade[1]] = "#"
            if self.check_if_loop(input2, start_position, directions[0]):
                result += 1

        # result = len(blockades)
        print(result)

    def check_if_loop(self, input, position, direction):
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        # direction = directions[(directions.index(direction) + 1) % len(directions)]
        new_position = self.next_move(position, direction)
        # turns it makes. list[(position, direction)]
        turns = []
        while (0 <= new_position[0] < len(input) and 0 <= new_position[1] < len(input[0])):

            if input[new_position[0]][new_position[1]] == "#":
                # If encounter a # from same direction again -> loop
                if (position, direction) in turns:
                    return True
                turns.append((position, direction))
                direction = directions[(directions.index(direction) + 1) % len(directions)]
            else:
                position = new_position
            new_position = self.next_move(position, direction)
        return False

    # def part_two(self):
    #     """
    #     Identify all positions where adding a blockade causes the guard to loop.
    #     """
    #     # Parse input and locate the guard's starting position
    #     self.input = [[val for column in row for val in column] for row in self.input]
    #     start_position = None
    #     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

    #     for i, row in enumerate(self.input):
    #         if "^" in row:
    #             start_position = (i, row.index("^"))
    #             break

    #     if not start_position:
    #         raise ValueError("No starting position found for the guard.")

    #     start_direction = directions[0]  # Guard starts facing up
    #     valid_positions = set()

    #     # Iterate over all possible positions to add an obstruction
    #     for i in range(len(self.input)):
    #         for j in range(len(self.input[0])):
    #             if self.input[i][j] == "." and (i, j) != start_position:
    #                 # Temporarily add an obstruction
    #                 self.input[i][j] = "#"
    #                 if self.check_if_loop(self.input, start_position, start_direction):
    #                     valid_positions.add((i, j))
    #                 # Remove the obstruction
    #                 self.input[i][j] = "."

    #     result = len(valid_positions)
    #     print(result)

    # def check_if_loop(self, grid, start_position, start_direction):
    #     """
    #     Simulate guard movement to check if a loop is formed.
    #     Returns True if the guard gets stuck in a loop.
    #     """
    #     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    #     position, direction = start_position, start_direction
    #     visited_states = set()

    #     while 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
    #         state = (position, direction)
    #         if state in visited_states:
    #             return True  # Loop detected
    #         visited_states.add(state)

    #         next_position = self.next_move(position, direction)

    #         # Turn if hitting a wall
    #         if 0 <= next_position[0] < len(grid) and 0 <= next_position[1] < len(grid[0]):
    #             if grid[next_position[0]][next_position[1]] == "#":
    #                 direction = directions[(directions.index(direction) + 1) % 4]
    #             else:
    #                 position = next_position
    #         else:
    #             break  # Guard moves out of bounds

    #     return False  # No loop detected


Day()