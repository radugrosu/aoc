# https://adventofcode.com/2021/day/4
from collections import defaultdict
from typing import Mapping, MutableMapping, Optional, Sequence, Set, Tuple

import attr

Input = Sequence[int]
Pos = Tuple[int, int]


@attr.s(auto_attribs=True, auto_detect=True)
class Board:
    board: Sequence[Sequence[int]]
    marked: Set = attr.ib(factory=set)
    row_indexes: Mapping[int, Sequence[int]] = attr.ib(factory=lambda: defaultdict(list))
    col_indexes: Mapping[int, Sequence[int]] = attr.ib(factory=lambda: defaultdict(list))

    def find_in_board(self, number: int) -> Optional[Pos]:
        for r, row in enumerate(self.board):
            for c, value in enumerate(row):
                if value == number:
                    return r, c

    def mark(self, number: int) -> Optional[Pos]:
        found = self.find_in_board(number)
        if found:
            r, c = found
            self.marked.add(number)
            self.row_indexes[r].append(c)
            self.col_indexes[c].append(r)
            return r, c

    @property
    def bingo(self) -> bool:
        for values in self.row_indexes.values():
            if len(values) == len(self.board):
                return True
        for values in self.col_indexes.values():
            if len(values) == len(self.board):
                return True
        return False

    def score(self, number: int):
        out = 0
        for row in self.board:
            for value in row:
                if value not in self.marked:
                    out += value
        return out * number


def read_input(path: str) -> Tuple[Input, Sequence[Board]]:
    with open(path) as fh:
        numbers = [int(n) for n in fh.readline().strip().split(",")]
        boards = []
        current_board = []
        for line in fh:
            if not line.strip():
                if current_board:
                    assert len(current_board) == 5
                    boards.append(current_board)
                    current_board = []
            else:
                row = [int(n) for n in line.strip().split()]
                current_board.append(row)
        if current_board:
            assert len(current_board) == 5
            boards.append(current_board)
        return numbers, boards


def part_1(inputs: Tuple[Input, Sequence[Sequence[int]]]) -> int:
    numbers, boards = inputs
    boards = [Board(b) for b in boards]
    for number in numbers:
        for board in boards:
            if board.mark(number):
                if board.bingo:
                    return board.score(number)
    raise ValueError("One board is supposed to win..")

def part_2(inputs: Tuple[Input, Sequence[Sequence[int]]]) -> int:
    numbers, boards = inputs
    boards = [Board(b) for b in boards]
    done = set()
    for number in numbers:
        for i, board in enumerate(boards):
            if board.mark(number):
                if board.bingo:
                    done.add(i)
                    if len(done) == len(boards):
                        return board.score(number)
    raise ValueError("One board is supposed to win..")

test_inputs = read_input("/home/radu/repos/aoc/2021/inputs/4_test.txt")
real_inputs = read_input("/home/radu/repos/aoc/2021/inputs/4.txt")

assert part_1(test_inputs) == 4512
print(part_1(real_inputs))

assert part_2(test_inputs) == 1924
print(part_2(real_inputs))
