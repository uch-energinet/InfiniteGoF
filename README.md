# Conway's Infinite Game of Life

This is an implementation of Conway's game of life on an infinite grid.

1. The game starts with an infinite grid, where each cell is defined to be either *alive*  or *dead* (this starting configuration of the grid is called a *seed*).
2. A rule is then applied to each cell (Conway's rule is one example), which tells what that cell's state should be in the next round.
3. The game continues for as long as you want.


## Concepts

A **grid** is a function, which for each cell returns the state of that cell.
```
grid : Cell -> State
```

A **rule** is a function, which for each cells, and a particular grid, returns a potentially new state of that cell.

```
rule : (Cell, Grid) -> State
```

In each round, a new grid is formed, by applying the rule to the current grid:

```
new_grid(cell) = rule(cell, grid)
```

## Example

To see an example, run

```python
python example.py
```