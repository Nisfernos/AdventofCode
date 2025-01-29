from Utils.Day import DayFormat


class DijkstraTurn():
    def __init__(self, grid) -> None:
        self.cards = ["N", "E", "S", "W"]
        self.dirs = ((-1,0), (0,1), (1,0), (0,-1))
        self.nodes = []
        self.grid = grid
        self.construct_dijkstra()
        self.start_direction = "E"
        self.start = [node for node in self.nodes if node.start][0]
        self.end =   [node for node in self.nodes if node.end][0]

    def construct_dijkstra(self):
        self.visited_squares = []
        start = [(i,j) for i,row in enumerate(self.grid) for j,val in enumerate(row) if val=="S"][0]
        start_node = Node(start=True)
        self.nodes[start] = start_node
        for nb in self.get_neighbours(start):
            self.connect_dijkstra(nb, start_node, 0)

    def connect_dijkstra(self, coords, last_node, path_len):
        nbs = self.get_neighbours(coords)
        if len(nbs) > 2:
            new_node = Node()
            last_node.neighbours[coords] = new_node
            new_node.neighbours[coords] = last_node
            
            last_node = new_node
            path_len = 0
        for nb in [nnb for nnb in nbs if nnb not in self.visited_squares]:
            #TODO: dir
            self.connect_dijkstra(nb, last_node, path_len+1000*self.dirs.index(dir))

    def get_neighbours(self, coords, pc="."):
        nbs = []
        for dir in self.dirs:
            if self.grid[coords[0]+dir[0]][coords[1]+dir[1]] in ".E":
                nbs.append((coords[0]+dir[0],coords[1]+dir[1]))
        return nbs

    def solve(self):
        pass
                

class Node():
    def __init__(self, start=False, end=False) -> None:
        self.start = start
        self.end = end
        self.distance = {"N": -1, "E": -1, "S": -1, "W": -1}
        self.neighbours = {}


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 16)

    def part_one(self):
        # Make graph: Every direction with path is a seperate node; only nodes at crossroads and begin and end; shortest distance first; calculate length between nodes by usig graph
        self.input = self.test_input

        grid = DijkstraTurn(self.input)
        grid.solve()

        result = min([val for val in grid.end.distance.values() if val != -1])

        print(result)


    def part_two(self):
        self.input = self.restore
        self.input = self.test_input

Day()