import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import csv

fil = Path(__file__).parent / "Befolkning.csv"
xverdier = []
yverdier = []
with open(fil, encoding = "utf-8-sig") as f:
    i = 0
    next(f)
    next(f)
    filInnhold = csv.reader(f, delimiter=";")
    overskrifter = next(filInnhold)
    for rad in filInnhold:
        xverdier.append(int(rad[0]))
        yverdier.append(int(rad[1]))
        i += 1

xdiff = (abs(max(xverdier)-min(xverdier)))/25
ydiff = (abs(max(yverdier)-min(yverdier)))/25

plt.plot(xverdier, yverdier, color = 'blue', linestyle = '--')
plt.title("Folketall fra 1769")      # tittel
plt.xlabel("År")             # x-aksetittel
plt.ylabel("Befolkning")     # y-aksetittel
plt.xlim(min(xverdier) - xdiff,max(xverdier) + xdiff)   # definisjonsmengde
plt.ylim(min(yverdier) - ydiff,max(yverdier) + ydiff)   # verdimengde
plt.grid()       # tegner rutenett
plt.legend()
plt.show()