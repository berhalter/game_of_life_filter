#!/usr/bin/python3

import numpy as np
import sys

import os

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        num_gens = sys.argv[2]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <filename> <# of generations>")
        
    grid = np.zeros((24, 80), int)
    print("init:")
    for row in grid:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()

    print('\ninput:')
    print(read_data)

