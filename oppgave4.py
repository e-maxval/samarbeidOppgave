import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import csv

fil = Path(__file__).parent / "Skilsmisser og ekteskap.csv"

with open(fil, encoding="utf-8-sig") as f:
    tittel = f.readlines(1)[0] # Tar første linje i dataen og gjør om til tittel
    tittel = tittel.replace('"','') # Tar vekk " fra stringen
    filInnhold = csv.reader(f, delimiter=";") # reader ved hjelp av csv
    titler = [] # lager liste for tilene av de ulike data-tingene
    data = [] # lager liste for dataene
    for rad in filInnhold: 
        if len(rad) == 0: # gjør ingenting med tomme linjer
            pass
        else:
            if rad[0] == "statistikkvariabel": # finner hva som skal være "hovedakse"(/år)
                data1_tittel = rad[0] # Finner tittelen av hovedakse 
                data1 = rad[1:] # Finner dataen til hovedaksen
            else:
                titler.append(rad[0]) # legger til titlene til dataen/søylene
                data = data + rad[1:] # legger til dataene til liste for dataen
    k = 0 # lager en variabel med verdi null
    for i in data:
        if ".." in i: # finner der det ikke er et nummer i dataen
            data[k] = "NaN" # erstatter dette med "NaN"
        k += 1 # legger til en hver gang den går gjennom "i" i "data" for å kunne få indeksen
    data = [float(i) for i in data] # Gjør all dataen om til float (float fordi int("NaN") fungerte ikke)

antall_data = len(titler) # Finner hvor mange dataer/søyler som skal inn på hver hovedakse/år verdi (som er 2)
data_lengde = int(len(data)/antall_data) # finner hvor mange datapunkter for hver data/søylegruppe
avstand = 0.05 # avstanden jeg vil ha mellom søylene i et år til et annet
høyde = data_lengde/antall_data/data_lengde-avstand #Høyden til hver enkelt søyle (som her er 42/2/42 = 0.5)
offset = høyde/2 # finner hvor mye som skal offsettes for at begge søyelene skal vises

fig, ax = plt.subplots(figsize=(10, 6)) # lager figur

y = np.arange(data_lengde) # Lager tall fra 1 til lengden av dataene 

ax.barh(y + offset, data[:data_lengde], height = høyde, label = titler[0]) # lager søyler av de første datapunktene/"Inngåtte ekteskap"
ax.barh(y - offset, data[data_lengde:], height = høyde, label = titler[1]) # lager søyler av de andre datapunktene/"Skilsmisser"
ax.set_yticks(y, data1) # Setter årstall for y-dataene (søylene er horisontale).
ax.grid(axis="x") # Setter grid langs x-aksene (horisontale)
ax.legend() # Setter på labels
plt.show() # Viser søylene