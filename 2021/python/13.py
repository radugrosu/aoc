from typing import Sequence, Set, Tuple


def read_input(path: str):
    a, b = open(path).read().strip().split("\n\n")
    dots = {tuple(map(int, line.split(","))) for line in a.splitlines()}
    instructions = [line.split("=") for line in b.splitlines()]
    instructions = [(a[-1], int(b)) for a, b in instructions]
    return dots, instructions


Pos = Tuple[int, int]


def fold(dots: Set[Pos], instruction: Tuple[str, int]) -> Set[Pos]:
    kind, anchor = instruction
    dotlist = list(dots)
    for i, (x, y) in enumerate(dotlist):
        if kind == "x" and x > anchor:
            dotlist[i] = (2 * anchor - x, y)
        elif kind == "y" and y > anchor:
            dotlist[i] = (x, 2 * anchor - y)
    return set(dotlist)

def dots_repr(dots) -> str:
    m = max(dots, key=lambda x: x[0])[0] + 1
    n = max(dots, key=lambda x: x[1])[1] + 1
    empty = [["." for _ in range(m)] for _ in range(n)]
    for x, y in dots:
        empty[y][x] = "#"
    return "\n".join("".join(line) for line in empty)
    

def part_1(inputs) -> int:
    dots, instructions = inputs
    dots = fold(dots, instructions[0])
    return len(dots)

def part_2(inputs) -> int:
    dots, instructions = inputs
    for instruction in instructions:
        dots = fold(dots, instruction)
    return dots_repr(dots)

test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/13_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/13.txt")
assert part_1(test_inputs) == 17
print(part_1(real_inputs))
print(part_2(real_inputs))
