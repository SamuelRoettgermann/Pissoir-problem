#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

# Dynamische Programmierung: Abspeichern Zeitaufwendiger Berechnungen die häufiger gebraucht werden.
# Vorteil: Fakultät ist danach ein vernachlässigbarer Faktor
# nachteil: n*n*log(n) Speicherplatz verbrauch da n! eine O(n * log(n))-stellige Zahl ist.
#
# Leider ist die Fakultät nicht der einzige begrenzende Faktor: die pure Multiplikation von erg * fakultät()
# braucht etwa halbsolang wie die fakultät. Daher nicht in Verwendung.
class Factorial(dict):
    def __missing__(self, key):
        value = self[key] = key * self[key-1]
        return value
    
FAK = Factorial()
FAK[0] = 1


def get_maxis(L):
    '''
    Gibt die maximalen Lückengrößen zurück, wobei wir immer auf die nächste gerade Zahl runden,
    da eine 4er Lücke ebenso wie eine 3er Lücke dich zwingt, mit nur ein Pissoir abstand halten 
    zu können.
    
    Wenn also 12 die maximale Lückengröße ist, so gibt man alle Lücken der größe 12 (als maxis) 
    und 11 (als maxis2) zurück. Ebenso wenn 11 die maximale Lückengröße ist, wobei dann die Liste 
    maxis naturgemäß leer sein muss, da es keine 12er gibt.
    
    maxi wäre in beiden Fällen einfach der Wert 12, also die gerade Zahl die in maxis enthalten ist,
    wenn maxis nicht leer wäre.
    '''
    maxis = L.pop()
    maxi = maxis[0]
    
    # Fall: es gibt keine maximalen geraden Lückenlängen
    if maxi % 2: 
        return  [], maxis
    
    #Fall: es gibt gerade und ungerade (maximale) Lückengrößen
    if L and L[-1][0] == maxi-1: 
        return maxis, L.pop()
    
    #Fall: es gibt nur gerade (maximale) Lückengrößen
    return maxis, []
    
    
def einfügen(L, l): 
    '''
    Fügt eine Lückenliste l in L sortiert ein.
    
    Da L maximal 4 verschiede Listen beinhalten kann, lohnt es sich nicht, L als Suchbaum oder ähnliches 
    zu implementieren.
    
    '''
    
    # Wir wollen keine Leeren Listen mitschleppen.
    if not l: return


    for i, l_i in enumerate(L):
        # Wenn es die Lückengröße bereits gibt, werden die Lückenlisten zusammengefügt.
        if l_i[0] == l[0]:
            l_i += l
            return
        # Wenn nicht, dann wird die Lückenliste an der ensprechenden Stelle eingefügt.
        elif l_i[0] > l[0]:
            L.insert(i, l)
            return
    
    # wenn alle Lücken kleiner sind als die in l, wird l hinten angehangen. (In diesem Fall wird L vorher immer leer gewesen sein)
    L.append(l)

def restliche_besucher(L, rand):
    erg = 1
    while True:
        # maxi = maximale entfernung, die die nächsten Besucher einhalten können = lückengröße / 2 bei geraden Lücken bzw (lückengröße+1) / 2 bei ungeraden.
        maxi = (L[-1][0]+1)//2
        
        # nerfiger Randfall. Wenn die Randlücke die größte Lücke ist. (Erinnerung Randlückengröße ist 2 mal ihre tatsächliche Größe)
        # Die Person hat keine wahl und muss sind an den Randstellen. (erg bleibt gleich)
        # Füge die neue Lücke (echte größe - 1 also k//2 - 1) als standardfall ein.
        # Danach gibt es keine Reandlücke mehr (k = 0)
        if maxi < rand:
            einfügen(L, [rand - 1])
            rand = 0
        
        # Wenn andere Lücken genauso groß sind wie die Randlücke, wird diese mit eingearbeitet.
        # Sie verhält sich wie eine ungerade Lücke, mit dem einzigen Unterschied, dass sie am Ende 
        # nur eine neue Lücke erzeugt und keine zwei.
        rand_verwenden = 0
        if maxi == rand:
            rand_verwenden = 1
            rand = 0
            
        maxis, maxis2 = get_maxis(L)
        
        # Wenn es nur noch Lücken der größe 1 und 2 gibt, hat der Rest freie Wahl. Also Fakultät der restlichen Plätze.
        # Restliche Plätze = 2 * 2er Lücken + 1 * 1er-Lücken, wenn die Randlücke größe 1 hat (k = 2) wird sie auch dazu gezählt.
        if maxi == 1:
            return erg * math.factorial(2*len(maxis) + len(maxis2) + rand_verwenden)
        
        # Wir betrachten die nächsten maxis + maxis2 viele Toilettengänger. Diese müssen alle die Lücken von maxis und maxis2 besetzen.
        # Dafür haben sie fakultät(maxis + maxis2) - viele Möglichkeiten die Lücken auszuwählen und jeder der eine gerade Lücke besetzt
        # hat 2 möglichkeiten welchen der mittleren Plätze er wählt. Also nochmal zusätzlich 2^maxis viele Möglichkeiten.
        erg *= math.factorial(len(maxis) + len(maxis2) + rand_verwenden) * 2**len(maxis)
            
        # die neuen Lücken: die geraden Lücken zerfallen in maxi//2 und maxi//2-1 große Lücken
        # und die ungeraden zerfallen in 2 maxi//2-1 große Lücken die dann direkt eingefügt werden
        l1 = len(maxis) * [maxi]
        einfügen(L, l1)  
        l2 = (len(maxis) + 2*len(maxis2) + rand_verwenden) * [maxi-1]
        einfügen(L, l2)
        
