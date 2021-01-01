import pygame
import FelderKlasse
import FigurenKlasse
from Figurenklassen import pawn
from Figurenklassen import bishop
from Figurenklassen import king
from Figurenklassen import queen
from Figurenklassen import knight
from Figurenklassen import rook

# Texturen
BauernWeissTextur = "./textures/Bauer_1.png"
LaeuferWeissTextur = "./textures/Laeufer_1.png"
SpringerWeissTextur = "./textures/Springer_1.png"
TurmWeissTextur = "./textures/Turm_1.png"
KoenigWeissTextur = "./textures/Koenig_1.png"
DameWeissTextur = "./textures/Dame_1.png"
BauernSchwarzTextur = "./textures/Bauer_1_s.png"
LaeuferSchwarzTextur = "./textures/Laeufer_1_s.png"
SpringerSchwarzTextur = "./textures/Springer_1_s.png"
TurmSchwarzTextur = "./textures/Turm_1_s.png"
DameSchwarzTextur = "./textures/Dame_1_s.png"
KoenigSchwarzTextur = "./textures/Koenig_1_s.png"
SpielBrettBild = pygame.image.load("./textures/Schachbrett_x512.png")
markierungTextur = "./textures/markierung_1.png"
ZugMoeglichTextur = "./textures/markierung_1.png"
ZugMoeglichBild = pygame.image.load(ZugMoeglichTextur)
MarkierungBild = pygame.image.load(markierungTextur)
TurmSchwarzBild = pygame.image.load(TurmSchwarzTextur)
TurmWeissBild = pygame.image.load(TurmWeissTextur)
BauerSchwarzBild = pygame.image.load(BauernSchwarzTextur)
BauerWeissBild = pygame.image.load(BauernWeissTextur)
SpringerSchwarzBild = pygame.image.load(SpringerSchwarzTextur)
SpringerWeissBild = pygame.image.load(SpringerWeissTextur)
LaeuferSchwarzBild = pygame.image.load(LaeuferSchwarzTextur)
LaeuferWeissBild = pygame.image.load(LaeuferWeissTextur)
TurmSchwarzBild = pygame.image.load(TurmSchwarzTextur)
TurmWeissBild = pygame.image.load(TurmWeissTextur)
DameSchwarzBild = pygame.image.load(DameSchwarzTextur)
DameWeissBild = pygame.image.load(DameWeissTextur)
KoenigSchwarzBild = pygame.image.load(KoenigSchwarzTextur)
KoenigWeissBild = pygame.image.load(KoenigWeissTextur)

#Allgemeine Variablen
aktuellMarkiert = None
aktuellGeKlickt= None
title = "Chess"
fps = 10
AmZug = "Weiss"
SchachWeiss = False
SchachSchwarz = False
Figurenarten = ["wBauer", "wSpringer", "wLaeufer", "wDame", "wTurm", "wKönig",
                "sBauer", "sSpringer", "sLaeufer", "sDame", "sTurm", "sKönig"]
fieldsthatarepossible = []
fieldsthatarepossibleLenght = 0

# Alle Felderobjekte
a1 = FelderKlasse.FelderKlasse(1, Figurenarten[4])
b1 = FelderKlasse.FelderKlasse(2, Figurenarten[1])
c1 = FelderKlasse.FelderKlasse(3, Figurenarten[2])
d1 = FelderKlasse.FelderKlasse(4, Figurenarten[3])
e1 = FelderKlasse.FelderKlasse(5, Figurenarten[5])
f1 = FelderKlasse.FelderKlasse(6, Figurenarten[2])
g1 = FelderKlasse.FelderKlasse(7, Figurenarten[1])
h1 = FelderKlasse.FelderKlasse(8, Figurenarten[4])
a2 = FelderKlasse.FelderKlasse(9, Figurenarten[0])
b2 = FelderKlasse.FelderKlasse(10, Figurenarten[0])
c2 = FelderKlasse.FelderKlasse(11, Figurenarten[0])
d2 = FelderKlasse.FelderKlasse(12, Figurenarten[0])
e2 = FelderKlasse.FelderKlasse(13, Figurenarten[0])
f2 = FelderKlasse.FelderKlasse(14, Figurenarten[0])
g2 = FelderKlasse.FelderKlasse(15, Figurenarten[0])
h2 = FelderKlasse.FelderKlasse(16, Figurenarten[0])
a3 = FelderKlasse.FelderKlasse(17, "")
b3 = FelderKlasse.FelderKlasse(18, "")
c3 = FelderKlasse.FelderKlasse(19, "")
d3 = FelderKlasse.FelderKlasse(20, "")
e3 = FelderKlasse.FelderKlasse(21, "")
f3 = FelderKlasse.FelderKlasse(22, "")
g3 = FelderKlasse.FelderKlasse(23, "")
h3 = FelderKlasse.FelderKlasse(24, "")
a4 = FelderKlasse.FelderKlasse(25, "")
b4 = FelderKlasse.FelderKlasse(26, "")
c4 = FelderKlasse.FelderKlasse(27, "")
d4 = FelderKlasse.FelderKlasse(28, "")
e4 = FelderKlasse.FelderKlasse(29, "")
f4 = FelderKlasse.FelderKlasse(30, "")
g4 = FelderKlasse.FelderKlasse(31, "")
h4 = FelderKlasse.FelderKlasse(32, "")
a5 = FelderKlasse.FelderKlasse(33, "")
b5 = FelderKlasse.FelderKlasse(34, "")
c5 = FelderKlasse.FelderKlasse(35, "")
d5 = FelderKlasse.FelderKlasse(36, "")
e5 = FelderKlasse.FelderKlasse(37, "")
f5 = FelderKlasse.FelderKlasse(38, "")
g5 = FelderKlasse.FelderKlasse(39, "")
h5 = FelderKlasse.FelderKlasse(40, "")
a6 = FelderKlasse.FelderKlasse(41, "")
b6 = FelderKlasse.FelderKlasse(42, "")
c6 = FelderKlasse.FelderKlasse(43, "")
d6 = FelderKlasse.FelderKlasse(44, "")
e6 = FelderKlasse.FelderKlasse(45, "")
f6 = FelderKlasse.FelderKlasse(46, "")
g6 = FelderKlasse.FelderKlasse(47, "")
h6 = FelderKlasse.FelderKlasse(48, "")
a7 = FelderKlasse.FelderKlasse(49, Figurenarten[6])
b7 = FelderKlasse.FelderKlasse(50, Figurenarten[6])
c7 = FelderKlasse.FelderKlasse(51, Figurenarten[6])
d7 = FelderKlasse.FelderKlasse(52, Figurenarten[6])
e7 = FelderKlasse.FelderKlasse(53, Figurenarten[6])
f7 = FelderKlasse.FelderKlasse(54, Figurenarten[6])
g7 = FelderKlasse.FelderKlasse(55, Figurenarten[6])
h7 = FelderKlasse.FelderKlasse(56, Figurenarten[6])
a8 = FelderKlasse.FelderKlasse(57, Figurenarten[10])
b8 = FelderKlasse.FelderKlasse(58, Figurenarten[7])
c8 = FelderKlasse.FelderKlasse(59, Figurenarten[8])
d8 = FelderKlasse.FelderKlasse(60, Figurenarten[9])
e8 = FelderKlasse.FelderKlasse(61, Figurenarten[11])
f8 = FelderKlasse.FelderKlasse(62, Figurenarten[8])
g8 = FelderKlasse.FelderKlasse(63, Figurenarten[7])
h8 = FelderKlasse.FelderKlasse(64, Figurenarten[10])
alleFelderInEinerListe = [a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7,
                          c8, d1, d2, d3, d4, d5, d6, d7, d8, e1, e2, e3, e4, e5, e6, e7, e8, f1, f2, f3, f4, f5, f6,
                          f7, f8, g1, g2, g3, g4, g5, g6, g7, g8, h1, h2, h3, h4, h5, h6, h7, h8]
