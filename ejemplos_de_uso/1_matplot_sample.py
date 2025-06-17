#Data Visualization with matplotlib

import numpy as np
import matplotlib.pyplot as plt

def build_points():
    x0 = float(0)
    y0 = float(0) * 2.0

    x1 = float(1)
    y1 = float(1) * 1.5

    x2 = float(2)
    y2 = float(2) * 2.0

    x3 = float(3)
    y3 = float(3) * 1.5

    x4 = float(4)
    y4 = float(4) * 2.0

    x = np.array((x0, x1, x2, x3, x4))
    y = np.array((y0, y1, y2, y3, y4))
    return x, y

def draw_plot(x, y):
    plt.plot(x, y)
    plt.title("Simple Plot with Modern NumPy")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

x, y = build_points()
draw_plot(x, y)
