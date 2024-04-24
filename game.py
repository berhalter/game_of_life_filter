#!/usr/bin/python3

import numpy as np
import sys

live = 1
dead = 0

"""
 *** GAME OF LIFE RULES ***
 * Any live cell with fewer than two live neighbors dies, as if by underpopulation.
 * Any live cell with two or three live neighbors lives on to the next generation.
 * Any live cell with more than three live neighbors dies, as if by overpopulation.
 * Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""

# Prints full grid to terminal, followed by a newline character
def print_grid(grid):
    for row in grid:
        for col in row:
            sys.stdout.write(str(col))
        print()

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        num_gens = sys.argv[2]
        mode = sys.argv[3]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <filename> <# of generations> <padding mode>")
    

    # width = 80
    # height = 24
    # grid = np.zeros((height, width), int)
    # print("init:")
    # print_grid(grid)

    grid = np.loadtxt(filename, dtype=int)
    print("\nparsed input:")
    print_grid(grid)


    """
    set border mode:
    this determines how neighbors are counted for cells at the edge of the grid.
    'live' mode counts cells outside of the grid as live
    'dead' mode counts cells outside of the grid as dead
    'wrap' mode counts cells outside of the grid as the value of the cells on the opposite side
    'copy' mode counts cells outside of the grid as the same value as the cells on that edge 
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
            raise ValueError("Invalid border mode. Valid inputs: \n" + 
                             "'live' - grid border is padded with live cells\n" +
                             "'dead' - grid is padded with dead cells\n" +
                             "'wrap' - grid is padded with cells from the opposite side\n" +
                             "'copy' - grid is padded with a copy of the adjacent cell")
