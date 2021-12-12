# https://adventofcode.com/2021/day/7
import re
from collections import Counter
from functools import reduce
from typing import Mapping, MutableMapping, Optional, Sequence, Set, Tuple


def read_input(path: str):
    with open(path) as fh:
        return [int(i) for i in fh.read().strip().split(",")]


def part_1(inputs: Sequence[int]):
    counter = Counter(inputs)
    uniques = sorted(counter)
    sums, counts = {}, {}
    for i, v in enumerate(uniques):
        if i > 0:
            v_prev = uniques[i - 1]
            sums[v] = sums[v_prev] + v * counter[v]
            counts[v] = counts[v_prev] + counter[v]
        else:
            sums[v] = v * counter[v]
            counts[v] = counter[v]
    total_sum = sum(inputs)
    total_counts = len(inputs)
    objective = {}
    for v in uniques:
        value = total_sum - 2 * sums[v] - (total_counts - 2 * counts[v]) * v
        objective[v] = value
    return min(objective.values())


def part_2(inputs: Sequence[int]):
    counter = Counter(inputs)
    uniques = sorted(counter)
    sums, counts = {}, {}
    for i, v in enumerate(uniques):
        if i > 0:
            v_prev = uniques[i - 1]
            sums[v] = sums[v_prev] + v * counter[v]
            counts[v] = counts[v_prev] + counter[v]
        else:
            sums[v] = v * counter[v]
            counts[v] = counter[v]
    total_sum = sum(inputs)
    total_sum_of_squares = sum(x**2 for x in inputs)
    total_counts = len(inputs)
    median = sorted(inputs)[total_counts // 2]
    mean = total_sum / total_counts
    if mean > median:
        mean = int(mean) + 1
    else:
        mean = int(mean)
        median = sorted(inputs)[total_counts // 2 + 1]

    objective = {}
    for n in range(min((mean, median)), max((mean, median)) + 1):
        if n in sums:
            v = n
        else:
            v = uniques[search_sorted(uniques, n) - 1]
        value = (total_sum - 2 * sums[v] - (total_counts - 2 * counts[v]) * n)
        value += total_sum_of_squares - 2 * n * total_sum + total_counts * n**2
        objective[n] = value // 2
    return min(objective.values())


def search_sorted(values: Sequence[int], v: int):
    if not values:
        return 0
    if v < values[0]:
        return 0
    if v > values[-1]:
        return len(values)

    l, h = 0, len(values) - 1
    while l < h:
        i = (l + h) // 2
        m = values[i]
        if v <= m:
            h = i
        else:
            l = i + 1
    return l


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/7_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/7.txt")
assert part_1(test_inputs) == 37
print(part_1(real_inputs))

assert part_2(test_inputs) == 168
print(part_2(real_inputs))
