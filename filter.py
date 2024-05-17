#!/usr/bin/python3

from PIL import Image
from dithering import ordered_dither
import numpy as np
import gol

#TODO: replace PIL with Wand

def normalize(grid):
    """Return a copy of the grid where all non-zero values are set to 1."""
    retval = grid.copy()
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == 0:
                retval[y, x] = 0
            else:
                retval[y, x] = 1
    return retval

def denormalize(grid):
    """Return a copy of the grid where all non-zero values are set to 255."""
    retval = grid.copy()
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == 0:
                retval[y, x] = 0
            else:
                retval[y, x] = 255
    return retval

def open_image(filename, is_color):
    try:
        with Image.open(filename) as im:
            colorspace = "RGB" if is_color else "L"
            im = im.convert(colorspace)
            return im
    except OSError:
        raise SystemExit(f"Could not open {filename}.")
    
def apply_dither_channel(ch, dither_mode):
    """Return a PIL image that is the input with a Bayer dither filter applied
       to an individual color channel or a grayscale image."""
    dither_mode = "Bayer" + dither_mode
    ch = np.array(ch)
    ch = ordered_dither(ch, dither_mode)
    ch = Image.fromarray(ch)
    return ch

def apply_dither_rgb(im, dither_mode):
    """Return a PIL image that is the input with a Bayer dither filter applied
       to each of its color channels separately."""
    r, g, b = im.split()
    r = apply_dither_channel(r, dither_mode)
    g = apply_dither_channel(g, dither_mode)
    b = apply_dither_channel(b, dither_mode)
    im = Image.merge('RGB', (r, g, b))   
    return im

def apply_dither(im, dither_mode, is_color):
    """Return a PIL image that is the input with a Bayer dither filter applied."""
    return apply_dither_rgb(im, dither_mode) if is_color else apply_dither_channel(im, dither_mode)

def apply_filter_channel(ch, num_gens, pad_mode):
    """Return a PIL image that is a result of applying Game of Life rules
       to an individual color channel or a grayscale image."""
    #somehow the normalize/denormalize functions are faster than dividing
    #the cell values by 255, but I still want to try to improve speed
    ch = np.array(ch)
    ch = normalize(ch)
    ch = gol.run_game(ch, num_gens, pad_mode)
    ch = denormalize(ch)
    ch = Image.fromarray(ch)
    return ch

def apply_filter_rgb(im, num_gens, pad_mode):
    """Return a PIL image that is a result of applying Game of Life rules
       to each of its color channels separately."""
    r, g, b = im.split()
    r = apply_filter_channel(r, num_gens, pad_mode)
    g = apply_filter_channel(g, num_gens, pad_mode)
    b = apply_filter_channel(b, num_gens, pad_mode)
    im = Image.merge('RGB', (r, g, b))

    return im

def apply_filter(im, num_gens, pad_mode, is_color):
    """Return a PIL image that is a result of applying Game of Life rules
       to its pixels."""
    return apply_filter_rgb(im, num_gens, pad_mode) if is_color else apply_filter_channel(im, num_gens, pad_mode)
