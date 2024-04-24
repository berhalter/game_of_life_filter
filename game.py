#!/usr/bin/python3

import numpy as np
import sys

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        num_gens = sys.argv[2]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <filename> <# of generations>")
    

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


