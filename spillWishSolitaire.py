


########################################################
############            RULES               ############
########################################################

#Take any cards that are pairs of the same kind, regardless of suit - two 10's, two Kings, etc. and clear them away.
#To win the game, you must clear away all piles in pairs.



import random
import time
import pickle
sparSymbol='\u2660'
ruterSymbol='\u2666'
kloverSymbol='\u2663'
hjerterSymbol='\u2665'
symboler = [sparSymbol, ruterSymbol,kloverSymbol,hjerterSymbol]
kort = ["7","8","9","10","J","Q","K","A"]
kortstokk = []
GUI = []
testGUI = []
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []

def meny():
    while True:
        meny = str(input(
"""
1 - Nytt Spill
2 - Lagre Spill
3 - Hent Lagret Spill
4 - Avslutt

Velg(1-4): """))
        if meny == "1":
            reset()
            start()
        elif meny == "2":
            print("Data Lagret!\nNB!: Start programmet på nytt for å kunne laste inn det lagrede spillet!")
            save()


        elif meny == "3":
            load()
        elif meny == "4":
            lagre = str(input("Vil du lagre først?(Y/N): ")).upper()
            if lagre == "Y":
                save()
                print("Takk for nå!")
                quit()
            elif lagre == "N":
                print("Takk for nå!")
                quit()
            else: print("Ikke igjenkjent!")
        else:
            print("Ugyldig! Velg mellom 1-4!")

def lagBunker():
    for suits in symboler:                  #generer kortstokken
        for i in kort:
            kortstokk.append(suits+i)
    random.shuffle(kortstokk)

    #bruker tilfeldig generert bunke og lager korstokk a-h
    for i in kortstokk:
        if len(a) < 4:
            a.append(i)
        elif len(b) < 4:
            b.append(i)
        elif len(c) < 4:
            c.append(i)
        elif len(d) < 4:
            d.append(i)
        elif len(e) < 4:
            e.append(i)
        elif len(f) < 4:
            f.append(i)
        elif len(g) < 4:
            g.append(i)
        elif len(h) < 4:
            h.append(i)
def reset():
    a.clear()
    b.clear()
    c.clear()
    d.clear()
    e.clear()
    f.clear()
    g.clear()
    h.clear()
    kortstokk.clear()
    GUI.clear()
    lagBunker()
    return


def start():

    laggui()
    visSpill()
    if sjekkMuligeTrekk() != True:
        print("Du har tapt!")
        time.sleep(3)
        reset()
        meny()

    while True:          #Det er garantert en bedre måte å gjøre dette på, men her ble det en hau med if/elif

        velgBunke1 = str(input("Velg bunke 1(<X> for å avbryte): ")).lower()
        if velgBunke1 == "x":
            meny()
            break
        if len(velgBunke1) > 1:
            print("Velg en bunke per linje!")
            time.sleep(2)
            start()
        elif velgBunke1 == "a":
            velgBunke1 = a
        elif velgBunke1 == "b":
            velgBunke1 = b
        elif velgBunke1 == "c":
            velgBunke1 = c
        elif velgBunke1 == "d":
            velgBunke1 = d
        elif velgBunke1 == "e":
            velgBunke1 = e
        elif velgBunke1 == "f":
            velgBunke1 = f
        elif velgBunke1 == "g":
            velgBunke1 = g
        elif velgBunke1 == "h":
            velgBunke1 = h
        else:
            print("Ugyldig! Velg bunke a-h!")
            start()
        velgBunke2 = str(input("Velg bunke 2(<X> for å avbryte): ")).lower()
        if velgBunke2 == "x":
            meny()
            break
        if len(velgBunke2) > 1:
            print("Velg en bunke per linje!")
            time.sleep(2)
            start()
        if velgBunke2 == "a":
            velgBunke2 = a
        elif velgBunke2 == "b":
            velgBunke2 = b
        elif velgBunke2 == "c":
            velgBunke2 = c
        elif velgBunke2 == "d":
            velgBunke2 = d
        elif velgBunke2 == "e":
            velgBunke2 = e
        elif velgBunke2 == "f":
            velgBunke2 = f
        elif velgBunke2 == "g":
            velgBunke2 = g
        elif velgBunke2 == "h":
            velgBunke2 = h
        else:
            print("Ugyldig! Velg bunke a-h!")
            start()
        if velgBunke1 == velgBunke2:
            print("Du kan ikke velge samme bunke!")
            time.sleep(2)
            start()
        if hentToppKort(velgBunke1)[1:] != hentToppKort(velgBunke2)[1:]:
            print("Ugyldig bevegelse!")
        if hentToppKort(velgBunke1)[1:] == hentToppKort(velgBunke2)[1:]:
            GUI.clear()
            velgBunke1.remove(hentToppKort(velgBunke1))
            velgBunke2.remove(hentToppKort(velgBunke2))
            start()
        if len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0 and len(e) == 0 and len(f) == 0 and len(g) == 0 and len(h) == 0:
            print("GG! Du har vunnet!")
            time.sleep(2)
            meny()

