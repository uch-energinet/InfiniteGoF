from models import Coordinate, Grid, Screen, State


def print_grid(grid: Grid, screen: Screen, t: int = 0):
    # clear screen
    if t > 0:
        for _ in range(len(screen.ys) + 1):
            print("\x1b[1A\x1b[2K", end="")
    # print grid
    print(f"Iteration: t = {t}")
    for y in screen.ys:
        line = ""
        for x in screen.xs:
            state = grid(Coordinate(x, y))
            if state == State.ALIVE:
                line += "■"
            else:
                line += "□"
            line += " "
        print(line)
