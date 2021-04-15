from hand import hand
from alive_progress import alive_bar
import numpy as np

class sannolikhet:
    def __init__(self, sim=1000000):
        self.sim = sim
        self.hand = hand()
        self.list_triss = []
        self.list_fyrtal = []

        self.list_par = []
        self.list_farg = []
        self.list_kok = []
        self.list_two_pair = []
        self.list_stege = []
        self.list_fargstege = []
        self.list_royal_flush = []
        self.antal_sim = np.linspace(0,self.sim,num=self.sim)
    

    def __del__(self):
        del self.list_par
        del self.list_triss
        del self.list_farg
        del self.list_kok
        del self.list_fyrtal
        del self.list_stege
        del self.list_fargstege
        del self.list_royal_flush

    def get_list_par(self): #Skapar en lista med alla par. Med en progressbar.
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_par.append(self.hand.got_pairs())
                self.hand.get_new_hand()
                bar()
        return self.list_par

    def get_list_triss(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_triss.append(self.hand.got_set())
                self.hand.get_new_hand()
                bar()

        return self.list_triss

    def get_list_stege(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_stege.append(self.hand.got_straight())
                self.hand.get_new_hand()
                bar()
        return self.list_stege
    
    def get_list_farg(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_farg.append(self.hand.got_flush())
                self.hand.get_new_hand()
                bar()
        return self.list_farg
    
    def get_list_kok(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_kok.append(self.hand.got_full_house())
                self.hand.get_new_hand()
                bar()
        return self.list_kok

    def get_list_fyrtal(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_fyrtal.append(self.hand.got_four_of_a_kind())
                self.hand.get_new_hand()
                bar()
        return self.list_fyrtal

    def get_list_fargstege(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_fargstege.append(self.hand.got_straight_flush())
                self.hand.get_new_hand()
                bar()
        return self.list_fargstege
    
    def get_list_royal_flush(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_royal_flush.append(self.hand.got_royal_flush())
                self.hand.get_new_hand()
                bar()
        return self.list_royal_flush

    
    def get_sum_par(self): #Summa av listan.
        return(sum(self.get_list_par))

    def get_sum_triss(self):
        return(sum(self.get_list_triss))

    def get_sum_farg(self):
        return(sum(self.get_list_farg))

    def get_sum_kok(self):
        return(sum(self.get_list_kok))

    def get_sum_fyrtal(self):
        return(sum(self.get_list_fyrtal))

    def get_sum_stege(self):
        return(sum(self.list_stege))
    
    def get_sum_fargstege(self):
        return(sum(self.list_fargstege()))

    def get_sum_royal_flush(self):
        return(sum(self.list_royal_flush))

    def get_antal_sim(self):
        return(self.antal_sim)