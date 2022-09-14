import math
import numpy as np
import matplotlib as mpl
import pandas as pd
import datetime as date


if __name__ == '__main__':
    L = 15  # Input length
    D = 3.12  # Input base diameter
    res = 200  # resolution

    xarr = np.linspace(0, L, res)

    von_karman(L, D, xarr)


def von_karman(L, D, xarr):
    yarr = np.empty(0)
    r = D / 2
    print(r)
    for i in len(xarr):
        phi = np.arccos(1 - (2 * xarr[i] / L))
        y = (r / math.sqrt(math.pi)) * math.sqrt(phi - ((math.sin(2 * phi)) / 2))
        yarr = np.append(yarr, np.array([y]))
    f = open("von_karman", 'x')




