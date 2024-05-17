import argparse
import os
import filter
import PIL.ImageOps

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
parser.add_argument("-c", "--color",
                    help="set the color space of the output image to RGB. the resulting image will be grayscale if this option is not given",
                    action="store_true")
parser.add_argument("-i", "--invert",
                    help="swap the values of live and dead cells in the image",
                    action="store_true")
parser.add_argument("-e", "--extension",
                    help="set the file extension of the output. default: bmp")

args = parser.parse_args()


#set default values of optional arguments
pad_mode = args.pad if args.pad else "dead"
dither_mode = args.dither if args.dither else "2x2"

img = filter.open_image(args.file, args.color)
img = filter.apply_dither(img, dither_mode, args.color)
if args.invert: #not sure yet if it matters whether this is done before or after dithering.
    img = PIL.ImageOps.invert(img)
print("Applying filter...")
img = filter.apply_filter(img, args.ngens, pad_mode, args.color)

outfile = os.path.splitext(args.file)
#set output info that cannot be taken directly from values
colorspace = "_rgb" if args.color else "_grayscale"
inverted = "_inverted" if args.invert else ""
info = f"_gen{args.ngens}" + f"_{pad_mode}" + f"_{dither_mode}" + colorspace + inverted 
outfile = outfile[0] + info + ".bmp"
img.save(outfile)

print(f"Image saved to: {outfile}")