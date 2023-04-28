from models import Coordinate, Grid, State


def _num_alive_neighbours(coord: Coordinate, grid: Grid) -> int:
    n = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            neighbour = Coordinate(coord.x + dx, coord.y + dy)

            if coord == neighbour:
                continue

            if grid(neighbour) == State.ALIVE:
                n += 1
    return n


def conway(coord: Coordinate, grid: Grid) -> State:
    n = _num_alive_neighbours(coord, grid)
    state = grid(coord)
    if state == State.ALIVE:
        if n < 2:
            return State.DEAD
        if n in [2, 3]:
            return State.ALIVE
        else:
            return State.DEAD
    else:
        if n == 3:
            return State.ALIVE
        else:
            return State.DEAD
