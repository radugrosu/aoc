from collections import defaultdict
from typing import Sequence, Set


def read_input(path: str):
    inputs, outputs = [], []
    with open(path) as fh:
        for line in fh:
            if line:
                i, o = line.strip().split("|")
                inputs.append(list(map(set, i.strip().split())))
                outputs.append(o.strip().split())
    return inputs, outputs


def part_1(outputs: Sequence[Set[str]]) -> int:
    n = 0
    lengths = {2, 3, 4, 7}
    for output in outputs:
        for pattern in output:
            if len(pattern) in lengths:
                n += 1
    return n


D2P = {
    1: "cf",
    7: "acf",
    4: "bcdf",
    8: "abcdefg",
    0: "abcefg",
    2: "acdeg",
    3: "acdfg",
    5: "abdfg",
    6: "abdefg",
    9: "abcdfg"
}

TABLE = [[len(set(D2P[i]) - set(D2P[j])) for j in range(10)]
         for i in range(10)]


def decode(inputs: Sequence[Set[str]]) -> int:
    l2p = {}
    remaining_patterns = []
    for p in inputs:
        if len(p) in {2, 3, 4, 7}:
            l2p[len(p)] = p
        else:
            remaining_patterns.append(p)
    d2p = {
        1: l2p[2],
        7: l2p[3],
        4: l2p[4],
        8: l2p[7],
    }
    d2p[6] = [p for p in remaining_patterns if len(p - d2p[1]) == 5][0]
    remaining_patterns = [p for p in remaining_patterns if p != d2p[6]]
    d2p[3] = [p for p in remaining_patterns if len(p - d2p[1]) == 3][0]
    remaining_patterns = [p for p in remaining_patterns if p != d2p[3]]
    d2p[0] = [p for p in remaining_patterns if len(p - d2p[3]) == 2][0]
    remaining_patterns = [p for p in remaining_patterns if p != d2p[0]]
    d2p[9] = [p for p in remaining_patterns if len(p) == 6][0]
    remaining_patterns = [p for p in remaining_patterns if p != d2p[9]]
    d2p[5] = [p for p in remaining_patterns if len(p - d2p[9]) == 0][0]
    remaining_patterns = [p for p in remaining_patterns if p != d2p[5]]
    d2p[2] = remaining_patterns[0]
    return {"".join(sorted(p)): d for d, p in d2p.items()}


def part_2(inputs_outputs) -> int:
    total = 0
    for patterns, outputs in zip(*inputs_outputs):
        d2p = decode(patterns)
        total += int("".join(str(d2p["".join(sorted(output))]) for output in outputs))
    return total


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/8_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/8.txt")
assert part_1(test_inputs[1]) == 26
print(part_1(real_inputs[1]))

assert part_2(test_inputs) == 61229
print(part_2(real_inputs))
