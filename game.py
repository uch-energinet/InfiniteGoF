import time
from functools import lru_cache

import visualize
from models import Coordinate, Grid, Rule, Screen, State


def evolve_grid(grid: Grid, rule: Rule) -> Grid:
    @lru_cache
    def evolved_grid(coord: Coordinate) -> State:
        return rule(coord, grid)

    return evolved_grid


def run(rule: Rule, grid: Grid, screen: Screen, tmax: int):
    for t in range(0, tmax + 1):
        visualize.print_grid(grid, screen, t)
        grid = evolve_grid(grid, rule)
        time.sleep(1)
