# https://adventofcode.com/2021/day/5
import re
from collections import defaultdict
from typing import Mapping, MutableMapping, Optional, Sequence, Set, Tuple


def read_input(path: str):
    with open(path) as fh:
        return [re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line).groups() for line in fh.readlines()]


def read_input(path: str):
    out = []
    with open(path) as fh:
        for line in fh:
            if line:
                current = []
                for part in line.strip().split("->"):
                    x, y = part.split(",")
                    current.extend([x, y])
                out.append(current)
    return out


def part_1(inputs):
    board = defaultdict(int)
    for line in inputs:
        x1, y1, x2, y2 = map(int, line)
        if x1 == x2:
            y1, y2 = sorted((y1, y2))
            for i in range(y1, y2 + 1):
                board[x1, i] += 1
        elif y1 == y2:
            x1, x2 = sorted((x1, x2))
            for i in range(x1, x2 + 1):
                board[i, y1] += 1
        else:
            pass
    return sum(1 for v in board.values() if v > 1)


def range_inclusive(a: int, b: int):
    if a < b:
        return range(a, b + 1)
    else:
        return reversed(range(b, a + 1))


def part_2(inputs):
    board = defaultdict(int)
    for line in inputs:
        x1, y1, x2, y2 = map(int, line)
        if x1 == x2:
            for i in range_inclusive(y1, y2):
                board[x1, i] += 1
        elif y1 == y2:
            for i in range_inclusive(x1, x2):
                board[i, y1] += 1
        else:
            for i, j in zip(range_inclusive(x1, x2), range_inclusive(y1, y2)):
                board[i, j] += 1
    return sum(1 for v in board.values() if v > 1)


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/5_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/5.txt")
assert part_1(test_inputs) == 5
print(part_1(real_inputs))

assert part_2(test_inputs) == 12
print(part_2(real_inputs))
