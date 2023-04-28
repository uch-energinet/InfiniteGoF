import game
import rules
import seeds
from models import Coordinate, Screen

if __name__ == "__main__":

    # 1. define a seed grid
    grid = seeds.grid_from_finite_list(
        coords=[
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(0, 1),
            Coordinate(2, 2),
            Coordinate(2, 4),
        ]
    )
    # 2. define a rule
    rule = rules.conway
    # 3. define the screen to print
    screen = Screen([0, 5], [0, 5])
    # 4. run game
    game.run(rule, grid, screen, tmax=5)
