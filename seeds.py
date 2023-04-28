from models import Coordinate, Grid, State


def switch_state(state: State) -> State:
    if state == State.ALIVE:
        return State.DEAD
    else:
        return State.ALIVE


def grid_from_finite_list(
    coords: list[Coordinate],
    state: State = State.ALIVE,
) -> Grid:
    def grid(coord: Coordinate) -> State:
        if coord in coords:
            return state
        else:
            return switch_state(state)

    return grid


def checker_grid(state_at_origin: State = State.ALIVE) -> Grid:
    def grid(coord: Coordinate) -> State:
        if (coord.x + coord.y) % 2 == 0:
            return state_at_origin
        else:
            return switch_state(state_at_origin)

    return grid
