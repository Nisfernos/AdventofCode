from Utils.Day import DayFormat


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 4)

    def part_one(self):
        self.limit = len(self.input[0])
        self.len_word = 4
        result = 0
        for i, line in enumerate(self.input):
            for j, letter in enumerate(line):
                if letter == "X":
                    result += self.search(self.input, "XMAS", i, j)
        print(result)


    def directions(self, i, j):
        directions = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]
        if i < self.len_word-1:
            directions = list(filter(lambda x: x not in [(-1,1), (-1,0), (-1,-1)], directions))
        if i > self.limit-self.len_word:
            directions = list(filter(lambda x: x not in [(1,-1), (1,0), (1,1)], directions))
        if j < self.len_word-1:
            directions = list(filter(lambda x: x not in [(0,-1), (1,-1), (-1,-1)], directions))
        if j > self.limit-self.len_word:
            directions = list(filter(lambda x: x not in [(1,1), (0,1), (-1,1)], directions))
        return directions
    
    def search(self, input, word, i, j):
        # i = row (y); j = column (x)
        directions = self.directions(i,j)
        valid = 0
        for direction in directions:
            if not input[i+direction[0]*1][j+direction[1]*1] == "M":
                continue
            if not input[i+direction[0]*2][j+direction[1]*2] == "A":
                continue
            if not input[i+direction[0]*3][j+direction[1]*3] == "S":
                continue
            valid += 1
        return valid
    
    def part_two(self):
        self.limit = len(self.input[0])
        result = 0
        for i, line in enumerate(self.input):
            for j, letter in enumerate(line):
                if i == 0 or j ==0 or i == self.limit-1 or j == self.limit-1:
                    continue
                if letter == "A":
                    result += self.search2(self.input, i, j)
        print(result)
    
    def search2(self, input, i, j):
        # i = row (y); j = column (x)
        directions = [[(1,1), (-1,-1)], [(1,-1), (-1,1)]]
        if ((input[i+directions[0][0][0]][j+directions[0][0][1]] == "M" 
            and input[i+directions[0][1][0]][j+directions[0][1][1]] == "S")
            or (input[i+directions[0][1][0]][j+directions[0][1][1]] == "M" 
            and input[i+directions[0][0][0]][j+directions[0][0][1]] == "S")):
            if (input[i+directions[1][0][0]][j+directions[1][0][1]] == "M" 
                and input[i+directions[1][1][0]][j+directions[1][1][1]] == "S"):
                return 1
            
            if (input[i+directions[1][1][0]][j+directions[1][1][1]] == "M" 
                and input[i+directions[1][0][0]][j+directions[1][0][1]] == "S"):
                return 1
            

        if ((input[i+directions[1][0][0]][j+directions[1][0][1]] == "M" 
            and input[i+directions[1][1][0]][j+directions[1][1][1]] == "S")
            or (input[i+directions[1][1][0]][j+directions[1][1][1]] == "M" 
            and input[i+directions[1][0][0]][j+directions[1][0][1]] == "S")):
            if (input[i+directions[0][0][0]][j+directions[0][0][1]] == "M" 
                and input[i+directions[0][1][0]][j+directions[0][1][1]] == "S"):
                return 1
            
            if (input[i+directions[0][1][0]][j+directions[0][1][1]] == "M" 
                and input[i+directions[0][0][0]][j+directions[0][0][1]] == "S"):
                return 1
        return 0



Day()