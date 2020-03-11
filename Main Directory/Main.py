import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import figure

def Read_Two_Column_File():
    with open('lc_PN_10s.dat', 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))
    return x, y

def styleSheet():
    figure(figsize=(8, 6))
    plt.xlabel("Cas")
    plt.ylabel("Pocet fotonov")
    mpl.rcParams['lines.linewidth'] = 0.5


x, y = Read_Two_Column_File()

styleSheet()
plt.plot(x, y)
plt.savefig('testImg', dpi=400)
plt.show()