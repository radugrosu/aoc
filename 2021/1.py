# https://adventofcode.com/2021/day/1
from typing import Sequence
from util import read_input

test_inputs = """
199
200
208
210
200
207
240
269
260
263""".strip().splitlines()

test_inputs = [int(item.strip()) for item in test_inputs]
inputs = [int(item) for item in read_input("./inputs/1.txt")]


def part_1(inputs: Sequence[int]) -> int:
    num_larger = 0
    for i in range(1, len(inputs)):
        if inputs[i] > inputs[i - 1]:
            num_larger += 1
    return num_larger


assert part_1(test_inputs) == 7


def part_2(inputs: Sequence[int]) -> int:
    """3-sized window"""
    num_larger = 0
    for i in range(4, len(inputs) + 1):
        if sum(inputs[i - 4 : i - 1]) < sum(inputs[i - 3 : i]):
            num_larger += 1
    return num_larger


assert part_2(test_inputs) == 5