alleFelderInEinerListe2D = [[a1, a2, a3, a4, a5, a6, a7, a8], [b1, b2, b3, b4, b5, b6, b7, b8], [c1, c2, c3, c4, c5, c6, c7,
                          c8], [d1, d2, d3, d4, d5, d6, d7, d8], [e1, e2, e3, e4, e5, e6, e7, e8], [f1, f2, f3, f4, f5, f6,
                          f7, f8], [g1, g2, g3, g4, g5, g6, g7, g8], [h1, h2, h3, h4, h5, h6, h7, h8]]
alleFelderInEinerListeColoms= [a1, b1, c1, d1, e1, f1, g1, h1, a2, b2, c2, d2, e2, f2, g2, h2, a3, b3, c3, d3, e3, f3,
                               g3, h3, a4, b4, c4, d4, e4, f4, g4, h4, a5, b5, c5, d5, e5, f5, g5, h5, a6, b6, c6, d6,
                               e6, f6, g6, h6, a7, b7, c7, d7, e7, f7, g7, h7, a8, b8, c8, d8, e8, f8, g8, h8]

#alle FigurenObjekte
aBauerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[0], a2, True, "w")
bBauerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[0], b2, True, "w")
cBauerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[0], c2, True, "w")
dBauerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[0], d2, True, "w")
eBauerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[0], e2, True, "w")
fBauerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[0], f2, True, "w")
gBauerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[0], g2, True, "w")
hBauerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[0], h2, True, "w")
aBauerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[6], a7, True, "b")
bBauerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[6], b7, True, "b")
cBauerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[6], c7, True, "b")
dBauerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[6], d7, True, "b")
eBauerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[6], e7, True, "b")
fBauerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[6], f7, True, "b")
gBauerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[6], g7, True, "b")
hBauerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[6], h7, True, "b")
aTurmWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[4], a1, True, "w")
hTurmWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[4], h1, True, "w")
aTurmSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[10], h8, True, "b")
hTurmSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[10], a8, True, "b")
bSpringerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[1], b1, True, "w")
gSpringerWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[1], g1, True, "w")
bSpringerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[7], b8, True, "b")
gSpringerSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[7], g8, True, "b")
cLaeuferWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[2], c1, True, "w")
fLaeuferWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[2], f1, True, "w")
cLaeuferSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[8], c8, True, "b")
fLaeuferSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[8], f8, True, "b")
DameWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[3], d1, True, "w")
KoenigWeiss = FigurenKlasse.FigurenKlasse(Figurenarten[5], e1, True, "w")
DameSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[9], d8, True, "b")
KoenigSchwarz = FigurenKlasse.FigurenKlasse(Figurenarten[11], e8, True, "b")
alleFigurenInEinerListe = [aBauerWeiss, bBauerWeiss, cBauerWeiss, dBauerWeiss, eBauerWeiss, fBauerWeiss,
                           gBauerWeiss, hBauerWeiss, aBauerSchwarz, bBauerSchwarz, cBauerSchwarz, dBauerSchwarz,
                           eBauerSchwarz, fBauerSchwarz, gBauerSchwarz, hBauerSchwarz, aTurmWeiss, hTurmWeiss,
                           aTurmSchwarz, hTurmSchwarz, bSpringerWeiss, gSpringerWeiss, bSpringerSchwarz,
                           gSpringerSchwarz, cLaeuferWeiss, fLaeuferWeiss, cLaeuferSchwarz, fLaeuferSchwarz,
                           DameWeiss, KoenigWeiss, DameSchwarz, KoenigSchwarz]
