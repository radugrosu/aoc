from typing import Sequence


def read_input(path: str):
    return [line.strip() for line in open(path).readlines() if line.strip()]


def score_corrupted_line(line: str) -> int:
    stack = []
    match_map = {"(": ")", "<": ">", "[": "]", "{": "}"}
    for c in line:
        if c in {"(", "[", "{", "<"}:
            stack.append(c)
        else:
            matching = stack.pop()
            if match_map[matching] != c:
                return c


def part_1(input: Sequence[str]):
    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in input:
        c = score_corrupted_line(line)
        if c is not None:
            score += score_map[c]
    return score


def complete_line(line: str):
    stack = []
    match_map = {"(": ")", "<": ">", "[": "]", "{": "}"}
    for c in line:
        if c in {"(", "[", "{", "<"}:
            stack.append(c)
        else:
            matching = stack.pop()
            if match_map[matching] != c:
                return
    return [match_map[i] for i in reversed(stack)]


def score_completed_line(chars: str):
    score_map = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for c in chars:
        score = 5 * score + score_map[c]
    return score


def part_2(input: Sequence[str]):
    scores = []
    for line in input:
        chars = complete_line(line)
        if chars is not None:
            scores.append(score_completed_line(chars))
    print(sorted(scores))
    return sorted(scores)[len(scores) // 2]


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/10_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/10.txt")
assert part_1(test_inputs) == 26397
print(part_1(real_inputs))
# assert part_2(test_inputs) == 288957
print(part_2(real_inputs))
