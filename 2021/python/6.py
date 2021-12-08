# https://adventofcode.com/2021/day/6
import re
from collections import defaultdict
from typing import Mapping, MutableMapping, Optional, Sequence, Set, Tuple
from functools import lru_cache


def read_input(path: str):
    with open(path) as fh:
        return [int(i) for i in fh.read().strip().split(",")]


def part_1(inputs, evolve_for: int = 80):
    fish = [*inputs]
    for _ in range(evolve_for):
        for i in range(len(fish)):
            f = fish[i]
            if f == 0:
                fish.append(8)
            if f == 8:
                fish[i] = 7
            else:
                fish[i] = (f - 1) % 7
    return len(fish)


@lru_cache(None)
def fish_evolution(initial_age: int, evolve_for: int) -> int:
    if evolve_for == 0:
        return 1
    if initial_age == 0:
        return fish_evolution(6, evolve_for - 1) + fish_evolution(8, evolve_for - 1)
    else:
        return fish_evolution(initial_age - 1, evolve_for - 1)


def fish_evolution_cached(initial_age: int, evolve_for: int) -> int:
    cache = {(i, 0): 1 for i in range(9)}
    for d in range(1, evolve_for + 1):
        for a in range(9):
            if a == 0:
                cache[a, d] = cache[6, d - 1] + cache[8, d - 1]
            else:
                cache[a, d] = cache[a - 1, d - 1]
    return cache[initial_age, evolve_for]


def part_1(inputs, evolve_for: int = 80):
    return sum(fish_evolution(i, evolve_for) for i in inputs)


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/6_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/6.txt")
assert part_1(test_inputs, 18) == 26
assert part_1(test_inputs, 80) == 5934
assert part_1(test_inputs, 256) == 26984457539

print(part_1(real_inputs, 80))
print(part_1(real_inputs, 256))
