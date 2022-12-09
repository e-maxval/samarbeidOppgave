import json         #Importerer Json for å lese filen
import matplotlib .pyplot as plt            #Importerer Matplotlib.pyplot for å fremstille data
from pathlib import Path

fil = Path(__file__).parent / "Sivilstand.json"
json_data = open(fil)         #Åpner filen "Sivilstand.json
json_load = json.load(json_data)            #Laster inn dataen       

input = json_load["dataset"]["dimension"]["Tid"]["category"]["index"].keys()        #Finner frem til årstall
xaxis = [int(x) for x in input]         #Omdanner til tall og bruker de som x-verdier
yaxis1 = json_load["dataset"]["value"][0:42]        #Definerer første intervall med y-verdier(Første graf)
yaxis2 = json_load["dataset"]["value"][42:84]       #Definerer Andre intervall med y-verdier(Andre graf)
yaxis3 = json_load["dataset"]["value"][84:126]      #Definerer Tredje intervall med y-verdier(Tredje graf)  
yaxis4 = json_load["dataset"]["value"][126:168]     #Definerer Fjerde intervall med y-verdier(Fjerde graf)
yaxis5 = json_load["dataset"]["value"][168:210]     #Definerer Femte intervall med y-verdier(Femte graf)


plt.xlabel("År")        #Setter navn på x-aksen til "År"
plt.ylabel("Sivilstand")        #Setter navn på y-aksen til "Sivilstand"
plt.title("Sivilstand fra 1769 til 2022")   #Overskrift på grafene
plt.plot(xaxis,yaxis1, label='ugift')       #Plotter første intervall med grafnavn: "Ugift"
plt.plot(xaxis,yaxis2, label='gift')        #Plotter andre intervall med grafnavn: "gift"
plt.plot(xaxis,yaxis3, label='Enke/Enkemann')       #Plotter tredje intervall med grafnavn: "Enke/Enkemann"
plt.plot(xaxis,yaxis4, label='Separert')        #Plotter fjerde intervall med grafnavn: "Separert"
plt.plot(xaxis,yaxis5, label='Skilt')       #Plotter femte intervall med grafnavn: "Skilt"

plt.legend()

plt.show()      #Viser grafen