alleFigurenInEinerListe2wegenIfcheck = [aBauerWeiss, bBauerWeiss, cBauerWeiss, dBauerWeiss, eBauerWeiss, fBauerWeiss,
                           gBauerWeiss, hBauerWeiss, aTurmWeiss, hTurmWeiss, bSpringerWeiss, gSpringerWeiss,
                            cLaeuferWeiss, fLaeuferWeiss, DameWeiss, KoenigWeiss,  aBauerSchwarz, bBauerSchwarz,
                            cBauerSchwarz, dBauerSchwarz, eBauerSchwarz, fBauerSchwarz, gBauerSchwarz,
                            hBauerSchwarz, bSpringerSchwarz, gSpringerSchwarz, cLaeuferSchwarz, fLaeuferSchwarz,
                            DameSchwarz, KoenigSchwarz]
def welchesFeldStehtDieFigur(figurobviously, whichArray):
    i = 0
    i2 = 0
    x = 0
    y = 0
    if whichArray == 2:
        while i < 8:
            while i2 < 8:
                if figurobviously.figurenposition.feldnummer == alleFelderInEinerListe2D[i][i2].feldnummer and x == 0:  # welches feld im array ist das feld auf dem der springer steht
                    x = i
                    y = i2
                i2 = i2 + 1
            i2 = 0
            i = i + 1
        return [x, y]
    elif whichArray == 1:
        while i < 64:
            if figurobviously.figurenposition.feldnummer == alleFelderInEinerListe[i].feldnummer:  # welches feld im array ist das feld auf dem der springer steht
                x = i
            i = i + 1
        return [x]

def welcheFigurStehtAufDemFeld(feld):
    i = 0
    while i < 32:
        if alleFigurenInEinerListe[i].figurenposition == feld:
            return alleFigurenInEinerListe[i]
        i = i + 1

def voidTheFigur(mtp):
    i = 0
    while i < 32:
        if alleFigurenInEinerListe[i].figurenposition == mtp and AmZug == "Weiss" and alleFigurenInEinerListe[i].color == "b" \
                or alleFigurenInEinerListe[i].figurenposition == mtp and AmZug == "Schwarz" and alleFigurenInEinerListe[i].color == "w":
            alleFigurenInEinerListe[i].isactive = False
            alleFigurenInEinerListe[i].figurenposition = "void"
        i = i + 1
    return True

def isthisyouownfigur(hilfvariable1, hilfsvariable2):
    if alleFelderInEinerListe2D[hilfvariable1][hilfsvariable2].figurauffeld != "":
        figur = welcheFigurStehtAufDemFeld(alleFelderInEinerListe2D[hilfvariable1][hilfsvariable2])
        if AmZug == "Weiss" and figur.color == "w":
            return False
        elif AmZug == "Schwarz" and figur.color == "b":
            return False
        else:
            return True
    else:
        return True

def movetoposIntXandY(mtp):
    i = 0
    i2 = 0
    x = 0
    y = 0
    while i != 8:
        while i2 != 8:
            if mtp == alleFelderInEinerListe2D[i][i2]:
                x = i
                y = i2
            i2 = i2 + 1
        i = i + 1
    return [x, y]

