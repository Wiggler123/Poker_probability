from kortlek import kortleken
import random
from random import shuffle


#Väljer ut 5 kort från kortleken
class hand:
    def __init__(self, num=5):
        self.lek = kortleken()
        self.hand = []
        for i in range(num):
            rint = random.randint(0, self.lek.__deck_size__()-1)
            self.hand.append(self.lek.__get_card_from_deck__(rint))
    
    def __del__(self):
        del self.hand
        del self.lek

    def __get_new_hand__(self):
        num = len(self.hand)
        for i, item in enumerate(self.hand):
            self.lek.__add_card__(item)
        self.hand.clear()
        self.lek.__shuffle__()
        for i in range(num):
            rint = random.randint(0, self.lek.__deck_size__()-1)
            self.hand.append(self.lek.__get_card_from_deck__(rint))
        
    def __hand_size__(self):
        return len(self.hand)

    def __view_hand__(self):
        for s in self.hand:
            s.view()
        print("\n")

    def __got_pairs__(self):
        pairs = 0
        numbers = []
        for i in self.hand:
            numbers.append(i.get_varde())
        for s in numbers:
            count = numbers.count(s)
            if count == 2:
                pairs = 1
                break
        return pairs
    
    def __got_set__(self):
        number = []
        sets = 0
        for i in self.hand:
            number.append(i.get_varde())
        for j in number:
            count = number.count(j)
            if count == 3:
                sets = 1
        return sets

    def __got_flush__(self):
        farger = []
        flush = 0
        for i in self.hand:
            farger.append(i.get_farg())
        for s in farger:
            count = farger.count(s)
            if count == 5:
                flush = 1
        return flush
    
    def __got_full_house__(self):
        full_house = 0
        if self.__got_pairs__() == 1 and self.__got_set__() == 1:
            full_house = 1
        return full_house

    def __got_four_of_a_kind__(self):
        fyrtal = []
        four_of_a_kind = 0
        for i in self.hand:
            fyrtal.append(i.get_varde())
        for s in fyrtal:
            count = fyrtal.count(s)
            if count == 4:
                four_of_a_kind = 1
        return four_of_a_kind
                