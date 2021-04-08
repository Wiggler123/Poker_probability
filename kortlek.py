from kort import kort
import random
from random import shuffle

class kortleken:
    def __init__(self):
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

    def __list__(self):
        for s in self.lek:
            s.__view__()

    def __deck_size__(self):
        return len(self.lek)

    def __view_card_at_index__(self,num:int):
        if num > 0 or num < self.__deck_size__():
            return self.lek[num]
        else:
            print("Index out of range")
    
    def __get_card_at_index__(self,kort):
        for i, item in enumerate(self.lek):
            if item.farg == kort.farg and item.varde == str(kort.varde):
                return i
    
    def __remove_card__(self,kort):
        del self.lek[self.__get_card_at_index__(kort)]
        
    def __add_card__(self,kort):
        self.lek.append(kort)
    
    def __shuffle__(self):
        shuffle(self.lek)

    def __get_card_from_deck__(self,num:int):
        a = kort(self.lek[num].get_farg(), self.lek[num].get_varde())
        del self.lek[num]
        return a
    

    