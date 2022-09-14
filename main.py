import math
import numpy as np
import matplotlib as mpl
import pandas as pd
import datetime as date


def von_karman(L, D, xarr):
    yarr = np.empty(0)
    zarr = np.zeros(len(xarr))
    r = D / 2
    phis = np.arccos(1 - (2 * xarr / L))
    for i in phis:
        y = (r / math.sqrt(math.pi)) * math.sqrt(i - ((math.sin(2 * i)) / 2))
        yarr = np.append(yarr, np.array([y]))
    arr = [xarr, yarr, zarr]
    arr = np.transpose(arr)
    f = open("von_karman_points.dat", 'w')
    np.savetxt("von_karman_points.dat", arr)


if __name__ == '__main__':
    L = 15  # Input length
    D = 3.12  # Input base diameter
    res = 200  # Resolution of points, small = accruacy

    xarr = np.linspace(0, L, res)  # Generates length array

    von_karman(L, D, xarr)
