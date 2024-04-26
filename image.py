#!/usr/bin/python3

from PIL import Image
from dithering import ordered_dither
import sys
import numpy as np
import game

def normalize(grid):
    """Return a copy of the grid where all non-zero values are set to 1"""
    retval = grid.copy()
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == 0:
                retval[y, x] = 0
            else:
                retval[y, x] = 1
    print(retval)
    return retval

def denormalize(grid):
    """Return a copy of the grid where all non-zero values are set to 255"""
    retval = grid.copy()
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == 0:
                retval[y, x] = 0
            else:
                retval[y, x] = 255
    print(retval)
    return retval


for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            im = im.convert("L")
            im = np.array(im)
            im = ordered_dither(im, "Bayer2x2")
            im = normalize(im)
            im = game.run_game(im, 10, "wrap")
            im = denormalize(im)
            im = Image.fromarray(im)
            im.show()
    except OSError:
        print("womp womp")