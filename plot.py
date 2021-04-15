from sannolikheter import sannolikhet
import matplotlib.pyplot as plt


class plot:
    def __init__(self, sim=10):
        self.chans = sannolikhet(sim)
        self.matte_par = 1098240/2598960*100
        self.matte_triss = 54912/2598960*100
        self.matte_farg = 5108/2598960*100
        self.matte_kok = 3744/2598960*100
        self.matte_stege = 10200/2598960*100
        self.matte_fyrtal = 624/2598960*100
        self.matte_fargstege = 36/2598960*100
        self.matte_royal_flush = 4/2598960*100
        self.antal_sim = self.chans.get_antal_sim()
        self.sannolikhet_par = []
        self.sannolikhet_triss = []
        self.sannolikhet_farg = []
        self.sannolikhet_kok = []
        self.sannolikhet_fyrtal = []
        self.sannolikhet_stege = []
        self.sannolikhet_fargstege = []
        self.sannolikhet_royal_flush = []

    def __del__(self):
        del self.chans
        del self.matte_par
        del self.matte_triss
        del self.matte_farg
        del self.matte_kok
        del self.matte_fyrtal
        del self.antal_sim
        del self.sannolikhet_par
        del self.sannolikhet_triss
        del self.sannolikhet_farg
        del self.sannolikhet_kok
        del self.sannolikhet_fyrtal
        del self.sannolikhet_stege
        del self.sannolikhet_fargstege
        del self.sannolikhet_royal_flush

    def plot_par(self): #Gör en massa saker utifrån de vi skapat.
        temp_sum_par = 0
        felaktighet = []
        self.sum_par = self.chans.get_list_par()
        print(len(self.sum_par))
        for i in range(len(self.antal_sim)):
            temp_sum_par += self.sum_par[i]
            self.sannolikhet_par.append(100*temp_sum_par/(i+1))
            felaktighet.append((self.sannolikhet_par[i] - (self.matte_par)) / self.matte_par*100)
        print("Sannolikheten för par på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_par[len(self.antal_sim)-1]) + "%\n")
        print("Program felaktighet var: " + str(felaktighet[len(felaktighet)-1]) + '%\n')
        if temp_sum_par == 1:
            print("Du fick 1 par på {} händer".format(len(self.antal_sim)))
        elif temp_sum_par > 1:
            print("Du fick {} par på {} händer".format(temp_sum_par,len(self.antal_sim)))
        else:
            print("Du fick inget par!")
        ask_par = input("Vill du plotta en graf till sannolikheten? (j/n) ").lower()
        if ask_par == 'j':
            plot1 = plt.figure(1,figsize=(7,5),dpi=80)
            plt_par = plt.subplot()
            plt_par.plot(self.antal_sim, self.sannolikhet_par, '-b', label='Program sannolikhet')
            plt_par.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet par')
            plt_par.axhline(self.matte_par, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_par.legend()
            plot2 = plt.figure(2,figsize=(7,5),dpi=80)
            plt_par = plt.subplot()
            plt_par.plot(self.antal_sim,felaktighet, '-b', label='Program felaktighet')
            plt_par.set(xlabel='Antal simuleringar', ylabel='Felaktighet i %', title='Program felaktighet')
            plt_par.axhline(y=0, color='black')
            plt_par.legend()
            plt.show()
        return

    def plot_triss(self):
        temp_sum_triss = 0
        felaktighet = []
        self.sum_triss = self.chans.get_list_triss()
        for i in range(len(self.antal_sim)):
            temp_sum_triss += self.sum_triss[i]
            self.sannolikhet_triss.append(100*temp_sum_triss/(i+1))
            felaktighet.append((self.sannolikhet_triss[i] - (self.matte_triss)) / self.matte_triss*100)
        print("Sannolikheten för triss på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_triss[len(self.antal_sim)-1]) + "%\n")
        print("Program felaktighet var: " + str(felaktighet[len(felaktighet)-1]) + '%\n')
        if temp_sum_triss == 1:
            print("Du fick 1 triss på {} händer".format(len(self.antal_sim)))
        elif temp_sum_triss > 1:
            print("Du fick {} trissar på {} händer".format(temp_sum_triss,len(self.antal_sim)))
        else:
            print("Du fick ingen triss!")
        ask_triss = input("Vill du plotta en graf till sannolikheten? (j/n) ").lower()
        if ask_triss == 'j':
            plot1 = plt.figure(1)
            plt_triss = plt.subplot()
            plt_triss.plot(self.antal_sim, self.sannolikhet_triss, '-b', label='Program sannolikhet')
            plt_triss.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet triss')
            plt_triss.axhline(self.matte_triss, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_triss.legend()
            plot2 = plt.figure(2)
            plt_triss = plt.subplot()
            plt_triss.plot(self.antal_sim,felaktighet, '-b', label='Program felaktighet')
            plt_triss.set(xlabel='Antal simuleringar', ylabel='Felaktighet i %', title='Program felaktighet')
            plt_triss.axhline(y=0, color='black')
            plt_triss.legend()
            plt.show()
        return

    def plot_stege(self):
        temp_sum_stege = 0
        felaktighet = []
        self.sum_stege = self.chans.get_list_stege()
        for i in range(len(self.antal_sim)):
            temp_sum_stege += self.sum_stege[i]
            self.sannolikhet_stege.append(100*temp_sum_stege/(i+1))
            felaktighet.append((self.sannolikhet_stege[i] - (self.matte_stege)) / self.matte_stege*100)
        print("Sannolikheten för stege på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_stege[len(self.antal_sim)-1]) + "%\n")
        print("Program felaktighet var: " + str(felaktighet[len(felaktighet)-1]) + '%\n')
        if temp_sum_stege == 1:
            print("Du fick 1 stege på {} händer".format(len(self.antal_sim)))
        elif temp_sum_stege > 1:
            print("Du fick {} stegar på {} händer".format(temp_sum_stege,len(self.antal_sim)))
        else:
            print("Du fick ingen stege")
        ask_stege = input("Vill du plotta en graf till sannolikheten? (j/n) ").lower()
        if ask_stege == 'j':
            plot1 = plt.figure(1)
            plt_stege = plt.subplot()
            plt_stege.plot(self.antal_sim, self.sannolikhet_stege, '-b', label='Program sannolikhet')
            plt_stege.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet stege')
            plt_stege.axhline(self.matte_stege, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_stege.legend()
            plot2 = plt.figure(2)
            plt_stege = plt.subplot()
            plt_stege.plot(self.antal_sim,felaktighet, '-b', label='Program felaktighet')
            plt_stege.set(xlabel='Antal simuleringar', ylabel='Felaktighet i %', title='Program felaktighet')
            plt_stege.axhline(y=0, color='black')
            plt_stege.legend()
            plt.show()
    
    def plot_farg(self):
        temp_sum_farg = 0
        felaktighet = []
        self.sum_farg = self.chans.get_list_farg()
        for i in range(len(self.antal_sim)):
            temp_sum_farg += self.sum_farg[i]
            self.sannolikhet_farg.append(100*temp_sum_farg/(i+1))
            felaktighet.append((self.sannolikhet_farg[i] - self.matte_farg)/self.matte_farg*100)
        print("Sannolikheten för färg på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_farg[len(self.antal_sim)-1]) + "%\n")
        print("Program felaktighet var: " + str(felaktighet[len(felaktighet)-1]) + '%\n')
        if temp_sum_farg == 1:
            print("Du fick 1 färg på {} händer".format(len(self.antal_sim)))
        elif temp_sum_farg > 1:
            print("Du fick {} färgar på {} händer".format(temp_sum_farg,len(self.antal_sim)))
        else:
            print("Du fick ingen färg")
        ask_farg = input("Vill du plotta en graf till sannolikheten? (j/n) ").lower()
        if ask_farg == 'j':
            plot1 = plt.figure(1)
            plt_farg = plt.subplot()
            plt_farg.plot(self.antal_sim, self.sannolikhet_farg, '-b', label='Program sannolikhet')
            plt_farg.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet färg')
            plt_farg.axhline(self.matte_farg, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_farg.legend()
            plot2 = plt.figure(2)
            plt_farg = plt.subplot()
            plt_farg.plot(self.antal_sim,felaktighet, '-b', label='Program felaktighet')
            plt_farg.set(xlabel='Antal simuleringar', ylabel='Felaktighet i %', title='Program felaktighet')
            plt_farg.axhline(y=0, color='black')
            plt_farg.legend()
            plt.show()
        return

    def plot_kok(self):
        self.sum_kok = self.chans.get_list_kok()
        temp_sum_kok = 0
        felaktighet = []
        for i in range(len(self.antal_sim)):
            temp_sum_kok += self.sum_kok[i]
            self.sannolikhet_kok.append(100*temp_sum_kok/(i+1))
            felaktighet.append((self.sannolikhet_kok[i] - self.matte_kok)/self.matte_kok*100)
        print("Sannolikheten för kåk på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_kok[len(self.antal_sim)-1]) + "%\n")
        print("Program felaktighet var: " + str(felaktighet[len(felaktighet)-1]) + '%\n')
        if temp_sum_kok == 1:
            print("Du fick 1 kåk på {} händer ".format(len(self.antal_sim)))
        elif temp_sum_kok > 1:
            print("Du fick {} kåkar på {} händer".format(temp_sum_kok,len(self.antal_sim)))
        else:
            print("Du fick inga kåkar!")
        ask_kok = input("Vill du plotta en graf till sannolikheten? (j/n) ").lower()
        if ask_kok == 'j':
            plot1 = plt.figure(1)
            plt_kok = plt.subplot()
            plt_kok.plot(self.antal_sim, self.sannolikhet_kok, '-b',label='Program sannolikhet')
            plt_kok.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet kåk')
            plt_kok.axhline(self.matte_kok, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_kok.legend()
            plot2 = plt.figure(2)
            plt_kok = plt.subplot()
            plt_kok.plot(self.antal_sim,felaktighet, '-b', label='Program felaktighet')
            plt_kok.set(xlabel='Antal simuleringar', ylabel='Felaktighet i %', title='Program felaktighet')
            plt_kok.axhline(y=0, color='black')
            plt_kok.legend()
            plt.show()
        return

    def plot_fyrtal(self):
        temp_sum_fyrtal = 0
        felaktighet = []
        self.sum_fyrtal = self.chans.get_list_fyrtal()
        for i in range(len(self.antal_sim)):
            temp_sum_fyrtal += self.sum_fyrtal[i]
            self.sannolikhet_fyrtal.append(100*temp_sum_fyrtal/(i+1))
            felaktighet.append((self.sannolikhet_fyrtal[i] - self.matte_fyrtal)/self.matte_fyrtal*100)
        print("Sannolikheten för fyrtal på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_fyrtal[len(self.antal_sim)-1]) + "%\n")
        print("Program felaktighet var: " + str(felaktighet[len(felaktighet)-1]) + '%\n')
        if temp_sum_fyrtal == 1:
            print("Du fick 1 fyrtal på {} händer".format(len(self.antal_sim)))
        elif temp_sum_fyrtal > 1:
            print("Du fick {} fyrtal på {} händer".format(temp_sum_fyrtal,len(self.antal_sim)))
        else:
            print("Du fick inga fyrtal")
        ask_fyrtal = input("Vill du plotta en graf till sannolikheten? (j/n) ").lower() 
        if ask_fyrtal == 'j':
            plot1 = plt.figure(1)
            plt_fyrtal = plt.subplot()
            plt_fyrtal.plot(self.antal_sim, self.sannolikhet_fyrtal, '-b', label='Program sannolikhet')
            plt_fyrtal.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet fyrtal')
            plt_fyrtal.axhline(self.matte_fyrtal, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_fyrtal.legend()
            plot2 = plt.figure(2)
            plt_fyrtal = plt.subplot()
            plt_fyrtal.plot(self.antal_sim,felaktighet, '-b', label='Program felaktighet')
            plt_fyrtal.set(xlabel='Antal simuleringar', ylabel='Felaktighet i %', title='Program felaktighet')
            plt_fyrtal.axhline(y=0, color='black')
            plt_fyrtal.legend()
            plt.show()
        return

    def plot_fargstege(self):
        temp_sum_fargstege = 0
        felaktighet = []
        self.sum_fargstege = self.chans.get_list_fargstege()
        for i in range(len(self.antal_sim)):
            temp_sum_fargstege += self.sum_fargstege[i]
            self.sannolikhet_fargstege.append(100*temp_sum_fargstege/(i+1))
            felaktighet.append((self.sannolikhet_fargstege[i] - self.matte_fargstege)/self.matte_fargstege*100)
        print("Sannolikheten för färgstege på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_fargstege[len(self.antal_sim)-1]) + "%\n")
        print("Program felaktighet var: " + str(felaktighet[len(felaktighet)-1]) + '%\n')
        if temp_sum_fargstege == 1:
            print("Du fick 1 färgstege på {} händer".format(len(self.antal_sim)))
        elif temp_sum_fargstege > 1:
            print("Du fick {} färgstegar på {} händer".format(temp_sum_fargstege,len(self.antal_sim)))
        else:
            print("Du fick inga färgstegar")
        ask_fargstege = input("Vill du plotta en graf till sannolikheten? (j/n) ").lower() 
        if ask_fargstege == 'j':
            plot1 = plt.figure(1)
            plt_fargstege = plt.subplot()
            plt_fargstege.plot(self.antal_sim, self.sannolikhet_fargstege, '-b', label='Program sannolikhet')
            plt_fargstege.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet färgstege')
            plt_fargstege.axhline(self.matte_fargstege, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_fargstege.legend()
            plot2 = plt.figure(2)
            plt_fargstege = plt.subplot()
            plt_fargstege.plot(self.antal_sim,felaktighet, '-b', label='Program felaktighet')
            plt_fargstege.set(xlabel='Antal simuleringar', ylabel='Felaktighet i %', title='Program felaktighet')
            plt_fargstege.axhline(y=0, color='black')
            plt_fargstege.legend()
            plt.show()
        return

    def plot_royal_flush(self):
        temp_sum_royal = 0
        felaktighet = []
        self.sum_royal_flush = self.chans.get_list_royal_flush()
        for i in range(len(self.antal_sim)):
            temp_sum_royal += self.sum_royal_flush[i]
            self.sannolikhet_royal_flush.append(100*temp_sum_royal/(i+1))
            felaktighet.append((self.sannolikhet_royal_flush[i] - self.matte_royal_flush)/self.matte_royal_flush*100)
        print("Sannolikheten för Royal flush på första handen under {} spel är: ".format(len(self.antal_sim)) + str(self.sannolikhet_royal_flush[len(self.antal_sim)-1]) + "%\n")
        print("Program felaktighet var: " + str(felaktighet[len(felaktighet)-1]) + '%\n')
        if temp_sum_royal == 1:
            print("Du fick 1 Royal flush på {} händer".format(len(self.antal_sim)))
        elif temp_sum_royal > 1:
            print("Du fick {} Royal flush på {} händer".format(temp_sum_royal,len(self.antal_sim)))
        else:
            print("Du fick inga Royal flush")
        ask_royal = input("Vill du plotta en graf till sannolikheten? (j/n) ").lower() 
        if ask_royal == 'j':
            plot1 = plt.figure(1)
            plt_royalflush = plt.subplot()
            plt_royalflush.plot(self.antal_sim, self.sannolikhet_royal_flush, '-b', label='Program sannolikhet')
            plt_royalflush.set(xlabel='Antal simuleringar', ylabel='Sannolikhet i %', title='Sannolikhet royal flush')
            plt_royalflush.axhline(self.matte_royal_flush, color='r', label='Matematisk sannolikhet',linestyle='dashed')
            plt_royalflush.legend()
            plot2 = plt.figure(2)
            plt_royalflush = plt.subplot()
            plt_royalflush.plot(self.antal_sim,felaktighet, '-b', label='Program felaktighet')
            plt_royalflush.set(xlabel='Antal simuleringar', ylabel='Felaktighet i %', title='Program felaktighet')
            plt_royalflush.axhline(y=0, color='black')
            plt_royalflush.legend()
            plt.show()
        return