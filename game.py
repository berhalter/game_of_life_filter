#!/usr/bin/python3

import numpy as np
import sys

live = 1
dead = 0

def print_grid(grid):
    """Prints full grid to terminal, followed by a newline character."""
    for row in grid:
        for col in row:
            sys.stdout.write(str(col))
        print()



def pad_grid(grid, mode):
    """ Pad the border of a grid depending on the border mode (see below).
    Return the padded grid. 

    Valid modes:
     - 'live' counts cells outside of the grid as live.
     - 'dead' counts cells outside of the grid as dead.
     - 'wrap' counts cells outside of the grid as the value of the cells on the opposite side.
     - 'copy' counts cells outside of the grid as the same value as the cells on that edge.
    """
    match mode:
        case "live":
            grid = np.pad(grid, 1, mode="constant", constant_values=1)
            print("\nlive")
            print_grid(grid)
        case "dead":
            grid = np.pad(grid, 1, mode="constant", constant_values=0)
            print("\ndead")
            print_grid(grid)
        case "wrap":
            grid = np.pad(grid, 1, mode="wrap")
            print("\nwrap")
            print_grid(grid)
        case "copy":
            grid = np.pad(grid, 1, mode="symmetric")
            print("\ncopy")
            print_grid(grid)
        case _:
            raise ValueError("Invalid border mode. Valid modes: live | dead | wrap | copy")


def count_neighbors(grid):
    """Return the number of live neighbors for the cell at the given position in the grid."""
    pass

def compute_next_gen(grid):
    """Compute the next state for each non-border cell of the input grid based on its number of live neighbors.
    Return the newly calculated grid.

    *** GAME OF LIFE RULES ***
    * Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    * Any live cell with two or three live neighbors lives on to the next generation.
    * Any live cell with more than three live neighbors dies, as if by overpopulation.
    * Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    """
    pass

def run_game(grid, num_gens):
    """Plays game for given number of generations.
    Prints output of each generation to terminal."""
    pass


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        num_gens = sys.argv[2]
        mode = sys.argv[3]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <filename> <# of generations> <padding mode>")
    
    grid = np.loadtxt(filename, dtype=int)
    print("\nparsed input:")
    print_grid(grid)

    grid = pad_grid(grid, mode)