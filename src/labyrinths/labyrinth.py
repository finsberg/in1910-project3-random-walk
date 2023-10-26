import matplotlib.pyplot as plt
import numpy as np


class InvalidSquareError(LookupError):
    pass


def get_legal_line(arr, y):
    """All legal points at a certain line of maze"""
    if not isinstance(y, (int, np.integer)):
        raise TypeError("line number y must be an int.")
    return [(x[0], y) for x in np.argwhere(arr[:, y])]


def plot(arr, ax=None):
    if ax is None:
        ax = plt.gca()
    im = ax.imshow(arr.T, origin="lower", cmap="gray")
    im.set_clim(vmax=1)
    ax.set_axis_off()
    return im


def circular(R: int = 100, padding: int = 2):
    """Create a circular area.
    input:
        R (int): radius of the circular area
        padding (int): padding around the area
    """
    N = int(2 * (R + padding) + 1)
    c = (N - 1) // 2
    x = np.arange(N)
    xx, yy = np.meshgrid(x, x)
    return (xx - c) ** 2 + (yy - c) ** 2 <= R**2


def example():
    arr = np.zeros((7, 7), dtype=bool)
    indices = np.array([1, 3, 5])
    arr[1:-1, indices] = True
    arr[indices, 1:-1] = True
    return arr


def labyrinth(layers=2, width=3, height=5):
    bars = 3 ** (layers + 1)
    Mx = 2 + width * bars + bars - 1
    My = 2 + height * (layers + 2) + width * (layers + 1)
    arr = np.zeros((Mx, My), dtype=bool)
    jump = 4
    for n in range(layers + 2):
        start0 = 2 * 3**n - 1
        start1 = n * (height + width) + 1
        end1 = start1 + height
        for j in range(width):
            arr[start0 + j :: jump, start1:end1] = True
        if n != layers + 1:
            arr[start0:-start0, end1 : end1 + width] = True
        jump *= 3
    return arr