def zugMöglich(figur, moveToPos):
    global AmZug
    global SchachSchwarz
    global SchachWeiss
    if SchachSchwarz == True and AmZug == "Schwarz":
        return False
    elif SchachWeiss == True and AmZug == "Weiss":
        return False
    if figur.figurenart == Figurenarten[0]: #Bauernlogik
        i = 0
        while i < 8:
            if figur.figurenposition.feldnummer == alleFelderInEinerListe2D[i][1].feldnummer and moveToPos.feldnummer == alleFelderInEinerListe2D[i][3].feldnummer:
                if alleFelderInEinerListe2D[i][2].figurauffeld != "":
                    return False
                else:
                    if moveToPos.figurauffeld == "":
                        return True
            i = i+1
        i = 0
        while i < 8:
            if moveToPos.feldnummer == figur.figurenposition.feldnummer + 8:
                if moveToPos.figurauffeld == "":
                    return True
            i = i+1

        if moveToPos.figurauffeld != "" and moveToPos.feldnummer == figur.figurenposition.feldnummer + 9 \
                and figur.figurenposition.feldnummer != (1, 2, 3, 4, 5, 6, 7, 8)\
                or moveToPos.figurauffeld != "" and moveToPos.feldnummer == figur.figurenposition.feldnummer + 7 \
                and figur.figurenposition.feldnummer != (64, 63, 62, 61, 60, 59, 58, 57):
            if not isthisyouownfigur(movetoposIntXandY(moveToPos)[0], movetoposIntXandY(moveToPos)[1]):
                return False
            return True
    elif figur.figurenart == Figurenarten[6]:
        feldx = welchesFeldStehtDieFigur(figur, 2)[0]
        feldy = welchesFeldStehtDieFigur(figur, 2)[1]
        i = 0
        while i < 8:
            if figur.figurenposition.feldnummer == alleFelderInEinerListe2D[i][6].feldnummer and moveToPos.feldnummer == \
                    alleFelderInEinerListe2D[i][4].feldnummer:
                if alleFelderInEinerListe2D[i][5].figurauffeld != "":
                    return False
                else:
                    return True
            i = i + 1
        i = 0
        while i < 8:
            if moveToPos.feldnummer == figur.figurenposition.feldnummer - 8:
                return True
            i = i + 1
        if moveToPos.figurauffeld != "" and moveToPos.feldnummer == figur.figurenposition.feldnummer - 9 \
                and figur.figurenposition.feldnummer != (64, 63, 62, 61, 60, 59, 58, 57)\
                or moveToPos.figurauffeld != "" and moveToPos.feldnummer == figur.figurenposition.feldnummer - 7 \
                and figur.figurenposition.feldnummer != (1, 2, 3, 4, 5, 6, 7, 8):
            if not isthisyouownfigur(movetoposIntXandY(moveToPos)[0], movetoposIntXandY(moveToPos)[1]):
                return False
            return True
    elif figur.figurenart == Figurenarten[1] and AmZug == "Weiss" or figur.figurenart == Figurenarten[7] and AmZug == "Schwarz": #springerlogik

        x = welchesFeldStehtDieFigur(figur, 2)[0]
        y = welchesFeldStehtDieFigur(figur, 2)[1]

        if -1 < x+1 < 8 and -1 < y+2 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x + 1][y + 2].feldnummer: #alle Möglichen Züge für springer
            if moveToPos.figurauffeld != "":
                if not isthisyouownfigur(x+1, y+2):
                    return False
            return True
        if -1 < x-1 < 8 and -1 < y-2 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x - 1][y - 2].feldnummer:
            if moveToPos.figurauffeld != "":
                if not isthisyouownfigur(x-1, y-2):
                    return False
            return True
        if -1 < x+2 < 8 and -1 < y+1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x + 2][y + 1].feldnummer:
            if moveToPos.figurauffeld != "":
                if not isthisyouownfigur(x+2, y+1):
                    return False
            return True
        if -1 < x-2 < 8 and -1 < y-1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x - 2][y - 1].feldnummer:
            if moveToPos.figurauffeld != "":
                if not isthisyouownfigur(x-2, y-1):
                    return False
            return True
        if -1 < x+1 < 8 and -1 < y-2 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x + 1][y - 2].feldnummer:
            if moveToPos.figurauffeld != "":
                if not isthisyouownfigur(x+1, y-2):
                    return False
            return True
        if -1 < x-1 < 8 and -1 < y+2 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x - 1][y + 2].feldnummer:
            if moveToPos.figurauffeld != "":
                if not isthisyouownfigur(x-1, y+2):
                    return False
            return True
        if -1 < x-2 < 8 and -1 < y+1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x - 2][y + 1].feldnummer:
            if moveToPos.figurauffeld != "":
                if not isthisyouownfigur(x-2, y+1):
                    return False
            return True
        if -1 < x+2 < 8 and -1 < y-1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x + 2][y - 1].feldnummer:
            if moveToPos.figurauffeld != "":
                if not isthisyouownfigur(x+2, y-1):
                    return False
            return True
    elif figur.figurenart == Figurenarten[2] and AmZug == "Weiss" or figur.figurenart == Figurenarten[8] and AmZug == "Schwarz": #Laeuferlogik
        x = welchesFeldStehtDieFigur(figur, 2)[0]
        y = welchesFeldStehtDieFigur(figur, 2)[1]
        mtpx = 0
        mtpy = 0
        i = 0
        i2 = 0
        while i < 8:
            while i2 < 8:
                if moveToPos.feldnummer == alleFelderInEinerListe2D[i][i2].feldnummer:  # welches feld im 2d ist das mov to pos feld
                    mtpx = i
                    mtpy = i2
                i2 = i2 + 1
            i2 = 0
            i = i + 1
        i = 1
        xgrenze = 8 - x
        ygrenze = 8 - y
        ygrenzeMinus = 9 - ygrenze
        xgrenzeMinus = 9 - xgrenze
        mtpxMinusX = mtpx - x

        while i < xgrenze and i < ygrenze:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x + i][y + i].feldnummer: # alle zugmöglichkeiten für Laeufer
                i = 1
                e = 0
                if mtpxMinusX != 1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx-i][mtpy-i].figurauffeld == "":
                            return False
                        i = i + 1
                    i = 0
                    if not isthisyouownfigur(mtpx,mtpy):
                        return False
                    return True
                else:
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenze and i < ygrenzeMinus:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x + i][y - i].feldnummer:
                i = 1
                e = 0
                if mtpxMinusX != 1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx-i][mtpy+i].figurauffeld == "":
                            return False
                        i = i + 1
                    i = 0
                    if not isthisyouownfigur(mtpx,mtpy):
                        return False
                    return True
                else:
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenzeMinus and i < ygrenze:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x - i][y + i].feldnummer:
                i = -1
                e = 0
                if mtpxMinusX != -1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx + i*-1][mtpy - i*-1].figurauffeld == "":
                            return False
                        i = i - 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenzeMinus and i < ygrenzeMinus:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x - i][y - i].feldnummer:
                i = -1
                e = 0
                if mtpxMinusX != -1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx + i*-1][mtpy + i*-1].figurauffeld == "":
                            return False
                        i = i - 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
    elif figur.figurenart == Figurenarten[4] and AmZug == "Weiss" or figur.figurenart == Figurenarten[10] and AmZug == "Schwarz": #Turmlogik
        x = welchesFeldStehtDieFigur(figur, 2)[0]
        y = welchesFeldStehtDieFigur(figur, 2)[1]
        mtpx = 0
        mtpy = 0
        i = 0
        i2 = 0
        while i < 8:
            while i2 < 8:
                if moveToPos.feldnummer == alleFelderInEinerListe2D[i][
                    i2].feldnummer:  # welches feld im 2d ist das mov to pos feld
                    mtpx = i
                    mtpy = i2
                i2 = i2 + 1
            i2 = 0
            i = i + 1
        i = 1
        xgrenze = 8 - x
        ygrenze = 8 - y
        ygrenzeMinus = 9 - ygrenze
        xgrenzeMinus = 9 - xgrenze
        mtpxMinusX = mtpx - x
        mtpyMinusY = mtpy - y

        while i < xgrenze:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x + i][y].feldnummer: # alle zugmöglichkeiten für turm
                i = 1
                e = 0
                if mtpxMinusX != 1:
                    while i != mtpxMinusX:
                        if alleFelderInEinerListe2D[mtpx - i][mtpy].figurauffeld != "":
                            return False
                        i = i + 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < ygrenze:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x][y + i].feldnummer:
                i = 1
                e = 0
                if mtpyMinusY != 1:
                    while i != mtpyMinusY:
                        if alleFelderInEinerListe2D[mtpx][mtpy - i].figurauffeld != "":
                            return False
                        i = i + 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenzeMinus:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x - i][y].feldnummer:
                i = -1
                e = 0
                if mtpxMinusX != -1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx + i * -1][mtpy].figurauffeld == "":
                            return False
                        i = i - 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < ygrenzeMinus:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x][y - i].feldnummer:
                i = -1
                e = 0
                if mtpyMinusY != -1:
                    while i != mtpyMinusY:
                        if not alleFelderInEinerListe2D[mtpx][mtpy + i * -1].figurauffeld == "":
                            return False
                        i = i - 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
    elif figur.figurenart == Figurenarten[3] and AmZug == "Weiss" or figur.figurenart == Figurenarten[9] and AmZug == "Schwarz": #Logik für die Dame
        x = welchesFeldStehtDieFigur(figur, 2)[0]
        y = welchesFeldStehtDieFigur(figur, 2)[1]
        mtpx = 0
        mtpy = 0
        i = 0
        i2 = 0
        while i < 8:
            while i2 < 8:
                if moveToPos.feldnummer == alleFelderInEinerListe2D[i][
                    i2].feldnummer:  # welches feld im 2d ist das mov to pos feld
                    mtpx = i
                    mtpy = i2
                i2 = i2 + 1
            i2 = 0
            i = i + 1
        i = 1
        xgrenze = 8 - x
        ygrenze = 8 - y
        ygrenzeMinus = 9 - ygrenze
        xgrenzeMinus = 9 - xgrenze
        mtpxMinusX = mtpx - x
        mtpyMinusY = mtpy - y

        while i < xgrenze:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x + i][y].feldnummer:  # alle zugmöglichkeiten für turm
                i = 1
                e = 0
                if mtpxMinusX != 1:
                    while i != mtpxMinusX:
                        if alleFelderInEinerListe2D[mtpx - i][mtpy].figurauffeld != "":
                            return False
                        i = i + 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < ygrenze:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x][y + i].feldnummer:
                i = 1
                e = 0
                if mtpyMinusY != 1:
                    while i != mtpyMinusY:
                        if alleFelderInEinerListe2D[mtpx][mtpy - i].figurauffeld != "":
                            return False
                        i = i + 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenzeMinus:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x - i][y].feldnummer:
                i = -1
                e = 0
                if mtpxMinusX != -1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx + i * -1][mtpy].figurauffeld == "":
                            return False
                        i = i - 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < ygrenzeMinus:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x][y - i].feldnummer:
                i = -1
                e = 0
                if mtpyMinusY != -1:
                    while i != mtpyMinusY:
                        if not alleFelderInEinerListe2D[mtpx][mtpy + i * -1].figurauffeld == "":
                            return False
                        i = i - 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenze and i < ygrenze:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x + i][
                y + i].feldnummer:  # alle zugmöglichkeiten für Laeufer
                i = 1
                e = 0
                if mtpxMinusX != 1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx - i][mtpy - i].figurauffeld == "":
                            return False
                        i = i + 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenze and i < ygrenzeMinus:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x + i][y - i].feldnummer:
                i = 1
                e = 0
                if mtpxMinusX != 1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx - i][mtpy + i].figurauffeld == "":
                            return False
                        i = i + 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenzeMinus and i < ygrenze:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x - i][y + i].feldnummer:
                i = -1
                e = 0
                if mtpxMinusX != -1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx + i * -1][mtpy - i * -1].figurauffeld == "":
                            return False
                        i = i - 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
        i = 1
        while i < xgrenzeMinus and i < ygrenzeMinus:
            if moveToPos.feldnummer == alleFelderInEinerListe2D[x - i][y - i].feldnummer:
                i = -1
                e = 0
                if mtpxMinusX != -1:
                    while i != mtpxMinusX:
                        if not alleFelderInEinerListe2D[mtpx + i * -1][mtpy + i * -1].figurauffeld == "":
                            return False
                        i = i - 1
                    i = 0
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                else:
                    if not isthisyouownfigur(mtpx, mtpy):
                        return False
                    return True
                return False
                e = 0
                i = 0
            i = i + 1
    elif figur.figurenart == Figurenarten[5] and AmZug == "Weiss" or figur.figurenart == Figurenarten[11] and AmZug == "Schwarz": #Koeniglogik
        x = welchesFeldStehtDieFigur(figur, 2)[0]
        y = welchesFeldStehtDieFigur(figur, 2)[1]
        i = 1
        if -1 < x+1 < 8 and -1 < y < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x + 1][y].feldnummer: #alle Möglichen Züge für springer
            if not isthisyouownfigur(x+1, y):
                return False
            return True
        elif -1 < x-1 < 8 and -1 < y < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x - 1][y].feldnummer:
            if not isthisyouownfigur(x-1,y):
                return False
            return True
        elif -1 < x < 8 and -1 < y+1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x][y + 1].feldnummer:
            if not isthisyouownfigur(x, y+1):
                return False
            return True
        elif -1 < x < 8 and -1 < y-1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x][y - 1].feldnummer:
            if not isthisyouownfigur(x, y-1):
                return False
            return True
        elif -1 < x+1 < 8 and -1 < y+1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x + 1][y + 1].feldnummer:
            if not isthisyouownfigur(x+1, y+1):
                return False
            return True
        elif -1 < x-1 < 8 and -1 < y+1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x - 1][y + 1].feldnummer:
            if not isthisyouownfigur(x-1, y+1):
                return False
            return True
        elif -1 < x+1 < 8 and -1 < y-1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x + 1][y - 1].feldnummer:
            if not isthisyouownfigur(x+1, y-1):
                return False
            return True
        elif -1 < x-1 < 8 and -1 < y-1 < 8 and moveToPos.feldnummer == alleFelderInEinerListe2D[x - 1][y - 1].feldnummer:
            i = 0
            if not isthisyouownfigur(x-1, y-1):
                return False
            return True
        else:
            return False

