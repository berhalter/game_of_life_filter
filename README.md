# Game of Life Image Filter
This program applies Conway's Game of Life to images, either in RGB or grayscale.

## Requirements
Requires [Pygame](https://www.pygame.org/), [NumPy](https://numpy.org/), [Pillow](https://python-pillow.org/), and [Dithering](https://pypi.org/project/dithering/)

## Usage
Run `python main.py` in your command line.
```
usage: main.py [-h] [-p {dead,live,wrap,symmetric}] [-d {2x2,4x4,8x8}]
               [--rgb] [-i]
               ngens file

positional arguments:
  ngens                 number of generations
  file                  path to the image that will be filtered

options:
  -h, --help            show this help message and exit
  -p {dead,live,wrap,symmetric}, --pad {dead,live,wrap,symmetric}
                        determine how cells outside the edge of the image
                        are treated. default: dead
  -d {2x2,4x4,8x8}, --dither {2x2,4x4,8x8}
                        set the bayer filter size. default: 2x2
  --rgb                 set the color space of the output image to RGB.
                        the resulting image will be grayscale if this
                        option is not given
  -i, --invert          swap the values of live and dead cells in the
                        image
```

## Bugs and Future Improvements
Please see the "Issues" tab for this repository.

## License
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)
