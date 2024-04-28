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
    return retval

def open_image(filename):
    try:
        with Image.open(filename) as im:
            im = im.convert("L")
            #im.show()
            return im
    except OSError:
        raise SystemExit(f"Could not open {filename}.")


def apply_filter(im, num_gens, pad_mode):
    im = np.array(im)
    im = ordered_dither(im, "Bayer2x2") #TODO: parameterize the fitler size
    im = normalize(im)
    im = game.run_game(im, num_gens, pad_mode)
    im = denormalize(im)
    im = Image.fromarray(im)
    return im