"""

Damit man sich ein Bild macht, hier ein Beispiel in der Mitte der Berechnung zu n = 36:

L = [[2, 2, 2, 2], [3, 3], [4, 4, 4]]

L speichert die Größe der Lücken die es zwischen den besetzten Pissoirs gibt.
Das bedeutet, dass es in den 36 Toiletten noch 4 2er-Lücken gibt, 2 3er-Lücken und 3-4er Lücken.
Wie sie angeordnet sind ist egal. Es ist klar, dass der nächste Besucher in die Mitte einer 3er 
oder einer 4er Lücke gehen muss, sagen wir eine 4er Lücke. Diese würde dann ein eine 1er und eine 
2er Lücke zerfallen:

L = [[1], [2, 2, 2, 2, 2], [3, 3], [4, 4]] # (Achtung, wie gleich erklärt, überspringt der Algorithmus diesen Zwischenschritt)

Der nächste Besucher muss wieder eine der restlichen 4 Lücken der größe 3 oder 4 nehmen.

Daraus ergibt sich, dass die 5 Lücken vom anfang, von den nächsten 5 Personen in beliebiger Reinfolge besetzt werden.
Das sind 5! Möglichkeiten die Lücken aufzuteilen, wobei bei den 4er-Lücken man immer zwischen den linken und rechten Platz 
wählen kann. Also 5! * 2^3 Möglichkeiten insgesamt. Danach sieht L immer so aus:

L = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2]] 

Die 2 3er-Lücken zerfallen in 4 1er-Lücken und die 3 4er-Lücken in 3 1er und 3 2er-Lücken. 
Ab diesen Schritt gibt es noch 21 freie Plätze die jeder direkt neben einer Person sind.
Damit können die restlichen 21 Personen frei wählen und es gibt nochmal 21! weitere Möglichkeiten, für
jede der bisherigen Ausgänge. Ergibgt 5! * 2^3 * 21! Möglichkeiten ausgehend von diesem L. 
"""
def möglichkeiten_pissoirs(n):
    
    # Algorithmus funktioniert nur für n >= 4, da rechts > 0 sein muss.
    if n <= 3:
        return 2**(n-1)
    
    # Der erste entscheidet sich frei für eine Position von 1 bin n, wobei wir
    # nur die erste Hälfte berechnen, die zweite Hälft ist symmetrisch.
    # links = größe der linken (kleineren Lücke)
    # rechts größe der größeren Lücke, nachdem sich die zweite Person an den rechten Rand
    # gestellt hat. Die zweiter Person hat nur eine Wahl, wenn n ungerade und Person 1
    # exakt die Mitte besetzt. Das ist zufällig auch der einzige Fall, der für Person 1
    # gespiegelt keinen neuen Fall ergibt. Daraus folgt, dass wir einfach das Ergebnis für 
    # Person 2 statt für Person 1 verdoppeln müssen. Es hebt sich also wieder auf.
    
    erg = 0
    for links in range((n+1)//2):
        rechts = n - links - 2
        # L gibt an, wie groß die Lücken sind. am Anfang gibt es zwei Lücken, die Zwischen Person 1 und Person 2
        # und die Randlücke. Die Randlücke ist ein Spezialfall, daher wird sie nicht in L verwaltet sondern der Funktion
        # separat übergeben.
        L = [[rechts]]
        erg += restliche_besucher(L, links)
    return 2*erg


# In[13]:


get_ipython().run_line_magic('time', 'möglichkeiten_pissoirs(4000)')


# In[ ]:




