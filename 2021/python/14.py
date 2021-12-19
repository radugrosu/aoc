from collections import Counter, defaultdict
from itertools import zip_longest
from typing import Mapping


def read_input(path: str):
    elements, rules = open(path).read().strip().split("\n\n")
    rules = dict(rule.split(" -> ") for rule in rules.splitlines())
    return elements, rules


def grow(elements: str, rules: Mapping[str, str], steps: int):
    for _ in range(steps):
        new = []
        for i in range(len(elements) - 1):
            new.append(rules[elements[i:i + 2]])
        elements = "".join(i for pair in zip_longest(elements, new)
                           for i in pair if i)
    return elements


def grow_2(elements: str, rules: Mapping[str, str], steps: int):
    counts = Counter(elements[i:i + 2] for i in range(len(elements) - 1))
    last_element = elements[-1]
    for _ in range(steps):
        new_counts = defaultdict(int)
        for pair, count in counts.items():
            produced = rules[pair]
            new_counts[f"{pair[0]}{produced}"] += count
            new_counts[f"{produced}{pair[1]}"] += count
        counts = new_counts
    elements = defaultdict(int)
    for key, count in counts.items():
        elements[key[0]] += count
    elements[last_element] += 1
    values = sorted(elements.values())
    return values[-1] - values[0]


def part_1(inputs):
    elements = grow(*inputs, 10)
    counts = sorted(Counter(elements).values())
    return counts[-1] - counts[0]


def part_2(inputs):
    return grow_2(*inputs, 40)


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/14_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/14.txt")
assert part_1(test_inputs) == 1588
print(part_1(real_inputs))
assert part_2(test_inputs) == 2188189693529
print(part_2(real_inputs))
