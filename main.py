from mandelbrot import Mandelbrot
from PIL import Image as im
import numpy as np
import sys

mandelbrot = Mandelbrot()

# default height and width - need to hardcode for debug mode
WIDTH = 192
HEIGHT = 128

while True:
    print("Starting render...")
    mandelbrot.render(WIDTH, HEIGHT)
    print("Done!")
    arr = mandelbrot.get_render()
    arr = (np.asarray(arr)*255).astype(np.uint8)
    image = im.fromarray(arr)
    # Save the image as BMP
    image = image.convert("1")

    image.show()

    mandelbrot.zoom_on_interesting_area()
