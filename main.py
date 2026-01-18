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
    arr = mandelbrot.get_render()
    arr_np = np.asarray(arr)
    iter_max = getattr(mandelbrot, 'iter_max', 50)
    h, w = arr_np.shape
    rgb = np.zeros((h, w, 3), dtype=np.uint8)

    def hsv_to_rgb(hue, s=1.0, v=1.0):
        i = int(hue * 6.0)
        f = hue * 6.0 - i
        p = v * (1.0 - s)
        q = v * (1.0 - f * s)
        t = v * (1.0 - (1.0 - f) * s)
        i = i % 6
        if i == 0:
            r, g, b = v, t, p
        elif i == 1:
            r, g, b = q, v, p
        elif i == 2:
            r, g, b = p, v, t
        elif i == 3:
            r, g, b = p, q, v
        elif i == 4:
            r, g, b = t, p, v
        else:
            r, g, b = v, p, q
        return int(r * 255), int(g * 255), int(b * 255)

    for y in range(h):
        for x in range(w):
            val = arr_np[y, x]
            if val >= iter_max:
                rgb[y, x] = (0, 0, 0)
            else:
                hue = (val / float(iter_max)) % 1.0
                r, g, b = hsv_to_rgb(hue)
                rgb[y, x] = (r, g, b)

    image = im.fromarray(rgb, 'RGB')
    image.show()

    mandelbrot.zoom_on_interesting_area()
