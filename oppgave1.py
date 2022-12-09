import matplotlib.pyplot as plt
from pathlib import Path
import csv

fil = Path(__file__).parent / "Befolkning.csv"

class csvTilgraf:
    """
    Klasse for å tegne grafer fra data i en csv fil
    Forutsetter at filen er relativt lik Befolkning.csv, noe jeg antar mange filer fra ssb er, 
    og inneholder kun 2 verdier hver rad.

    Parametre:
        fil (str) = filen som skal brukes
        xverdier (list) = xverdiene til grafen
        yverdier (list) = yverdiene til grafen
        tegnsett (str) = tegnsettet til filen
        overskrifter (list) = navnet til y- og x-aksen
        tittel (str) = tittelen til grafen
    """
    def __init__(self, filnavn:str, tegnsett:str = "utf-8-sig", skilletegn:str = ";", overskrifter:list = False, tittel:str = False):
        self.fil = Path(__file__).parent / filnavn
        self.xverdier = []
        self.yverdier = []
        self.tegnsett = tegnsett
        self.skilletegn = skilletegn
        self.overskrifter = overskrifter
        self.tittel = tittel
    
    def klargjør(self):
        """
        Metode for å klargjøre data fra filen til å kunne brukes til å lage graf
        """
        with open(self.fil, encoding= self.tegnsett) as f:
            self.tittel = f.readlines(1)[0] # Tar første linje i dataen og gjør om til tittel
            self.tittel = self.tittel.replace('"','') # Tar vekk " fra stringen
            for line in f:
                line = line.rstrip().split(self.skilletegn) 
                if len(line) == 2: # sjekker om linjen har to variabler etter den ble splittet tidligere
                    self.overskrifter = line # Gjør om linjen til overskrift
                    self.overskrifter = [i.replace('"','') for i in self.overskrifter] # tar vekk "
                    break # bryter loopen siden vi vil bare ha overskriften

            filInnhold = csv.reader(f, delimiter=self.skilletegn) # Gjør det enklere for å appende til x-verdi og y-verdi listen
            for rad in filInnhold:
                self.xverdier.append(int(rad[0])) # appender xverdier
                self.yverdier.append(int(rad[1])) # appender yverdier

    def lagGraf(self):
        """
        lager grafen (Denne burde brukes hvis man skal plotte flere grafer)
        """
        self.klargjør() # utfører denne funksjonen først
        plt.plot(self.xverdier, self.yverdier, color = 'blue', linestyle = '--', label = self.overskrifter[1]) # plotter
    
    def finGraf(self):
        """
        Legger til tittel, akse-tittler og grid til grafen
        """
        self.lagGraf() # utfører denne funksjonen først
        plt.title(self.tittel)     # tittel
        plt.xlabel(self.overskrifter[0])     # x-aksetittel
        plt.ylabel(self.overskrifter[1])     # y-aksetittel
        plt.grid()       # tegner rutenett

    def tegnGraf(self):
        """
        viser grafen
        """
        self.finGraf() # utfører denne funksjonen først
        plt.show() # Viser grafen

#graf = csvTilgraf(fil) #utfører oppgaven, men ikke import med dette aktivert
#graf.tegnGraf() # utfører oppgaven, men ikke import med dette aktivert