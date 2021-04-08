from sannolikheter import sannolikhet
import matplotlib.pyplot as plt


class plot:
    def __init__(self, sim=10):
        self.chans = sannolikhet(sim)
        self.matte_par = 1098240/2598960*100
        self.matte_triss = 54912/2598960*100
        self.matte_farg = 5108/2598960*100
        self.matte_kok = 3744/2598960*100
        self.matte_fyrtal = 624/2598960*100
        self.antal_sim = self.chans.__get_antal_sim__()
        self.sannolikhet_par = []
        self.sannolikhet_triss = []
        self.sannolikhet_farg = []
        self.sannolikhet_kok = []
        self.sannolikhet_fyrtal = []

    def __plot_par__(self):
        temp_sum_par = 0
        self.sum_par = self.chans.__get_list_par__()
        for i in range(len(self.antal_sim)):
            temp_sum_par += self.sum_par[i]
            self.sannolikhet_par.append(100*temp_sum_par/(i+1))
        print("Sannolikheten för par på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_par[len(self.antal_sim)-1]) + "%")
        if temp_sum_par == 1:
            print("Du fick 1 par på {} händer".format(len(self.antal_sim)))
        elif temp_sum_par > 1:
            print("Du fick {} par på {} händer".format(temp_sum_par,len(self.antal_sim)))
        else:
            print("Du fick inget par!")
        ask_par = input("Vill du plotta en graf till sannolikheten? (j/n) ")
        if ask_par == 'j':
            plt_par = plt.subplot()
            plt_par.plot(self.antal_sim, self.sannolikhet_par, '-b', label='Program sannolikhet')
            plt_par.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet par')
            plt_par.axhline(self.matte_par, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_par.legend()
            plt.show()
        return

    def __plot_triss__(self):
        temp_sum_triss = 0
        self.sum_triss = self.chans.__get_list_triss__()
        for i in range(len(self.antal_sim)):
            temp_sum_triss += self.sum_triss[i]
            self.sannolikhet_triss.append(100*temp_sum_triss/(i+1))
        print("Sannolikheten för triss på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_triss[len(self.antal_sim)-1]) + "%")
        if temp_sum_triss == 1:
            print("Du fick 1 triss på {} händer".format(len(self.antal_sim)))
        elif temp_sum_triss > 1:
            print("Du fick {} trissar på {} händer".format(temp_sum_triss,len(self.antal_sim)))
        else:
            print("Du fick ingen triss!")
        ask_triss = input("Vill du plotta en graf till sannolikheten? (j/n) ")
        if ask_triss == 'j':
            plt_triss = plt.subplot()
            plt_triss.plot(self.antal_sim, self.sannolikhet_triss, '-b', label='Program sannolikhet')
            plt_triss.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet triss')
            plt_triss.axhline(self.matte_triss, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_triss.legend()
            plt.show()
        return

    def __plot_farg__(self):
        temp_sum_farg = 0
        self.sum_farg = self.chans.__get_list_farg__()
        for i in range(len(self.antal_sim)):
            temp_sum_farg += self.sum_farg[i]
            self.sannolikhet_farg.append(100*temp_sum_farg/(i+1))
        print("Sannolikheten för färg på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_farg[len(self.antal_sim)-1]) + "%")
        if temp_sum_farg == 1:
            print("Du fick 1 färg på {} händer".format(len(self.antal_sim)))
        elif temp_sum_farg > 1:
            print("Du fick {} färgar på {} händer".format(temp_sum_farg,len(self.antal_sim)))
        else:
            print("Du fick ingen färg")
        ask_farg = input("Vill du plotta en graf till sannolikheten? (j/n) ")
        if ask_farg == 'j':
            plt_farg = plt.subplot()
            plt_farg.plot(self.antal_sim, self.sannolikhet_farg, '-b', label='Program sannolikhet')
            plt_farg.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet färg')
            plt_farg.axhline(self.matte_farg, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_farg.legend()
            plt.show()
        return

    def __plot_kok__(self):
        self.sum_kok = self.chans.__get_list_kok__()
        temp_sum_kok = 0
        for i in range(len(self.antal_sim)):
            temp_sum_kok += self.sum_kok[i]
            self.sannolikhet_kok.append(100*temp_sum_kok/(i+1))
        print("Sannolikheten för kåk på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_kok[len(self.antal_sim)-1]) + "%")
        if temp_sum_kok == 1:
            print("Du fick 1 kåk på {} händer ".format(len(self.antal_sim)))
        elif temp_sum_kok > 1:
            print("Du fick {} kåkar på {} händer".format(temp_sum_kok,len(self.antal_sim)))
        else:
            print("Du fick inga kåkar!")
        ask_kok = input("Vill du plotta en graf till sannolikheten? (j/n) ")
        if ask_kok == 'j':
            plt_kok = plt.subplot()
            plt_kok.plot(self.antal_sim, self.sannolikhet_kok, '-b',label='Program sannolikhet')
            plt_kok.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet kåk')
            plt_kok.axhline(self.matte_farg, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_kok.legend()
            plt.show()
        return

    def __plot_fyrtal__(self):
        temp_sum_fyrtal = 0
        self.sum_fyrtal = self.chans.__get_list_fyrtal__()
        for i in range(len(self.antal_sim)):
            temp_sum_fyrtal += self.sum_fyrtal[i]
            self.sannolikhet_fyrtal.append(100*temp_sum_fyrtal/(i+1))
        print("Sannolikheten för fyrtal på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_fyrtal[len(self.antal_sim)-1]) + "%")
        if temp_sum_fyrtal == 1:
            print("Du fick 1 fyrtal på {} händer".format(len(self.antal_sim)))
        elif temp_sum_fyrtal > 1:
            print("Du fick {} fyrtal på {} händer".format(temp_sum_fyrtal,len(self.antal_sim)))
        else:
            print("Du fick inga fyrtal")
        ask_fyrtal = input("Vill du plotta en graf till sannolikheten? (j/n) ") 
        if ask_fyrtal == 'j':
            plt_fyrtal = plt.subplot()
            plt_fyrtal.plot(self.antal_sim, self.sannolikhet_fyrtal, '-b', label='Program sannolikhet')
            plt_fyrtal.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet fyrtal')
            plt_fyrtal.axhline(self.matte_fyrtal, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_fyrtal.legend()
            plt.show()
        return