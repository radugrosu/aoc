from collections import defaultdict
from typing import Sequence


def read_input(path: str):
    return [list(map(int, line.strip())) for line in open(path).readlines()]


def adj_map_from_list(inputs: Sequence[Sequence[int]]):
    assert inputs
    n, m = len(inputs), len(inputs[0])
    out = defaultdict(list)
    for y in range(n):
        for x in range(m):
            neighbourhood = out[y, x]
            neighbours = set()
            neighbouring_positions = []
            for dy, dx in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    neighbours.add(inputs[y + dy][x + dx])
                    neighbouring_positions.append((y + dy, x + dx))
            neighbourhood.append(inputs[y][x])
            neighbourhood.append(neighbours)
            neighbourhood.append(neighbouring_positions)
    return dict(out)


def part_1(inputs: Sequence[Sequence[int]]):
    adj_map = adj_map_from_list(inputs)
    total = 0
    for value, neighbours, _ in adj_map.values():
        if value < min(neighbours):
            total += value + 1
    return total


def part_2(inputs: Sequence[Sequence[int]]):
    adj_map = adj_map_from_list(inputs)
    low_points = []
    for pos, (height, neighbour_heights,
              neighbour_positions) in adj_map.items():
        if height < min(neighbour_heights):
            low_points.append(pos)

    basins = []
    for pos in low_points:
        to_visit = set([pos])
        current_basin = set()
        visited = set()
        while to_visit:
            pos = to_visit.pop()
            height, neighbour_heights, neighbour_positions = adj_map[pos]
            if height < 9:
                current_basin.add(pos)
                for pos in neighbour_positions:
                    if pos not in visited:
                        to_visit.add(pos)
                        visited.add(pos)
        basins.append(current_basin)
    sizes = sorted(len(basin) for basin in basins)
    return sizes[-3] * sizes[-2] * sizes[-1]


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/9_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/9.txt")
assert part_1(test_inputs) == 15
print(part_1(real_inputs))
assert part_2(test_inputs) == 1134
print(part_2(real_inputs))
