import math
import numpy as np
from matplotlib import pyplot as plt


def von_karman(L, D, xarr):
    yarr = np.empty(0)  # Creates an empty array for y values
    zarr = np.zeros(len(xarr))  # Creates an array full of zeros for z axis
    r = D / 2  # Calculates radius
    phis = np.arccos(1 - (2 * xarr / L))  # Used the x array to calculates angles relative to the origin y-axis
    for i in phis:
        y = (r / math.sqrt(math.pi)) * math.sqrt(i - ((math.sin(2 * i)) / 2))  # Calculates y values from angle values
        yarr = np.append(yarr, np.array([y]))  # Appends y values to y array
    arr = [xarr, yarr, zarr]  # Combines all x,y, z arrays to be one matrix
    arr = np.transpose(arr)
    f = open("von_karman_points.dat", 'w')  # Creates/opens point.dat file and saves matrix values inside
    np.savetxt("von_karman_points.dat", arr)
    f.close()

    plt.title("Von Karman Nose Cone")  # Plots nose cone
    plt.xlabel("Length (in)")
    plt.ylabel("Radius (in)")
    plt.plot(xarr, yarr)
    plt.show()


if __name__ == '__main__':
    L = 15  # Input length
    D = 3.12  # Input base diameter
    res = 200  # Resolution of points, small = accuracy

    xarr = np.linspace(0, L, res)  # Generates length array

    von_karman(L, D, xarr)
