from dataclasses import dataclass
from enum import Enum
from typing import Callable

NUM_DIMS = 2


class State(Enum):
    ALIVE = 1
    DEAD = 0


@dataclass(eq=True, frozen=True)
class Coordinate:
    x: int
    y: int


Grid = Callable[[Coordinate], State]

Rule = Callable[[Coordinate, Grid], State]


class Screen:
    def __init__(self, xrange: [int, int], yrange: [int, int]):
        self.xs = range(xrange[0], xrange[1] + 1)
        self.ys = sorted(range(yrange[0], yrange[1] + 1), reverse=True)
