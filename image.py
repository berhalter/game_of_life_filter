#!/usr/bin/python3

from PIL import Image
from dithering import ordered_dither
import numpy as np
import game

#TODO: Rename this file to avoid confusion

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
            im = im.convert("RGB")
            #im.show()
            return im
    except OSError:
        raise SystemExit(f"Could not open {filename}.")

def apply_dither(im):
    """Return a PIL image that is the input with a Bayer dither filter applied"""
    r, g, b = im.split()
    r = np.array(r)
    r = ordered_dither(r, "Bayer2x2") #TODO: parameterize the fitler size
    r = Image.fromarray(r)

    g = np.array(g)
    g = ordered_dither(g, "Bayer2x2") #TODO: parameterize the fitler size
    g = Image.fromarray(g)

    b = np.array(b)
    b = ordered_dither(b, "Bayer2x2") #TODO: parameterize the fitler size
    b = Image.fromarray(b)


    im = Image.merge('RGB', (r, g, b))   
    return im


def apply_filter(im, num_gens, pad_mode):
    """Return a PIL image that is a result of applying Game of Life rules to its pixels"""
    #somehow the normalize/denormalize functions are faster than dividing
    #the cell values by 255, but I still want to try to improve speed
    r, g, b = im.split()
    r = np.array(r)
    r = normalize(r)
    r = game.run_game(r, num_gens, pad_mode)
    r = denormalize(r)
    r = Image.fromarray(r)

    g = np.array(g)
    g = normalize(g)
    g = game.run_game(g, num_gens, pad_mode)
    g = denormalize(g)
    g = Image.fromarray(g)

    b = np.array(b)
    b = normalize(b)
    b = game.run_game(b, num_gens, pad_mode)
    b = denormalize(b)
    b = Image.fromarray(b)


    im = Image.merge('RGB', (r, g, b))

    return im
