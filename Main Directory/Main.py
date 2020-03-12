import ax
import inline as inline
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd


def Read_Two_Column_File():
    with open('lc_PN_10s.dat', 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))
    return x, y


def annot_max(x, y, ax=None):
    xmax = max(x)
    ymax = max(y)
    text = "x={:f}, y={:f}".format(xmax, ymax)
    if not ax:
        ax = plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.5", fc="w", ec="k", lw=0.72)
    kw = dict(xycoords='data', textcoords="axes fraction", bbox=bbox_props, ha="right", va="center")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94, 0.96), **kw)


def styleSheet():
    figure(figsize=(8, 6))
    plt.xlabel("Cas")
    plt.ylabel("Pocet fotonov")
    mpl.rcParams['lines.linewidth'] = 0.5


x, y = Read_Two_Column_File()
styleSheet()

annot_max(x, y)
plt.plot(x, y)
plt.savefig('testImg', dpi=100)
plt.show()