def sjekkMuligeTrekk():  #sjekker om spillet kan fortsette
    sjekk = []
    sjekk.clear()
    if len(a) != 0:
        sjekk.append(hentToppKort(a)[1:])
    if len(b) != 0:
        sjekk.append(hentToppKort(b)[1:])
    if len(c) != 0:
        sjekk.append(hentToppKort(c)[1:])
    if len(d) != 0:
        sjekk.append(hentToppKort(d)[1:])
    if len(e) != 0:
        sjekk.append(hentToppKort(e)[1:])
    if len(f) != 0:
        sjekk.append(hentToppKort(f)[1:])
    if len(g) != 0:
        sjekk.append(hentToppKort(g)[1:])
    if len(h) != 0:
        sjekk.append(hentToppKort(h)[1:])


    sjekkDup = any(sjekk.count(el) > 1 for el in sjekk)

    return sjekkDup




def grensesnitt(bunke, kort, antall): #lager en modul for spillets gui
    GUI = \
f"""
     {bunke}  
 [ {kort} ] 
     {antall}  
"""
    return GUI


def hentToppKort(bunke):

    toppKort = bunke[:1]
    for item in toppKort:
        item.strip("[']\n")
        toppKort = item


    return toppKort


def lengde(bunke):  #egentlig ikke nødvendig, men yolo
    lengde = len(bunke)
    return lengde


def laggui():     #setter sammen modul for alle bunkene for å lage gui
    aBunke = (grensesnitt("A", hentToppKort(a), lengde(a)))
    bBunke = (grensesnitt("B", hentToppKort(b), lengde(b)))
    cBunke = (grensesnitt("C", hentToppKort(c), lengde(c)))
    dBunke = (grensesnitt("D", hentToppKort(d), lengde(d)))
    eBunke = (grensesnitt("E", hentToppKort(e), lengde(e)))
    fBunke = (grensesnitt("F", hentToppKort(f), lengde(f)))
    gBunke = (grensesnitt("G", hentToppKort(g), lengde(g)))
    hBunke = (grensesnitt("H", hentToppKort(h), lengde(h)))

    if len(GUI) != 8:
        GUI.append(aBunke)
        GUI.append(bBunke)
        GUI.append(cBunke)
        GUI.append(dBunke)
        GUI.append(eBunke)
        GUI.append(fBunke)
        GUI.append(gBunke)
        GUI.append(hBunke)
    else: pass

def visSpill():   #setter opp moduler fra laggui() side-by-side
    gui_split = [gui.split("\n") for gui in GUI]
    zipped = zip(*gui_split)
    for e in zipped:
        print("".join(e))

def save():   #lagrer bunkene i pickle
    ut = open("lagret", "wb")
    pickle.dump(a, ut)
    pickle.dump(b, ut)
    pickle.dump(c, ut)
    pickle.dump(d, ut)
    pickle.dump(e, ut)
    pickle.dump(f, ut)
    pickle.dump(g, ut)
    pickle.dump(h, ut)
    ut.close()

tempP = []
def pakkUt(start, slutt, bunke):  #pakker ut listene fra listen tempP

    for i in tempP[start:slutt]:
        for v in i:
            bunke.append(v)
    return
def load():    #legger lagrede bunker tilbake der de kom fra slik, prossesen kan kjøre igjen(Bygge bunkene og  GUI)
    reset()
    a.clear()
    b.clear()
    c.clear()
    d.clear()
    e.clear()
    f.clear()
    g.clear()
    h.clear()

    with open("lagret", 'rb') as fil:
        try:
            while True:
                tempP.append(pickle.load(fil))

        except EOFError:
            pass
        pakkUt(0, 1, a)
        pakkUt(1, 2, b)
        pakkUt(2, 3, c)
        pakkUt(3, 4, d)
        pakkUt(4, 5, e)
        pakkUt(5, 6, f)
        pakkUt(6, 7, g)
        pakkUt(7, 8, h)
    fil.close()

    start()
    return
lagBunker()
meny()