def isCheck(color):
    if color == "Schwarz":
        FigurenZaehler = 15 # wenn Weiss übergeben wird checkt es ob die weissen figuren den schwarzen könig schah setzten
        Koenigfeld = KoenigWeiss.figurenposition
    else:
        FigurenZaehler = 0 # anders herum
        Koenigfeld = KoenigSchwarz.figurenposition
    i = 0
    while i < 15:
        if alleFigurenInEinerListe2wegenIfcheck[FigurenZaehler].isactive and \
                zugMöglich(alleFigurenInEinerListe2wegenIfcheck[FigurenZaehler], Koenigfeld):
            return True
        FigurenZaehler = FigurenZaehler + 1
        i = i + 1

    return False


def updateField(window):
    window.blit(SpielBrettBild, (50, 15))
    #alle weißen figuren refreshen
    if aktuellMarkiert is not None:
        window.blit(MarkierungBild, (aktuellMarkiert.felddaten[0], aktuellMarkiert.felddaten[1]))
    if fieldsthatarepossibleLenght != 0:
        for i in range(fieldsthatarepossibleLenght):
            window.blit(ZugMoeglichBild, (fieldsthatarepossible[i].felddaten[0], fieldsthatarepossible[i].felddaten[1]))
    if aBauerWeiss.isactive:
        window.blit(BauerWeissBild, (aBauerWeiss.figurenposition.felddaten[0], aBauerWeiss.figurenposition.felddaten[1]))
    if bBauerWeiss.isactive:
        window.blit(BauerWeissBild, (bBauerWeiss.figurenposition.felddaten[0], bBauerWeiss.figurenposition.felddaten[1]))
    if cBauerWeiss.isactive:
        window.blit(BauerWeissBild, (cBauerWeiss.figurenposition.felddaten[0], cBauerWeiss.figurenposition.felddaten[1]))
    if dBauerWeiss.isactive:
        window.blit(BauerWeissBild, (dBauerWeiss.figurenposition.felddaten[0], dBauerWeiss.figurenposition.felddaten[1]))
    if eBauerWeiss.isactive:
        window.blit(BauerWeissBild, (eBauerWeiss.figurenposition.felddaten[0], eBauerWeiss.figurenposition.felddaten[1]))
    if fBauerWeiss.isactive:
        window.blit(BauerWeissBild, (fBauerWeiss.figurenposition.felddaten[0], fBauerWeiss.figurenposition.felddaten[1]))
    if gBauerWeiss.isactive:
        window.blit(BauerWeissBild, (gBauerWeiss.figurenposition.felddaten[0], gBauerWeiss.figurenposition.felddaten[1]))
    if hBauerWeiss.isactive:
        window.blit(BauerWeissBild, (hBauerWeiss.figurenposition.felddaten[0], hBauerWeiss.figurenposition.felddaten[1]))
    if aTurmWeiss.isactive:
        window.blit(TurmWeissBild, (aTurmWeiss.figurenposition.felddaten[0], aTurmWeiss.figurenposition.felddaten[1]))
    if bSpringerWeiss.isactive:
        window.blit(SpringerWeissBild, (bSpringerWeiss.figurenposition.felddaten[0], bSpringerWeiss.figurenposition.felddaten[1]))
    if cLaeuferWeiss.isactive:
        window.blit(LaeuferWeissBild, (cLaeuferWeiss.figurenposition.felddaten[0], cLaeuferWeiss.figurenposition.felddaten[1]))
    if DameWeiss.isactive:
        window.blit(DameWeissBild, (DameWeiss.figurenposition.felddaten[0], DameWeiss.figurenposition.felddaten[1]))
    if KoenigWeiss.isactive:
        window.blit(KoenigWeissBild, (KoenigWeiss.figurenposition.felddaten[0], KoenigWeiss.figurenposition.felddaten[1]))
    if fLaeuferWeiss.isactive:
        window.blit(LaeuferWeissBild, (fLaeuferWeiss.figurenposition.felddaten[0], fLaeuferWeiss.figurenposition.felddaten[1]))
    if gSpringerWeiss.isactive:
        window.blit(SpringerWeissBild, (gSpringerWeiss.figurenposition.felddaten[0], gSpringerWeiss.figurenposition.felddaten[1]))
    if hTurmWeiss.isactive:
        window.blit(TurmWeissBild, (hTurmWeiss.figurenposition.felddaten[0], hTurmWeiss.figurenposition.felddaten[1]))
    #alle schwarzen figuren refreshen
    if aBauerSchwarz.isactive:
        window.blit(BauerSchwarzBild, (aBauerSchwarz.figurenposition.felddaten[0], aBauerSchwarz.figurenposition.felddaten[1]))
    if bBauerSchwarz.isactive:
        window.blit(BauerSchwarzBild, (bBauerSchwarz.figurenposition.felddaten[0], bBauerSchwarz.figurenposition.felddaten[1]))
    if cBauerSchwarz.isactive:
        window.blit(BauerSchwarzBild, (cBauerSchwarz.figurenposition.felddaten[0], cBauerSchwarz.figurenposition.felddaten[1]))
    if dBauerSchwarz.isactive:
        window.blit(BauerSchwarzBild, (dBauerSchwarz.figurenposition.felddaten[0], dBauerSchwarz.figurenposition.felddaten[1]))
    if eBauerSchwarz.isactive:
        window.blit(BauerSchwarzBild, (eBauerSchwarz.figurenposition.felddaten[0], eBauerSchwarz.figurenposition.felddaten[1]))
    if fBauerSchwarz.isactive:
        window.blit(BauerSchwarzBild, (fBauerSchwarz.figurenposition.felddaten[0], fBauerSchwarz.figurenposition.felddaten[1]))
    if gBauerSchwarz.isactive:
        window.blit(BauerSchwarzBild, (gBauerSchwarz.figurenposition.felddaten[0], gBauerSchwarz.figurenposition.felddaten[1]))
    if hBauerSchwarz.isactive:
        window.blit(BauerSchwarzBild, (hBauerSchwarz.figurenposition.felddaten[0], hBauerSchwarz.figurenposition.felddaten[1]))
    if aTurmSchwarz.isactive:
        window.blit(TurmSchwarzBild, (aTurmSchwarz.figurenposition.felddaten[0], aTurmSchwarz.figurenposition.felddaten[1]))
    if bSpringerSchwarz.isactive:
        window.blit(SpringerSchwarzBild,(bSpringerSchwarz.figurenposition.felddaten[0], bSpringerSchwarz.figurenposition.felddaten[1]))
    if cLaeuferSchwarz.isactive:
        window.blit(LaeuferSchwarzBild, (cLaeuferSchwarz.figurenposition.felddaten[0], cLaeuferSchwarz.figurenposition.felddaten[1]))
    if DameSchwarz.isactive:
        window.blit(DameSchwarzBild, (DameSchwarz.figurenposition.felddaten[0], DameSchwarz.figurenposition.felddaten[1]))
    if KoenigSchwarz.isactive:
        window.blit(KoenigSchwarzBild, (KoenigSchwarz.figurenposition.felddaten[0], KoenigSchwarz.figurenposition.felddaten[1]))
    if fLaeuferSchwarz.isactive:
        window.blit(LaeuferSchwarzBild,(fLaeuferSchwarz.figurenposition.felddaten[0], fLaeuferSchwarz.figurenposition.felddaten[1]))
    if gSpringerSchwarz.isactive:
        window.blit(SpringerSchwarzBild,(gSpringerSchwarz.figurenposition.felddaten[0], gSpringerSchwarz.figurenposition.felddaten[1]))
    if hTurmSchwarz.isactive:
        window.blit(TurmSchwarzBild, (hTurmSchwarz.figurenposition.felddaten[0], hTurmSchwarz.figurenposition.felddaten[1]))

