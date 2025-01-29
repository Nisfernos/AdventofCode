from Utils.Day import DayFormat


class Grid():
    def __init__(self, grid) -> None:
        self.cards = ((-1,0), (0,1), (1,0), (0,-1))
        self.make_grid(grid)
        self.pos_agent = [(i,row.index("@")) for i, row in enumerate(self.grid) if "@" in row][0]

    def make_grid(self, grid_rows):
        self.grid = [[char for char in row] for row in grid_rows]
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def print_grid(self):
        for row in self.grid:
            print("".join(row))

    def move_agent(self, move):
        move = self.cards[["^",">","v","<"].index(move)]
        new_pos = (self.pos_agent[0]+move[0], self.pos_agent[1]+move[1])
        match self.grid[new_pos[0]][new_pos[1]]:
            case "#":
                return
            case ".":
                self.grid[new_pos[0]][new_pos[1]] = "@"
                self.grid[self.pos_agent[0]][self.pos_agent[1]] = "."
                self.pos_agent = [new_pos[0], new_pos[1]]
            case "O":
                i = 2
                while self.grid[self.pos_agent[0]+move[0]*i][self.pos_agent[1]+move[1]*i] == "O":
                    i += 1
                if self.grid[self.pos_agent[0]+move[0]*i][self.pos_agent[1]+move[1]*i] == "#":
                    return
                elif self.grid[self.pos_agent[0]+move[0]*i][self.pos_agent[1]+move[1]*i] == ".":
                    self.grid[self.pos_agent[0]+move[0]*i][self.pos_agent[1]+move[1]*i] = "O"
                    self.grid[new_pos[0]][new_pos[1]] = "@"
                    self.grid[self.pos_agent[0]][self.pos_agent[1]] = "."
                    self.pos_agent = [new_pos[0], new_pos[1]]
                    return
                

class GridWide():
    def __init__(self, grid) -> None:
        self.cards = ((-1,0), (0,1), (1,0), (0,-1))
        self.make_grid(grid)
        self.pos_agent = [(i,row.index("@")) for i, row in enumerate(self.grid) if "@" in row][0]

    def make_grid(self, grid_rows):
        self.grid = [[] for _ in grid_rows]
        for i,row in enumerate(grid_rows):
            for char in row:
                if char in "#.":
                    self.grid[i].append(char)
                    self.grid[i].append(char)
                elif char == "@":
                    self.grid[i].append("@")
                    self.grid[i].append(".")
                else:
                    self.grid[i].append("[")
                    self.grid[i].append("]")
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def print_grid(self):
        for row in self.grid:
            print("".join(row))

    def move(self, move):
        move = self.cards[["^",">","v","<"].index(move)]
        new_pos = (self.pos_agent[0]+move[0], self.pos_agent[1]+move[1])
        match self.grid[new_pos[0]][new_pos[1]]:
            case "#":
                return
            case ".":
                self.move_agent(new_pos)
                return
            case _:
                if move[0] == 0:
                    i = 2
                    while self.grid[self.pos_agent[0]+move[0]*i][self.pos_agent[1]+move[1]*i] in "[]":
                        i += 1
                    if self.grid[self.pos_agent[0]+move[0]*i][self.pos_agent[1]+move[1]*i] == "#":
                        return
                    elif self.grid[self.pos_agent[0]+move[0]*i][self.pos_agent[1]+move[1]*i] == ".":
                        for x in range(2,i+1):
                            if move[1] == 1:
                                self.grid[self.pos_agent[0]+move[0]*x][self.pos_agent[1]+move[1]*x] = "[]"[x%2]
                            else:
                                self.grid[self.pos_agent[0]+move[0]*x][self.pos_agent[1]+move[1]*x] = "]["[x%2]
                        self.move_agent(new_pos)
                        return
                else:
                    new_grid = [[val for val in row] for row in self.grid]
                    check_pos = [new_pos]
                    moves = {}
                    while check_pos:
                        new_check_pos = []
                        for pos in check_pos:
                            if self.grid[pos[0]][pos[1]] == "#":
                                return
                            elif self.grid[pos[0]][pos[1]] == "[":
                                new_check_pos.append((pos[0]+move[0], pos[1]))
                                new_check_pos.append((pos[0]+move[0], pos[1]+1))
                                moves[(pos[0]+move[0], pos[1])] = "["
                                moves[(pos[0]+move[0], pos[1]+1)] = "]"
                                new_grid[pos[0]][pos[1]] = "."
                                new_grid[pos[0]][pos[1]+1] = "."
                            elif self.grid[pos[0]][pos[1]] == "]":
                                new_check_pos.append((pos[0]+move[0], pos[1]))
                                new_check_pos.append((pos[0]+move[0], pos[1]-1))
                                moves[(pos[0]+move[0], pos[1]-1)] = "["
                                moves[(pos[0]+move[0], pos[1])] = "]"
                                new_grid[pos[0]][pos[1]] = "."
                                new_grid[pos[0]][pos[1]-1] = "."
                        check_pos = new_check_pos
                    for pos, struc in moves.items():
                        new_grid[pos[0]][pos[1]] = struc
                    self.grid = new_grid
                    self.move_agent(new_pos)
                    return
                    
    def move_agent(self, new_pos):
        self.grid[new_pos[0]][new_pos[1]] = "@"
        self.grid[self.pos_agent[0]][self.pos_agent[1]] = "."
        self.pos_agent = [new_pos[0], new_pos[1]]



class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 15)

    def part_one(self):
        # self.input = self.test_input

        divider = self.input.index("")
        gridrows = self.input[:divider]
        self.movement = "".join(line for line in self.input[divider:])
        self.grid = Grid(gridrows)
        for move in self.movement:
            self.grid.move_agent(move)
            # print(f"Move {move}:")
        # self.grid.print_grid()
            # input()

        # print([i*100+j for i,row in enumerate(self.grid.grid) for j,val in enumerate(row) if val == "O"])
        result = sum([i*100+j for i,row in enumerate(self.grid.grid) for j,val in enumerate(row) if val == "O"])

        print(result)

    def part_two(self):
        self.input = self.restore
        # self.input = self.test_input

        divider = self.input.index("")
        gridrows = self.input[:divider]
        self.movement = "".join(line for line in self.input[divider:])
        self.grid = GridWide(gridrows)
        # self.grid.print_grid()
        for move in self.movement:
            self.grid.move(move)
            # print(f"Move {move}:")
            # self.grid.print_grid()
            # input()

        result = sum([i*100+j for i,row in enumerate(self.grid.grid) for j,val in enumerate(row) if val == "["])

        print(result)


Day()