import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import csv

fil = Path(__file__).parent / "Skilsmisser og ekteskap.csv"

with open(fil, encoding="utf-8-sig") as f:
    tittel = f.readlines(1)[0] # Tar første linje i dataen og gjør om til tittel
    tittel = tittel.replace('"','') # Tar vekk " fra stringen
    filInnhold = csv.reader(f, delimiter=";")
    titler = []
    data = []
    for rad in filInnhold:
        if len(rad) == 0:
            pass
        else:
            if rad[0] == "statistikkvariabel":
                data1_tittel = rad[0]
                data1 = rad[1:]
            else:
                titler.append(rad[0])
                data = data + rad[1:]
    k = 0
    for i in data:
        if ".." in i:
            data[k] = "NaN"
        k += 1
    data = [float(i) for i in data]

antall_data = len(titler)
data_lengde = int(len(data)/antall_data)
avstand = 0.05
høyde = data_lengde/antall_data/data_lengde-avstand
offset = høyde/2

fig, ax = plt.subplots(figsize=(10, 6)) 

y = np.arange(data_lengde)

ax.barh(y + offset, data[:data_lengde], height = høyde, label = titler[0])
ax.barh(y - offset, data[data_lengde:], height = høyde, label = titler[1])
ax.set_yticks(y, data1)
ax.grid(axis="x")
ax.legend()
plt.show()