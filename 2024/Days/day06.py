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

    def part_two(self):
        self.input = [[val for column in row for val in column] for row in self.input]
        for i, row in enumerate(self.input):
            if "^" in row:
                self.position = i, row.index("^")
        start_position = self.position
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        anns = ["^", ">", "v", "<"]
        self.direction = directions[0]

        # position row, column or y,x
        new_position = self.move()
        result = 0
        blockades = set()
        i = 0
        while 0 <= new_position[0] < len(self.input) and 0 <= new_position[1] < len(self.input[0]):
            check_dir = directions[(directions.index(self.direction) + 1) % len(directions)]
            cells = [self.input[new_position[0]+check_dir[0]*i][new_position[1]+ check_dir[1]*i] for i in range(1, len(self.input)) if ((0 <= new_position[0]+check_dir[0]*i < len(self.input)) and (0 <= new_position[1]+ check_dir[1]*i < len(self.input)))]
            # If possible blockade not start position
            if (new_position[0]+self.direction[0], new_position[1]+self.direction[1]) != start_position:
                if "#" in cells:
                    blockade = new_position[0]+self.direction[0], new_position[1]+self.direction[1]
                    # If already walked
                    if "+" in cells:
                        if cells.index("+") < cells.index("#"):
                                result += 1
                                blockades.add(blockade)
                    # See if loops
                    else:
                        self.input2 = [llist[:] for llist in self.input]
                        # Set blockade
                        if 0 <= new_position[0]+self.direction[0] < len(self.input) and 0 <= new_position[1]+self.direction[1] < len(self.input):
                            self.input2[new_position[0]+self.direction[0]][new_position[1]+self.direction[1]] = "#"
                            self.position2 = self.position
                            new_position2 = new_position
                            self.direction2 = directions[(directions.index(self.direction) + 1) % len(directions)]
                            prev_pos = []
                            while 0 <= new_position2[0] < len(self.input2) and 0 <= new_position2[1] < len(self.input2[0]):
                                if self.input2[new_position2[0]][new_position2[1]] == "#":
                                    self.direction2 = directions[(directions.index(self.direction2) + 1) % len(directions)]
                                    self.input2[self.position2[0]][self.position2[1]] = "+"
                                else:
                                    # if self.input2[new_position2[0]][new_position2[1]] == "+":
                                    # if (self.input2[self.position2[0]][self.position2[1]] == "|" and directions.index(self.direction2) % 2 == 0) or (self.input2[self.position2[0]][self.position2[1]] == "-" and directions.index(self.direction2) % 2 == 1):
                                    if self.input2[self.position2[0]][self.position2[1]] == anns[directions.index(self.direction2)] or self.position2 in prev_pos:
                                        result += 1
                                        blockades.add(blockade)
                                        # print(self.position, 2, blockade)
                                        # print(result)
                                        break
                                    if self.input2[self.position2[0]][self.position2[1]] != "+":
                                        # self.input2[self.position2[0]][self.position2[1]] = "|" if directions.index(self.direction2) % 2 == 0 else "-"
                                        self.input2[self.position2[0]][self.position2[1]] = anns[directions.index(self.direction2)]
                                    self.position2 = new_position2
                                    # if i > 439:
                                    #     print(self.position2)
                                prev_pos.append(self.position2)
                                new_position2 = self.position2[0]+self.direction2[0], self.position2[1]+ self.direction2[1]
            if self.input[new_position[0]][new_position[1]] == "#":
                self.direction = directions[(directions.index(self.direction) + 1) % len(directions)]
                self.input[self.position[0]][self.position[1]] = "+"
            else:
                if self.input[self.position[0]][self.position[1]] != "+":
                    # self.input[self.position[0]][self.position[1]] = "|" if directions.index(self.direction) % 2 == 0 else "-"
                    self.input[self.position[0]][self.position[1]] = anns[directions.index(self.direction)]
                self.position = new_position
            new_position = self.move()
            i += 1
            print(i)
            # print(self.position)

        # for x in self.input:
        #     print(x)

        # self.position = start_position
        # self.direction = directions[0]
        # new_position = self.move()
        # result = 
        # while 0 <= new_position[0] < len(self.input) and 0 <= new_position[1] < len(self.input[0]):
            # check_dir = directions[(directions.index(self.direction) + 1) % len(directions)]
            # cells = [self.input[new_position[0]+check_dir[0]*i][new_position[1]+ check_dir[1]*i] for i in range(1, len(self.input)) if ((0 <= new_position[0]+check_dir[0]*i < len(self.input)) and (0 <= new_position[1]+ check_dir[1]*i < len(self.input)))]
            # # If blockade not start position
            # if (new_position[0]+self.direction[0], new_position[1]+self.direction[1]) != start_position:
            #     if "#" in cells:
            #         # If already walked
            #         if "+" in cells:
            #             if cells.index("+") < cells.index("#"):
            #                     result += 1
            #         # See if loops
            #         else:
            #             self.input2 = self.input

            # if self.input[new_position[0]][new_position[1]] == "#":
            #     self.direction = directions[(directions.index(self.direction) + 1) % len(directions)]
            # else:
            #     self.position = new_position
            # new_position = self.move()
       
        # with open("testing.txt", "w") as file:
        #     for row in self.input:
        #         for val in row:
        #             file.write(val)
        #         file.write("\n")
        print(len(blockades))
        print(result)


Day() 

