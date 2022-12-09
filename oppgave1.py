import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import csv

fil = Path(__file__).parent / "Befolkning.csv"

class csvTilgraf:
    def __init__(self, filnavn:str, tegnsett:str = "utf-8-sig"):
        self.fil = Path(__file__).parent / filnavn
        self.xverdier = []
        self.yverdier = []
        self.tegnsett = tegnsett
        self.overskrifter = []
        self.tittel = ""
    
    def klargjør(self):
        with open(self.fil, encoding= self.tegnsett) as f:
            self.tittel = f.readlines(1)
            for line in f:
                line = line.rstrip().split(";")
                print(line)
                if len(line) == 2: 
                    self.overskrifter = line
                    self.overskrifter = [i.replace('"','') for i in self.overskrifter]
                    print(self.overskrifter)
                    break

            filInnhold = csv.reader(f, delimiter=";")
            for rad in filInnhold:
                self.xverdier.append(int(rad[0]))
                self.yverdier.append(int(rad[1]))

    def lagGraf(self):
        xdiff = (abs(max(self.xverdier)-min(self.xverdier)))/25
        ydiff = (abs(max(self.yverdier)-min(self.yverdier)))/25

        plt.plot(self.xverdier, self.yverdier, color = 'blue', linestyle = '--')
        plt.title(self.tittel)     # tittel
        plt.xlabel(self.overskrifter[0])     # x-aksetittel
        plt.ylabel(self.overskrifter[1])     # y-aksetittel
        plt.xlim(min(self.xverdier) - xdiff,max(self.xverdier) + xdiff)   # definisjonsmengde
        plt.ylim(min(self.yverdier) - ydiff,max(self.yverdier) + ydiff)   # verdimengde
        plt.grid()       # tegner rutenett
        plt.legend()

    def tegnGraf(self):
        self.lagGraf()
        plt.show()
        

graf = csvTilgraf("Befolkning.csv")
graf.klargjør()
graf.tegnGraf()