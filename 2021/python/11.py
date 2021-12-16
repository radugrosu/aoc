from typing import List
from copy import deepcopy


def read_input(path: str):
    return [list(map(int, line.strip())) for line in open(path).readlines()]


NEIGHBOURS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1),
              (-1, -1)]


def repr(table) -> str:
    return "\n".join("".join(map(str, line)) for line in table)


def step(table: List[List[int]]) -> int:
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] += 1
    to_visit = {(x, y) for x in range(len(table)) for y in range(len(table[0]))
                if table[x][y] > 9}
    if to_visit:
        flashed = set()
        while to_visit:
            pos = x, y = to_visit.pop()
            flashed.add(pos)
            for dx, dy in NEIGHBOURS:
                nx, ny = x + dx, y + dy
                if (0 <= nx < len(table)) & (0 <= ny < len(table[0])):
                    table[nx][ny] += 1
                    if (nx, ny) not in flashed and table[nx][ny] > 9:
                        to_visit.add((nx, ny))
        for x, y in flashed:
            table[x][y] = 0
        return len(flashed)
    else:
        return 0

def part_1(inputs: List[List[int]], steps: int = 100) -> int:
    flashes = 0
    for _ in range(steps):
        flashes += step(inputs)
    return flashes

def part_2(inputs: List[List[int]], steps: int = 100) -> int:
    n = len(inputs) * len(inputs[0])
    for i in range(1, steps + 1):
        if step(inputs) == n:
            return i
    raise ValueError("Should be synchronized by this step")


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/11_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/11.txt")
assert part_1(deepcopy(test_inputs)) == 1656
print(part_1(deepcopy(real_inputs)))
assert part_2(test_inputs, 195) == 195
print(part_2(real_inputs, 1000))
