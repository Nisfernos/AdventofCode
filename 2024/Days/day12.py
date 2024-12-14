from Utils.Day import DayFormat


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 12)

    def part_one(self):
        # self.input = self.test_input

        self.height = len(self.input)
        self.width = len(self.input[0])
        self.cards = ((-1,0), (0,1), (1,0), (0,-1))
        
        fences = [[0 for a in range(self.width)] for b in range(self.height)]
        for i,row in enumerate(self.input):
            for j,val in enumerate(row):
                nbs = self.get_neighbours((i,j))
                fence_count = 4
                for dir in nbs:
                    if self.input[i+dir[0]][j+dir[1]] == val:
                        fence_count -= 1
                fences[i][j] = fence_count

        visited_squares = set()
        result = 0
        for i,row in enumerate(self.input):
            for j,val in enumerate(row):
                if (i,j) in  visited_squares:
                    continue
                polygon = set()
                to_eval = [(i,j)]
                perimeter = 0
                while (to_eval):
                    ci,cj = to_eval.pop()
                    perimeter += fences[ci][cj]
                    polygon.add((ci,cj))
                    visited_squares.add((ci,cj))
                    for nb in self.get_neighbours((ci,cj)):
                        nbi, nbj = ci+nb[0], cj+nb[1]
                        if (nbi, nbj) in polygon or (nbi, nbj) in visited_squares or (nbi, nbj) in to_eval:
                            continue
                        elif self.input[nbi][nbj] == val:
                            to_eval.append((nbi, nbj))
                result += perimeter * len(polygon)

        print(result)

    def get_neighbours(self, pos):
        neighbours = []
        for dir in self.cards:
            if 0 <= pos[0]+dir[0] < self.height and 0 <= pos[1]+dir[1] < self.width:
                neighbours.append(dir)
        return neighbours

    def part_two(self):
        # self.input = self.restore
        # self.input = self.test_input

        self.height = len(self.input)
        self.width = len(self.input[0])
        self.cards = ((-1,0), (0,1), (1,0), (0,-1))
        
        self.fences = {(i,j):[] for i in range(self.height) for j in range(self.width)}
        for i,row in enumerate(self.input):
            for j,val in enumerate(row):
                nbs = self.get_neighbours((i,j))
                for dir in nbs:
                    if self.input[i+dir[0]][j+dir[1]] == val:
                        continue
                    match dir:
                        case (-1,0):    # up
                            self.fences[(i,j)].append(("h", i, j))
                        case (0,1):     # right
                            self.fences[(i,j)].append(("v", j+1, i))
                        case (1,0):     # down
                            self.fences[(i,j)].append(("h", i+1, j))
                        case (0,-1):    # left
                            self.fences[(i,j)].append(("v", j, i))
                for cdir in self.cards:
                    if cdir not in nbs:
                        match cdir:
                            case (-1,0):    # up
                                self.fences[(i,j)].append(("h", i, j))
                            case (0,1):     # right
                                self.fences[(i,j)].append(("v", j+1, i))
                            case (1,0):     # down
                                self.fences[(i,j)].append(("h", i+1, j))
                            case (0,-1):    # left
                                self.fences[(i,j)].append(("v", j, i))

        visited_squares = set()
        result = 0
        for i,row in enumerate(self.input):
            for j,val in enumerate(row):
                if (i,j) in  visited_squares:
                    continue
                polygon = set()
                to_eval = [(i,j)]
                while (to_eval):
                    ci,cj = to_eval.pop()
                    polygon.add((ci,cj))
                    visited_squares.add((ci,cj))
                    for nb in self.get_neighbours((ci,cj)):
                        nbi, nbj = ci+nb[0], cj+nb[1]
                        if (nbi, nbj) in polygon or (nbi, nbj) in visited_squares or (nbi, nbj) in to_eval:
                            continue
                        elif self.input[nbi][nbj] == val:
                            to_eval.append((nbi, nbj))
                result += self.unique_edges(polygon, val)

        print(result)

    def unique_edges(self, polygon, symbol):
        unedge = 0
        # All ('x', x, x) in polygon
        edges = {value for key,values in self.fences.items() for value in values if key in polygon}
        for dir in ["h", "v"]:
            # All horizontal/vertical line coords
            lines = {val[1] for val in edges if val[0] == dir}
            for line in sorted(lines):
                # All coords in 1 line
                coords = sorted([val[2] for val in edges if val[0] == dir and val[1] == line])
                lcoord = coords[0]
                unedge += 1
                if (line < self.width and dir == "v"):
                    is_sym = self.input[coords[0]][line] == symbol
                elif (line < self.height and dir == "h"):
                    is_sym = self.input[line][coords[0]] == symbol
                for coord in coords[1:]:
                    # If not consecutive
                    if not coord == lcoord+1:
                        unedge += 1
                        if (line < self.width and dir == "v"):
                            is_sym = self.input[coord][line] == symbol
                        if (line < self.height and dir == "h"):
                            is_sym = self.input[line][coord] == symbol
                    elif dir == "h" and line < self.height and ((self.input[line][coord] == symbol) != is_sym):
                        unedge += 1
                        is_sym = self.input[line][coord] == symbol
                    elif dir == "v" and line < self.width and ((self.input[coord][line] == symbol) != is_sym):
                        unedge += 1
                        is_sym = self.input[coord][line] == symbol
                    lcoord = coord
        return unedge * len(polygon)

        

Day()