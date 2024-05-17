#!/usr/bin/env python3

"""
    Command line version of the Game of Life Image Filter.
    Copyright (C) 2024  Matthew Berhalter

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
import os
import filter
import PIL.ImageOps


print("""Game of Life Image Filter  Copyright (C) 2024  Matthew Berhalter
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain
conditions.
""")


parser = argparse.ArgumentParser()
#required arguments
parser.add_argument("ngens", 
                    help="number of generations",
                    type=int)
parser.add_argument("file",
                    help="path to the image that will be filtered")

#optional arguments
parser.add_argument("-p", "--pad",
                    help="determine how cells outside the edge of the image are treated. default: dead",
                    choices=["dead", "live", "wrap", "symmetric"])
parser.add_argument("-d", "--dither",
                    help="set the bayer filter size. default: 2x2",
                    choices=["2x2","4x4","8x8"])
parser.add_argument("--rgb",
                    help="set the color space of the output image to RGB. the resulting image will be grayscale if this option is not given",
                    action="store_true")
parser.add_argument("-i", "--invert",
                    help="swap the values of live and dead cells in the image",
                    action="store_true")

args = parser.parse_args()


#set default values of optional arguments
pad_mode = args.pad if args.pad else "dead"
dither_mode = args.dither if args.dither else "2x2"

img = filter.open_image(args.file, args.rgb)
img = filter.apply_dither(img, dither_mode, args.rgb)
if args.invert: #looks better when done after dithering imo.
    img = PIL.ImageOps.invert(img)
print("Applying filter...")
img = filter.apply_filter(img, args.ngens, pad_mode, args.rgb)

outfile = os.path.splitext(args.file)
#set output info that cannot be taken directly from values
colorspace = "_rgb" if args.rgb else "_grayscale"
inverted = "_inverted" if args.invert else ""
info = f"_gen{args.ngens}" + f"_{pad_mode}" + f"_{dither_mode}" + colorspace + inverted 
outfile = outfile[0] + info + ".bmp"
img.save(outfile)

print(f"Image saved to: {outfile}")