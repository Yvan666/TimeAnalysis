import math

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import figure
import statistics


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


def Data():
    with open('lc_PN_10s.dat', 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]) - 5.579416976389E+08)
            y.append(float(p[1]))
        return x, y


def subinterval(n2):
    sucetX = 0
    sucetY = 0
    i = 0
    j = 1
    k = 0
    while j < (len(x) / n2):
        while i < n2:
            sucetX += x[k]
            sucetY += y[k]
            i += 1
            k += 1
        i = 0
        priemerY = sucetY / n2
        priemerX = sucetX / n2

        subintervalTok.append(priemerY)
        subintervalCas.append(priemerX)

        priemerY = 0
        priemerX = 0
        sucetY = 0
        sucetX = 0
        j += 1

    return subintervalCas, subintervalTok


def interval(n1):
    sucetX = 0
    sucetY = 0
    i = 0
    j = 1
    k = 0
    while j < (len(subintervalCas) / n1):
        while i < n1:
            sucetX += subintervalCas[k]
            sucetY += subintervalTok[k]
            i += 1
            k += 1
        i = 0
        priemerY = sucetY / n1
        priemerX = sucetX / n1

        intervalTok.append(priemerY)
        intervalCas.append(priemerX)

        priemerY = 0
        priemerX = 0
        sucetY = 0
        sucetX = 0
        j += 1
    return intervalCas, intervalTok


def smerOdchylka(n1):
    sigmaMeanX = 0
    sigmaMeanY = 0
    sigmaMeanX = 0
    sigmaMeanY = 0
    sigmaX = math.sqrt(statistics.variance(intervalCas))
    sigmaY = math.sqrt(statistics.variance(intervalTok))
    sigmaMeanX = sigmaX / n1
    sigmaMeanY = sigmaY / n1

    return sigmaMeanX, sigmaMeanY


subintervalTok = []
subintervalCas = []

intervalCas = []
intervalTok = []

styleSheet()
# annot_max(x, y)


# plt.savefig('testImg', dpi=100)
n1 = int(input("zadaj n1: "))
n2 = int(input("zadaj n2:"))

x, y = Data()

subintervalCas, subintervalTok = subinterval(n2)
intervalCas, intervalTok = interval(n1)


print(intervalCas)
sigmaMeanX, sigmaMeanY = smerOdchylka(n1)
print(sigmaMeanX)
print(sigmaMeanY)

# plt.plot(x, y)
# plt.plot(subintervalCas, subintervalTok, linewidth=1)
# plt.plot(intervalCas, intervalTok, linewidth=1)
# plt.plot(sigmaX, sigmaY)
plt.errorbar(intervalCas, intervalTok, xerr=sigmaMeanX, yerr=sigmaMeanY,ls='none', elinewidth=0.3, lw=1)
plt.show()
