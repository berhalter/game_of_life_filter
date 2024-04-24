#!/usr/bin/python3

import numpy as np
import sys


"""
use this for different border modes(dead, wrap, live, copy):
https://numpy.org/doc/stable/reference/generated/numpy.pad.html
"""

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        num_gens = sys.argv[2]
        mode = sys.argv[3]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <filename> <# of generations> <padding mode>")
    

    width = 80
    height = 24
    grid = np.zeros((height, width), int)
    print("init:")
    for row in grid:
        for col in row:
            sys.stdout.write(str(col))
        print()

    print("\nparsed input:")
    input = np.loadtxt(filename, dtype=int)
    for row in input:
        for col in row:
            sys.stdout.write(str(col))
        print()

    match mode:
        case "live":
            pass
        case "dead":
            pass
        case "wrap":
            pass
        case "copy":
            pass
        case _:
            raise ValueError("Invalid border mode. Valid inputs: \n" + 
                             "'live' - grid border is padded with live cells\n" +
                             "'dead' - grid is padded with dead cells\n" +
                             "'wrap' - grid is padded with cells from the opposite side\n" +
                             "'copy' - grid is padded with a copy of the adjacent cell")



