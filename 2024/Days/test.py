# import copy

# def next_move(position, direction):
#     return position[0] + direction[0], position[1] + direction[1]

# def part_two():
#     with open("2024\\Input\\day06.txt") as txt:
#         input_grid = [list(row) for row in txt.read().splitlines()]

#     for i, row in enumerate(input_grid):
#         if "^" in row:
#             start_position = i, row.index("^")
#             break

#     directions = [(-1,0), (0,1), (1,0), (0,-1)]
#     start_direction = directions[0]

#     possible_barriers = set()

#     direction = start_direction
#     position = start_position
#     next_position = next_move(position, direction)

#     while (0 <= next_position[0] < len(input_grid) and 0 <= next_position[1] < len(input_grid[0])):
#         if input_grid[next_position[0]][next_position[1]] == "." and position != start_position:
#             possible_barriers.add(next_position)
#         if input_grid[next_position[0]][next_position[1]] == "#":
#             direction = directions[(directions.index(direction) + 1) % len(directions)]
#         else:
#             position = next_position
#         next_position = next_move(position, direction)

#     valid_barriers = []
#     for barrier in possible_barriers:
#         modified_grid = copy.deepcopy(input_grid)
#         modified_grid[barrier[0]][barrier[1]] = "#"

#         if check_if_loop(modified_grid, start_position, start_direction, directions):
#             valid_barriers.append(barrier)

#     result = len(valid_barriers)
#     print(result)

# def check_if_loop(input, position, direction, directions):
#     visited_states = set()
#     next_position = next_move(position, direction)
#     while (0 <= next_position[0] < len(input) and 0 <= next_position[1] < len(input[0])):
#         state = (position, direction)

#         if input[next_position[0]][next_position[1]] == "#":
#             if state in visited_states:
#                 return True
#             visited_states.add(state)
#             direction = directions[(directions.index(direction) + 1) % len(directions)]
#         else:
#             position = next_position
#         next_position = next_move(position, direction)
#     return False

# part_two()

# a = ""
# a += "1" * 9
# print(a)
# import re
# a = "12345..6...798"
# b = a.index("...")
# a = a.replace("6", "99", 1)
# a = a[:b] + a[b:].replace(".", "0", 3)
# print(b)
# print(a)

# Example: Using update
# set_of_tuples = {(1, 2)}
# new_tuples = set()

# # Update the set with new tuples
# set_of_tuples.update(new_tuples)
# print(set_of_tuples)

print([x for x in [-1,-2,-3,0] if x not in [0,1]])
