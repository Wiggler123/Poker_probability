from hand import hand
from alive_progress import alive_bar
import numpy as np

class sannolikhet:
    def __init__(self, sim=10):
        self.sim = sim
        self.hand = hand()
        self.list_triss = []
        self.list_fyrtal = []
        self.antal_sim = []
        self.list_par = []
        self.list_farg = []
        self.list_kok = []
        self.antal_sim = np.linspace(0,self.sim,num=self.sim)
    

    def __del__(self):
        del self.list_par
        del self.list_triss
        del self.list_farg
        del self.list_kok
        del self.list_fyrtal

    def __get_list_par__(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_par.append(self.hand.__got_pairs__())
                self.hand.__get_new_hand__()
                bar()
        return self.list_par

    def __get_list_triss__(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_triss.append(self.hand.__got_set__())
                self.hand.__get_new_hand__()
                bar()

        return self.list_triss
    
    def __get_list_farg__(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_farg.append(self.hand.__got_flush__())
                self.hand.__get_new_hand__()
                bar()
        return self.list_farg
    
    def __get_list_kok__(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_kok.append(self.hand.__got_full_house__())
                self.hand.__get_new_hand__()
                bar()
        return self.list_kok

    def __get_list_fyrtal__(self):
        with alive_bar(self.sim, bar='bubbles', spinner='waves2') as bar:
            for i in range(self.sim):
                self.list_fyrtal.append(self.hand.__got_four_of_a_kind__())
                self.hand.__get_new_hand__()
                bar()
        return self.list_fyrtal
    

    def __get_sum_par__(self):
        return(sum(self.__get_list_par__()))

    def __get_sum_triss__(self):
        return(sum(self.__get_list_triss__()))

    def __get_sum_farg__(self):
        return(sum(self.__get_list_farg__()))

    def __get_sum_kok__(self):
        return(sum(self.__get_list_kok__()))

    def __get_sum_fyrtal__(self):
        return(sum(self.__get_list_fyrtal__()))

    def __get_antal_sim__(self):
        return(self.antal_sim)
