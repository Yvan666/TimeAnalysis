import math

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import figure
import statistics

mpl.use('TkAgg')


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
    with open('lc_pn_60s.dat', 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]) - 5.579416976389E+08)
            y.append(float(p[1]))
        return x, y


def subinterval(n2):
    tmpY = []
    sucetX = 0
    sucetY = 0
    i = 0
    j = 1
    k = 0
    while j < (len(x) / n2):
        while i < n2:
            sucetX += x[k]
            sucetY += y[k]
            tmpY.append(y[k])
            i += 1
            k += 1
        i = 0
        priemerY = sucetY / n2
        priemerX = sucetX / n2

        varArr.append(math.sqrt(statistics.variance(tmpY)))
        subintervalTok.append(priemerY)
        subintervalCas.append(priemerX)

        tmpY.clear()
        priemerY = 0
        priemerX = 0
        sucetY = 0
        sucetX = 0
        j += 1

    return subintervalCas, subintervalTok, varArr


def interval(n1):
    priemerSigmaArr = []
    priemerSigma = 0
    sucetSigma = 0
    sucetX = 0
    sucetY = 0

    i = 0
    j = 1
    k = 0
    while j < (len(subintervalCas) / n1):
        while i < n1:
            sucetX += subintervalCas[k]
            sucetY += subintervalTok[k]
            sucetSigma += varArr[k]
            i += 1
            k += 1
        i = 0
        priemerY = sucetY / n1
        priemerX = sucetX / n1
        priemerSigma = sucetSigma / n1

        intervalTok.append(priemerY)
        intervalCas.append(priemerX)
        priemerSigmaArr.append(priemerSigma)

        sucetSigma = 0
        priemerSigma = 0
        priemerY = 0
        priemerX = 0
        sucetY = 0
        sucetX = 0
        j += 1
    sigmaZPS = math.sqrt(statistics.variance(priemerSigmaArr))

    return intervalCas, intervalTok, priemerSigmaArr, sigmaZPS


def smerOdchylka(n1):
    sigmaMeanY = 0
    sigmaMeanY = 0
    sigmaY = math.sqrt(statistics.variance(intervalTok))
    sigmaMeanY = sigmaY / n1

    return sigmaMeanY


sigmaZPS = 0
varArr = []
priemerSigmaArr = []

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

subintervalCas, subintervalTok, varArr = subinterval(n2)
intervalCas, intervalTok, priemerSigmaArr, sigmaZPS = interval(n1)

print("varArr = ", varArr)
print("priemerSigmaArr = ", priemerSigmaArr)
print("sigmaZPS = ", sigmaZPS)
sigmaMeanY = smerOdchylka(n1)

# plt.plot(x, y, linewidth=0.3)
plt.plot(intervalCas, priemerSigmaArr, 'g', linewidth=1, )
plt.errorbar(intervalCas, priemerSigmaArr, yerr=sigmaMeanY, ls='none', elinewidth=1, capsize=3)
plt.show()
