import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            zx, zy = x * (x_max - x_min) / (width - 1) + x_min, y * (y_max - y_min) / (height - 1) + y_min
            c = zx + zy * 1j
            image[y, x] = mandelbrot(c, max_iter)
    return image

image = generate_fractal(700, 700, -2.0, 1.0, -1.5, 1.5, 256)
plt.imshow(image, extent=(-2, 1, -1.5, 1.5), cmap="hot")
plt.colorbar()
plt.show()
