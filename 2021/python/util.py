from typing import Sequence, Union
from pathlib import Path

PathLike = Union[str, Path]


def read_input(path: PathLike) -> Sequence[str]:
    with open(path, "r") as f:
        return f.readlines()