def markThePossibeleMoves(mark):
    global fieldsthatarepossible
    global fieldsthatarepossibleLenght
    figurtocheck = None
    i = 0
    while i < 31:
        if alleFigurenInEinerListe[i].figurenposition == mark:
            figurtocheck = alleFigurenInEinerListe[i]
        i = i + 1
    i = 0
    listpointer = 0
    while i < 64:
        if zugMöglich(figurtocheck, alleFelderInEinerListe[i]):
            try:
                fieldsthatarepossible[listpointer] = alleFelderInEinerListe[i]
            except IndexError:
                fieldsthatarepossible.append(alleFelderInEinerListe[i])
            listpointer = listpointer + 1
        i = i + 1
    fieldsthatarepossibleLenght = len(fieldsthatarepossible)
    print(fieldsthatarepossible)

def ifClick():
    global AmZug
    global aktuellMarkiert
    global aktuellGeKlickt
    global fieldsthatarepossibleLenght
    global fieldsthatarepossible
    mouse = pygame.mouse.get_pos()
    i = 0
    while i < len(alleFelderInEinerListe):  # schaut auf welches feld du geklickt hast
        if alleFelderInEinerListe[i].felddaten[1] < mouse[1] < alleFelderInEinerListe[i].felddaten[3]:
            if alleFelderInEinerListe[i].felddaten[0] < mouse[0] < alleFelderInEinerListe[i].felddaten[2]:
                aktuellGeKlickt = alleFelderInEinerListe[i]
        i = i+1
    if aktuellMarkiert is None:
        if aktuellGeKlickt.figurauffeld != "":  #markiert wenn weiss am zug ist
            if AmZug == "Weiss" and aktuellGeKlickt.figurauffeld == Figurenarten[0] \
                    or AmZug == "Weiss" and aktuellGeKlickt.figurauffeld == Figurenarten[1] \
                    or AmZug == "Weiss" and aktuellGeKlickt.figurauffeld == Figurenarten[2] \
                    or AmZug == "Weiss" and aktuellGeKlickt.figurauffeld == Figurenarten[3] \
                    or AmZug == "Weiss" and aktuellGeKlickt.figurauffeld == Figurenarten[4] \
                    or AmZug == "Weiss" and aktuellGeKlickt.figurauffeld == Figurenarten[5]:
                aktuellGeKlickt.Clicked()
                aktuellMarkiert = aktuellGeKlickt
                print(aktuellMarkiert.figurauffeld)
                print("wurde markiert")
                markThePossibeleMoves(aktuellMarkiert)
            elif AmZug == "Schwarz" and aktuellGeKlickt.figurauffeld == Figurenarten[6] \
                    or AmZug == "Schwarz" and aktuellGeKlickt.figurauffeld == Figurenarten[7] \
                    or AmZug == "Schwarz" and aktuellGeKlickt.figurauffeld == Figurenarten[8] \
                    or AmZug == "Schwarz" and aktuellGeKlickt.figurauffeld == Figurenarten[9] \
                    or AmZug == "Schwarz" and aktuellGeKlickt.figurauffeld == Figurenarten[10] \
                    or AmZug == "Schwarz" and aktuellGeKlickt.figurauffeld == Figurenarten[11]:  #markiert wenn Schwarz am zug ist
                aktuellGeKlickt.Clicked()
                aktuellMarkiert = aktuellGeKlickt
                print(aktuellMarkiert.figurauffeld)
                print("wurde markiert")
                markThePossibeleMoves(aktuellMarkiert)
    else:  # Demarkiert entweder die Felder oder Markiert andere oder macht den Zug
        if aktuellMarkiert.felddaten[1] < mouse[1] < aktuellMarkiert.felddaten[3]: #demarkieren falls man auf die selbe figur nochmals clickt
            if aktuellMarkiert.felddaten[0] < mouse[0] < aktuellMarkiert.felddaten[2]:
                aktuellMarkiert.deClicked()
                aktuellMarkiert = None
                print("markierung gelöscht aufgrund von erneutem klicken")
                fieldsthatarepossibleLenght = 0
                fieldsthatarepossible.clear()
        if aktuellMarkiert is not None:
            if aktuellGeKlickt.figurauffeld != "" and AmZug == "Weiss" and aktuellGeKlickt.figurauffeld == Figurenarten[0] \
                    or aktuellGeKlickt.figurauffeld == Figurenarten[1] and AmZug == "Weiss"\
                    or aktuellGeKlickt.figurauffeld == Figurenarten[2] and AmZug == "Weiss"\
                    or aktuellGeKlickt.figurauffeld == Figurenarten[3] and AmZug == "Weiss"\
                    or aktuellGeKlickt.figurauffeld == Figurenarten[4] and AmZug == "Weiss"\
                    or aktuellGeKlickt.figurauffeld == Figurenarten[5] and AmZug == "Weiss": # demarkieren wenn man auf eine andere figur der weissen Farbe tippt
                aktuellMarkiert.deClicked()
                aktuellMarkiert = aktuellGeKlickt
                print("markierung geaendert auf")
                print(aktuellMarkiert.figurauffeld)
                fieldsthatarepossibleLenght = 0
                fieldsthatarepossible.clear()
                markThePossibeleMoves(aktuellMarkiert)
            if aktuellGeKlickt.figurauffeld != "" and AmZug == "Schwarz" and aktuellGeKlickt.figurauffeld == Figurenarten[6] \
                    or aktuellGeKlickt.figurauffeld == Figurenarten[7] and AmZug == "Schwarz"\
                    or aktuellGeKlickt.figurauffeld == Figurenarten[8] and AmZug == "Schwarz"\
                    or aktuellGeKlickt.figurauffeld == Figurenarten[9] and AmZug == "Schwarz"\
                    or aktuellGeKlickt.figurauffeld == Figurenarten[10] and AmZug == "Schwarz"\
                    or aktuellGeKlickt.figurauffeld == Figurenarten[11] and AmZug == "Schwarz": # demarkieren  wenn man auf eine andere figur der Schwarzen Farbe tippt
                aktuellMarkiert.deClicked()
                aktuellMarkiert = aktuellGeKlickt
                print("markierung geaendert auf")
                print(aktuellMarkiert.figurauffeld)
                fieldsthatarepossibleLenght = 0
                fieldsthatarepossible.clear()
                markThePossibeleMoves(aktuellMarkiert)
        if aktuellMarkiert is not None: # Figurenzug wenn leeres feld oder Schlagen
            i2 = 0
            while i2 < 32: # schaut welche figur bewegt werden soll
                if alleFigurenInEinerListe[i2].figurenposition == aktuellMarkiert:
                    aktuellefigur = alleFigurenInEinerListe[i2]
                i2 = i2 + 1
            if not zugMöglich(aktuellefigur, aktuellGeKlickt): #If zugmöglich
                return False
            voidTheFigur(aktuellGeKlickt)
            aktuellefigur.figurenposition = aktuellGeKlickt  # Figur wird verschoben
            aktuellGeKlickt.figurauffeld = aktuellMarkiert.figurauffeld
            aktuellMarkiert.figurauffeld = ""                               # Markirung ist gelöscht
            if AmZug == "Weiss":                                            # Zug wird gewechselt
                print("Schwarz am Zug")
                AmZug = "Schwarz"
            else:
                print("Weiss am Zug")
                AmZug = "Weiss"
            aktuellMarkiert = None
            print("markierung geloescht (zug gezogen)")
            fieldsthatarepossibleLenght = 0
            fieldsthatarepossible.clear()
            updateField(fenster)                                                    #fenster wird refreshed


def start(): # startfunktion die alles vorbereitet und die main schleife laufen lässt
    pygame.init()
    global fenster
    fenster = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()

    aktive = True
    while aktive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aktive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ifClick()
        pygame.display.flip()
        clock.tick(fps)
        updateField(fenster)


if __name__ == '__main__':
    start()