"""
Bad ideas:
 # or_pos = self.position
            # or_dir = self.direction
            # or_new_pos = new_position
            # i = 0
            # self.input[new_position[0]][new_position[1]] = "#"
            # while 0 <= new_position[0] < len(self.input) and 0 <= new_position[1] < len(self.input[0]):
            #     if self.input[new_position[0]][new_position[1]] == "#":
            #         self.direction = directions[(directions.index(self.direction) + 1) % len(directions)]
            #     else:
            #         self.input[self.position[0]][self.position[1]] = "X"
            #         self.position = new_position
            #     new_position = self.move()
            #     i += 1
            #     if i > 169000:
            #         result += 1
            #         break
            # self.position = or_pos
            # self.direction = or_dir
            # new_position = or_new_pos
            # if self.input[new_position[0]][new_position[1]] == "X":
            #     check_dir = directions[(directions.index(self.direction) + 1) % len(directions)]
            #     if self.input[new_position[0]+check_dir[0]][new_position[1]+ check_dir[1]] == "X":
            #         if (new_position[0]+self.direction[0], new_position[1]+self.direction[1]) != start_position:
            #             result += 1
                        # obstacles.append(new_position)
                        # for x in self.input:
                        #     print(x)
                        # print()

                        
---------------------------
new_position = self.move()
        result = 0
        while 0 <= new_position[0] < len(self.input) and 0 <= new_position[1] < len(self.input[0]):
            check_dir = directions[(directions.index(self.direction) + 1) % len(directions)]
            cells = [self.input[new_position[0]+check_dir[0]*i][new_position[1]+ check_dir[1]*i] for i in range(1, len(self.input)) if ((0 <= new_position[0]+check_dir[0]*i < len(self.input)) and (0 <= new_position[1]+ check_dir[1]*i < len(self.input)))]
            # if (("|" in cells and directions.index(check_dir) % 2 == 0) or ("-" in cells and directions.index(check_dir) % 2 == 1) or "+" in cells) and "#" in cells:
            # if any([cells[c-1] == "+" for c,cell in enumerate(cells) if cell == "#"]):
            if "+" in cells and "#" in cells:
                if cells.index("+") < cells.index("#"):
                    if (new_position[0]+self.direction[0], new_position[1]+self.direction[1]) != start_position:
                        result += 1
            # check_dir = directions[(directions.index(self.direction) + 1) % len(directions)]
            # cells = [self.input[new_position[0]+check_dir[0]*i][new_position[1]+ check_dir[1]*i] for i in range(1, len(self.input)) if ((0 <= new_position[0]+check_dir[0]*i < len(self.input)) and (0 <= new_position[1]+ check_dir[1]*i < len(self.input)))]
            # # if (("|" in cells and directions.index(check_dir) % 2 == 0) or ("-" in cells and directions.index(check_dir) % 2 == 1) or "+" in cells) and "#" in cells:
            # if any([cells[c-1] == "+" for c,cell in enumerate(cells) if cell == "#"]):
            #     if (new_position[0]+self.direction[0], new_position[1]+self.direction[1]) != start_position:
            #         result += 1
            if self.input[new_position[0]][new_position[1]] == "#":
                self.direction = directions[(directions.index(self.direction) + 1) % len(directions)]
                self.input[self.position[0]][self.position[1]] = "+"
            else:
                if self.input[self.position[0]][self.position[1]] != "+":
                    self.input[self.position[0]][self.position[1]] = "|" if directions.index(self.direction) % 2 == 0 else "-"
                self.position = new_position
            new_position = self.move()

        # for x in self.input:
        #     print(x)

        # self.position = start_position
        # self.direction = directions[0]
        # new_position = self.move()
        # result = 0
        # while 0 <= new_position[0] < len(self.input) and 0 <= new_position[1] < len(self.test_input[0]):
        #     check_dir = directions[(directions.index(self.direction) + 1) % len(directions)]
        #     cells = [self.input[new_position[0]+check_dir[0]*i][new_position[1]+ check_dir[1]*i] for i in range(1, len(self.input)) if ((0 <= new_position[0]+check_dir[0]*i < len(self.input)) and (0 <= new_position[1]+ check_dir[1]*i < len(self.input)))]
        #     # if (("|" in cells and directions.index(check_dir) % 2 == 0) or ("-" in cells and directions.index(check_dir) % 2 == 1) or "+" in cells) and "#" in cells:
        #     # if any([cells[c-1] == "+" for c,cell in enumerate(cells) if cell == "#"]):
        #     if "+" in cells and "#" in cells:
        #         if cells.index("+") < cells.index("#"):
        #             if (new_position[0]+self.direction[0], new_position[1]+self.direction[1]) != start_position:
        #                 result += 1
        #     if self.input[new_position[0]][new_position[1]] == "#":
        #         self.direction = directions[(directions.index(self.direction) + 1) % len(directions)]
        #         self.input[self.position[0]][self.position[1]] = "+"
        #     else:
        #         if self.input[self.position[0]][self.position[1]] != "+":
        #             self.input[self.position[0]][self.position[1]] = "|" if directions.index(self.direction) % 2 == 0 else "-"
        #         self.position = new_position
        #     new_position = self.move()
        # print(positions)
        with open("testing.txt", "w") as file:
            for row in self.input:
                for val in row:
                    file.write(val)
                file.write("\n")
        print(result)


            check_dir = directions[(directions.index(self.direction) + 1) % len(directions)]
            cells = [self.input[new_position[0]+check_dir[0]*i][new_position[1]+ check_dir[1]*i] for i in range(1, len(self.input)) if ((0 <= new_position[0]+check_dir[0]*i < len(self.input)) and (0 <= new_position[1]+ check_dir[1]*i < len(self.input)))]
            if "+" in cells and "#" in cells:
                if cells.index("+") < cells.index("#"):
                    if (new_position[0]+self.direction[0], new_position[1]+self.direction[1]) != start_position:
                        result += 1
"""