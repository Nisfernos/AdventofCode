from Utils.Day import DayFormat


class Grid():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.nodes = []

    def step(self):
        for node in self.nodes:
            node.step()

    def make_grid(self):
        self.grid = [[" " for c in range(self.width)] for r in range(self.height)]
        for node in self.nodes:
            if self.grid[node.y][node.x] == " ":
                self.grid[node.y][node.x] = "1"
            else:
                self.grid[node.y][node.x] = str(int(self.grid[node.y][node.x])+1)
    
    def valid_grid(self, trunk_length):
        self.make_grid()
        trunks = 0
        for column in range(self.width):
            tl = 0
            for row in range(self.height):
                if tl >= trunk_length:
                    trunks += 1
                if self.grid[row][column].isdigit():
                    tl += 1
                else:
                    tl = 0
        return trunks >= 2

    def print_grid(self, second):
        # grid = self.make_grid()
        for row in self.grid:
            print("".join(row))
        print(f"Above is second: {second}")
        print("---------------------------------------------------------------------------------")

class Node():
    def __init__(self, x, y, vx, vy, height, width):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.height = height
        self.width = width

    def step(self):
        self.x = (self.x + self.vx) % self.width
        self.y = (self.y + self.vy) % self.height


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 14)

    def part_one(self):
        self.height = 103
        self.width = 101
        steps = 100

        # self.input = self.test_input
        # self.height = 7
        # self.width = 11

        quadrants = [[0,0],[0,0]]
        result = 0
        for line in self.input:
            pos, vel = line.split("v")
            x = int("".join([char for char in pos.split(",")[0] if char.isdigit()]))
            y = int("".join([char for char in pos.split(",")[1] if char.isdigit()]))
            vx = int(vel.split(",")[0].strip("="))
            vy = int(vel.split(",")[1])
            
            # position after steps
            fin_x = (x + vx * steps) % self.width
            fin_y = (y + vy * steps) % self.height
            
            #check if middle
            if fin_x == self.width // 2 or fin_y == self.height // 2:
                continue
            quadrants[fin_x < self.width // 2][fin_y < self.height // 2] = quadrants[fin_x < self.width // 2][fin_y < self.height // 2] + 1
        
        result = 1
        for amount in [val for row in quadrants for val in row]:
            result = result * amount
        
        print(result)

    def part_two(self):
        self.height = 103
        self.width = 101

        # self.input = self.test_input
        # self.height = 7
        # self.width = 11

        grid = Grid(self.height, self.width)
        for line in self.input:
            pos, vel = line.split("v")
            x = int("".join([char for char in pos.split(",")[0] if char.isdigit()]))
            y = int("".join([char for char in pos.split(",")[1] if char.isdigit()]))
            vx = int(vel.split(",")[0].strip("="))
            vy = int(vel.split(",")[1])

            grid.nodes.append(Node(x,y,vx,vy,self.height,self.width))

        inp = False
        second = 0
        while not inp:
            # Checking for long line was hint from Reddit: https://www.reddit.com/r/adventofcode/comments/1hdwdak/comment/m1zfv5c/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
            if grid.valid_grid(6):
                grid.print_grid(second)

                x = input()
                if x:
                    inp = True

            grid.step()
            second += 1
        # grid.print_grid(0)
        # for _ in range(100):
        #     grid.step()
        # grid.print_grid(100)

Day()
