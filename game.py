#!/usr/bin/python3

import numpy as np
import sys

live = 1
dead = 0

def print_grid(grid):
    """Prints full grid to terminal, followed by a newline character."""
    for row in grid:
        for col in row:
            if col == live:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        print()



def pad_grid(grid, pad_mode):
    """ Pad the border of a grid depending on the padding mode (see below).
    Return the padded grid. 

    Valid modes:
     - 'live' counts cells outside of the grid as live.
     - 'dead' counts cells outside of the grid as dead.
     - 'wrap' counts cells outside of the grid as the value of the cells on the opposite side.
     - 'symmetric' counts cells outside of the grid as the same value as the cells on that edge.
    """
    match pad_mode:
        case "live":
            grid = np.pad(grid, 1, mode="constant", constant_values=live)
            print("\nlive border:")
            print_grid(grid)
        case "dead":
            grid = np.pad(grid, 1, mode="constant", constant_values=dead)
            print("\ndead border:")
            print_grid(grid)
        case "wrap":
            grid = np.pad(grid, 1, mode=pad_mode)
            print("\nwrap border:")
            print_grid(grid)
        case "symmetric":
            grid = np.pad(grid, 1, mode=pad_mode)
            print("\nsymmetric border:")
            print_grid(grid)
        case _:
            raise ValueError("Invalid padding mode. Valid modes: live | dead | wrap | symmetric")
    return grid


def count_neighbors(grid, y, x):
    """Return the number of live neighbors for the cell at the given position in the grid."""
    return grid[y-1, x-1] + grid[y-1, x] + grid[y-1, x+1] + \
           grid[y,   x-1]                + grid[y,   x+1] + \
           grid[y+1, x-1] + grid[y+1, x] + grid[y+1, x+1]

def compute_next_gen(grid, pad_mode):
    """Compute the next state for each non-border cell of the input grid based on its number of live neighbors.
    Return the newly calculated grid.

    *** GAME OF LIFE RULES ***
    * Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    * Any live cell with two or three live neighbors lives on to the next generation.
    * Any live cell with more than three live neighbors dies, as if by overpopulation.
    * Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    """
    retval = grid.copy()
    #ranges need to exclude the first and last elements of each axis to avoid an indexing error.
    for y in range(1, grid.shape[0]-1):
        for x in range(1, grid.shape[1]-1):
            neighbors = count_neighbors(grid, y, x)
            if neighbors == 3:
                retval[y, x] = live
            elif grid[y, x] == live and neighbors == 2:
                retval[y, x] = live
            else:
                retval[y, x] = dead

    #if the padding mode is either wrap or symmetric, we need to repad the grid
    if pad_mode == "wrap" or pad_mode == "symmetric":
        retval = np.pad(retval[1:-1, 1:-1], 1, mode=pad_mode)

    return retval

def run_game(grid, num_gens, pad_mode):
    """Plays game for given number of generations.
    Prints output of each generation (without padding) to terminal."""
    print("\ngeneration 0:")
    print_grid(grid[1:-1, 1:-1])

    for gen in range(1, num_gens+1):
        print(f"\ngeneration {gen}:")
        grid = compute_next_gen(grid, pad_mode)
        print_grid(grid[1:-1, 1:-1])



if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        num_gens = int(sys.argv[2])
        pad_mode = sys.argv[3]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <filename> <# of generations> <padding mode>")
    
    grid = np.loadtxt(filename, dtype=int)
    print("\nparsed input:")
    print_grid(grid)

    grid = pad_grid(grid, pad_mode)

    run_game(grid, num_gens, pad_mode)