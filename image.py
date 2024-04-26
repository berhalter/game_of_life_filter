#!/usr/bin/python3

from PIL import Image
from dithering import ordered_dither
import sys
import numpy as np

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            im = im.convert("L")
            im = np.array(im)
            im = ordered_dither(im, "Bayer2x2")
            print(im)
            im = Image.fromarray(im)
            im.show()
    except OSError:
        print("womp womp")