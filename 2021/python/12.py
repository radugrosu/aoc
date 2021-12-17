from collections import Counter, defaultdict
from typing import Mapping, Sequence, Set


def read_input(path: str):
    edges = [line.strip().split("-") for line in open(path).readlines()]
    graph = defaultdict(set)
    for (s, e) in edges:
        graph[s].add(e)
        graph[e].add(s)
    return dict(graph)


def part_1(graph: Mapping[str, Set[str]]) -> int:
    to_develop = [["start"]]
    done = []
    while to_develop:
        path = to_develop.pop()
        for neighbour in graph[path[-1]]:
            if neighbour.isupper() or neighbour not in path:
                new_path = [*path, neighbour]
                if neighbour == "end":
                    done.append(new_path)
                else:
                    to_develop.append(new_path)
    return len(done)


def admits_minor(path: Sequence[str]) -> bool:
    counts = Counter(p for p in path if p.islower())
    return max(counts.values()) < 2


def part_2(graph: Mapping[str, Set[str]]) -> int:
    to_develop = [["start"]]
    done = []
    while to_develop:
        path = to_develop.pop()
        for neighbour in graph[path[-1]]:
            if neighbour != "start":
                if neighbour.isupper() or neighbour not in path or admits_minor(path):
                    new_path = [*path, neighbour]
                    if neighbour == "end":
                        done.append(new_path)
                    else:
                        to_develop.append(new_path)
    return len(done)


test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/12_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/12.txt")
assert part_1(test_inputs) == 10
print(part_1(real_inputs))
assert part_2(test_inputs) == 36
print(part_2(real_inputs))
