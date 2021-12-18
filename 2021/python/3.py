# https://adventofcode.com/2021/day/2
from typing import Sequence
from collections import Counter
from util import read_input


def most_common(items: Sequence[str]) -> str:
    counts = Counter(items)
    return "1" if counts["1"] >= counts["0"] else "0"


def least_common(items: Sequence[str]) -> str:
    counts = Counter(items)
    return "1" if counts["1"] < counts["0"] else "0"


def int_from_byte_list(items: Sequence[int]) -> int:
    return int("".join(items), 2)


def part_1(inputs: Sequence[str]) -> int:
    inputs = [list(line.strip()) for line in inputs]
    transposed = list(zip(*inputs))
    gamma = [most_common(col) for col in transposed]
    epsilon = [least_common(col) for col in transposed]
    gamma = int_from_byte_list(gamma)
    epsilon = int_from_byte_list(epsilon)
    return gamma * epsilon


def part_1_alt(inputs: Sequence[str]) -> int:
    inputs = [list(map(int, line.strip())) for line in inputs]
    transposed = list(zip(*inputs))
    n, m = len(inputs), len(transposed)
    sums = [sum(col) for col in transposed]
    gamma = [1 if s > n / 2 else 0 for s, col in zip(sums, transposed)]
    epsilon = [0 if s > n / 2 else 1 for s, col in zip(sums, transposed)]
    gamma = sum(c * 2 ** i for c, i in zip(gamma, reversed(range(m))))
    epsilon = sum(c * 2 ** i for c, i in zip(epsilon, reversed(range(m))))
    return gamma * epsilon


def part_2(inputs: Sequence[str]) -> int:
    inputs = [list(line.strip()) for line in inputs]
    oxygen_inputs = [*inputs]
    co2_inputs = [*inputs]
    for col in range(len(inputs[0])):
        mc = most_common(line[col] for line in oxygen_inputs)
        oxygen_inputs = [line for line in oxygen_inputs if line[col] == mc]
        if len(oxygen_inputs) == 1:
            break
    else:
        raise ValueError("Too many rows left for oxygen")
    for col in range(len(inputs[0])):
        mc = least_common(line[col] for line in co2_inputs)
        co2_inputs = [line for line in co2_inputs if line[col] == mc]
        if len(co2_inputs) == 1:
            break
    else:
        raise ValueError("Too many rows left for co2")

    oxygen = int_from_byte_list(oxygen_inputs[0])
    co2 = int_from_byte_list(co2_inputs[0])
    return oxygen * co2


test_inputs = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip().splitlines()
inputs = read_input("../inputs/3.txt")

assert part_1(test_inputs) == 198
print(part_1(inputs))
print(part_1_alt(inputs))

assert part_2(test_inputs) == 230
print(part_2(inputs))
