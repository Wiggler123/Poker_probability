from kort import kort
import random
from random import shuffle

class kortleken:
    def __init__(self): #Skapar kortleken
        self.lek = []
        farg = ['Hjärter','Ruter','Klöver','Spader']
        hoga_kort = ['Knekt', 'Dam', 'Kung', 'Ess']
        for i in range(len(farg)):
            for s in range(2,11):
                self.lek.append(kort(farg[i], str(s)))
            for k in hoga_kort:
                self.lek.append(kort(farg[i], k))

    def __del__(self):
        del self.lek

    def list(self): #Listar hela kortleken
        for s in self.lek:
            s.view()

    def deck_size(self): #Returnerar längden av listan self.lek(Hur många kort i leken.)
        return len(self.lek)

    def view_card_at_index(self,num:int): #Visar kort på ett visst index
        if num > 0 or num < self.deck_size():
            return self.lek[num]
        else:
            print("Index out of range")
    
    def get_card_at_index(self,kort): #Här kan vi få tag på ett index där ett visst kort finns tex get_card_at_index('Hjärter',6)
        for i, item in enumerate(self.lek):
            if item.farg == kort.farg and item.varde == str(kort.varde):
                return i
    
    def remove_card(self,kort): #Ta bort ett kort
        del self.lek[self.get_card_at_index(kort)]
        
    def add_card(self,kort): #lägg till ett kort
        self.lek.append(kort)
    
    def shuffle(self): #blandar leken
        shuffle(self.lek)

    def get_card_from_deck(self,num:int): #Få ett kort från index
        a = kort(self.lek[num].get_farg(), self.lek[num].get_varde())
        del self.lek[num]
        return a