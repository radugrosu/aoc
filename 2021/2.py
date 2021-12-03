# https://adventofcode.com/2021/day/2
from typing import Sequence, List
from util import read_input

test_inputs = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip().splitlines()


def process_inputs(inputs: Sequence[str]) -> Sequence[List]:
    out = []
    for line in inputs:
        dir, value = line.strip().split()
        out.append([dir, int(value)])
    return out


test_inputs = process_inputs(test_inputs)


def part_1(inputs: Sequence[int]) -> Sequence[int]:
    pos = [0, 0]
    for dir, value in inputs:
        if dir == "forward":
            index = 0
        elif dir == "down":
            index = 1
        elif dir == "up":
            index = 1
            value *= -1
        else:
            raise ValueError(f"Unexpected direction {dir}")
        pos[index] += value
    return pos


assert part_1(test_inputs) == [15, 10]

inputs = process_inputs(read_input("./inputs/2.txt"))
print(part_1(inputs))


def part_2(inputs: Sequence[int]) -> Sequence[int]:
    pos = [0, 0]  # horizontal, depth
    aim = 0
    for dir, value in inputs:
        if dir == "down":
            aim += value
            continue
        if dir == "up":
            aim -= value
            continue
        pos[0] += value
        pos[1] += aim * value
    return pos


assert part_2(test_inputs) == [15, 60]
print(part_2(inputs))
