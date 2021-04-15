from kortlek import kortleken
import random
from random import shuffle
import matplotlib.pyplot as plt

#Väljer ut 5 kort från kortleken
class hand:
    #kontstruktor
    def __init__(self, num=5):
        self.lek = kortleken()
        self.hand = []
        for i in range(num):
            rint = random.randint(0, self.lek.deck_size()-1)
            self.hand.append(self.lek.get_card_from_deck(rint))
    #destruktor
    def __del__(self):
        del self.hand
        del self.lek
    
    #Ny hand från lek
    def get_new_hand(self):
        #Räknar kort i handen. 5st
        num = len(self.hand)
        #Här skapar vi en räknare som räknar varje item i listan self.hand
        for i, item in enumerate(self.hand):
            #enumerate gör så vi kan skapa en räknare och ett som jag kallar det 'item' så vi vet värdet på iterationen
            self.lek.add_card(item)
        #Här tömmer vi handen.
        self.hand.clear()
        #Shufflar sedan leken
        self.lek.shuffle()
        #räknare som räknar till num
        for i in range(num):
            #Plockar en siffra mellan 0 och kortlekens storlek-1 detta för att i börjar på 0 och slutar på 51.
            rint = random.randint(0, self.lek.deck_size()-1)
            #lägger till handen från leken.
            self.hand.append(self.lek.get_card_from_deck(rint))
    
    #Visar handens storlek    
    def hand_size(self):
        return len(self.hand)

    #Visar alla kort i handen
    def view_hand(self):
        for s in self.hand:
            s.view()
        print("\n")
    #dict_val(feldöpt) ändrar kenkt,dam,kung,ess till värdet 11,12,13,14 för att enklare kunna räkna ut stege
    def dict_val(self):
        #Lista val
        val = []
        #Loopar varje element i hand
        for s in self.hand:
            #Lägger till elementets värde i val
            val.append(s.get_varde())
        #Här byter vi ut sträng mot digit.
        word = [w.replace('Knekt', '11').replace('Dam', '12').replace('Kung', '13').replace('Ess', '14') for w in val]
        #Onödigt gjort menmen
        val = word
        return val

    
    def got_pairs(self): #Kollar par
        pairs = 0 
        numbers = []
        par = {}
        for i in self.hand:
            numbers.append(i.get_varde())
        for s in numbers:
            if s not in par.keys(): 
                par[s] = 1
            else:
                par[s] += 1
        if list(par.values()).count(2) == 1:
            pairs = 1
        return pairs
    
    def got_set(self): #Kollar triss
        number = []
        sets = 0
        triss = {}
        for i in self.hand:
            number.append(i.get_varde())
        for s in number:
            if s not in triss.keys():
                triss[s] = 1
            else:
                triss[s] += 1
        
        """Här använder vi set för att ta bort multiplar av 1. Om vi har triss och par har vi ju kåk
        och då har vi en set på [3,2]. Nu vill vi bara kolla triss alltså set av [3,1,1] vilket blir [3,1]"""
        if set(list(triss.values())) == set([3,1]):
            sets = 1
        return sets

    def got_straight(self): #Kollar stege
        straights = 0 #sätter stege till 0
        straight = {} #gör en dict som sedan ska innehålla kortet och antalet
        val = self.dict_val() #hämtar en lista från funktionen dict_val() (felbenämnd!)
        for i in range (0, len(val)): #Kör igenom varje sträng i listan och omvandlar till int
            val[i] = int(val[i])
        val = sorted(val) #Detta för att kunna sortera listan från lägst till högst
        for i in val: 
            if i not in straight.keys(): #Kollar om elementet finns i nycklarna av dict ({keys:values})
                straight[i] = 1#Om det inte finns i nyckelen lägger vi till den som nyckel med värde 1
            else:
                #Om den finns vill vi lägga till 1. då har vi tex ({'Ess': 2})
                straight[i] += 1
        #Värde av lista för att se om högsta värdet - minsta i listan blir 4.
        val_lista = val[4] - val[0]
        #Här räknar vi hur många 1or som finns i straight. Om det finns 5 så finns ju inget par
        #Vi behöver även veta att högsta - minsta i listan blir 4. Eftersom det blir så i stegar. tex 2 3 4 5 6, 6-2 = 4
        if list(straight.values()).count(1) == 5 and val_lista == 4:
            straights = 1
        else:
            #Här tittar vi på hela listan val och om den är lika med 14,2,3,4,5 så har vi en stege.
            #Vi kollar alltså med Ess som lägst istället för högst.
            if set(val) == set([14,2,3,4,5]):
                straights = 1
            else:
                pass
        return straights

    def got_flush(self): #Kollar färg
        farger = []
        flush = 0
        farg = {}
        for i in self.hand:
            farger.append(i.get_farg())
        for s in farger:
            if s not in farg.keys():
                farg[s] = 1
            else:
                farg[s] += 1
        if list(farg.values()).count(5) == 1:
            flush = 1
            #self.view_hand()
        return flush
    
    def got_full_house(self): #Kollar kåk
        full_house = 0
        kok = {}
        kokar = [i.get_varde() for i in self.hand]
        for s in kokar:
            if s not in kok.keys():
                kok[s] = 1
            else:
                kok[s] += 1
        if sorted(kok.values()) == [2,3]:
            full_house = 1
            #self.view_hand()
        return full_house

    def got_four_of_a_kind(self): #Kollar fyrtal
        fyrtal = []
        fyrtalet = {}
        four_of_a_kind = 0
        for i in self.hand:
            fyrtal.append(i.get_varde())
        for s in fyrtal:
            if s not in fyrtalet.keys():
                fyrtalet[s] = 1
            else:
                fyrtalet[s] += 1
        if list(fyrtalet.values()).count(4) == 1:
            four_of_a_kind = 1
            #self.view_hand()
        return four_of_a_kind

    def got_straight_flush(self): #Kollar färgstege
        straight_flush = 0
        if self.got_flush() == 1 and self.got_straight() == 1:
            straight_flush = 1
            self.view_hand()
        return straight_flush
    
    def got_royal_flush(self):
        val = []
        royal = {}
        royal_flush = 0
        if self.got_straight() == 1 and self.got_flush() == 1:
            for i in self.hand:
                val.append(i.get_varde())
            if set(val) == set(['10','Knekt','Dam','Kung','Ess']):
                royal_flush = 1
                self.view_hand()
            else:
                pass
        return royal_flush