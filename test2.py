#Importera nödvändiga bibliotek 
import random
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt;plt.rcdefaults()
from alive_progress import alive_bar
from timeit import default_timer as timer
import logging
import threading
import time

#Skapar klass kort
class kort:
    def __init__(self,color,value):
        self.color = color
        self.value = value

    
    def View(self):
        return print(self.color + ' ' + self.value)
    
    def GetColor(self):
        return self.color
    
    def GetValue(self):
        return self.value

#Klass kort tar emot två parametrar, färg och värde. Vi kan få tag på färg,värde samt visa kortet. 


#Skapar klass lek
class lek:
    def __init__(self):
        self.leken = []
        self.hoga = ['Knekt','Dam','Kung','Ess']
        self.farg = ['Hjärter','Spader','Ruter','Klöver']
        for i in range(len(self.farg)):
            for s in range(2,11):
                self.leken.append(kort(self.farg[i], str(s)))
            for v in self.hoga:
                self.leken.append(kort(self.farg[i],v))
    
    def View_lek(self):
        [i.View() for i in self.leken]

    def GetCardFromDeck(self, num:int):
        a = kort(self.leken[num].GetColor(), self.leken[num].GetValue())
        del self.leken[num]
        return a
#I lek skapar vi själva leken som består av 52st kort från klass kort. Sedan kan vi använda oss 
# av kort egenskaperna för att visa hela leken. Vi kan även ta ett kort från leken.

#Skapar klass hand
class hand:
    start = timer()
    def __init__(self):
        self.lek = lek()
        self.hand = []
        num = 5
        for i in range(num):
            rint = random.randint(0, len(self.lek.leken)-1)
            self.hand.append(self.lek.GetCardFromDeck(rint))

#Här skapar vi en hand med 5 kort. Där vi slumpar ett tal från 0-52, eftersom listor går från 0-51 måste vi ta -1

    def ViewHand(self):
        [i.View() for i in self.hand]

    #Här visar vi alla kort på handen, vi använder View() från kort klassen.

    def GotPar(self):
        par = 0
        pars = [i.GetValue() for i in self.hand]
        if len(set(pars)) == 4:
            par = 1
        return par

    #Här börjar vi med att sätta par till 0(inget par) och en lista pars.
    #Sedan loopar vi igenom handen och lägger till värdet på kortet till pars.
    #Sen kollar vi helt enkelt om längden på set() av listan är 4. Set tar sammar värde och slår ihop
    # Tex print(set([2,2,1,4,5])) då kommer {1,2,4,5} att visas

    def GotSet(self):
        triss = 0
        sets = [i.GetValue() for i in self.hand]
        d = {}
        for i in sets:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        if set(list(d.values())) == set([3,1]):
            triss = 1
        return triss
    
     #Här börjar vi med att sätta par till 0(inget par),en lista (pars) och en dictionary.
    #Sedan loopar vi igenom handen och lägger till värdet på kortet till pars.
    #Sedan loopar vi igenom listan par och kollar om värdet är med i dict.keys() Är det inte det lägger vi till det
    #Finns värdet redan i dict adderar vi 1 till värdet.i
    #Sen omvandlar vi värdena på dictionaryn till en lista och räknar antalet 2 som finns. Om det finns exakt 1 har vi par
    

    def GotKok(self):
        full_house = 0
        kok = {}
        kokar = [i.GetValue() for i in self.hand]
        for s in kokar:
            if s not in kok.keys():
                kok[s] = 1
            else:
                kok[s] += 1
        if sorted(kok.values()) == [2,3]:
            full_house = 1
            #self.view_hand()
        return full_house
    
    #Här gör vi ungefär samma  som för triss, Men vi vet att räknaren måste vara 2,3 för kåk.
    #Så vi kan sortera värdena och kolla om de är lika med [2,3]

    def DictVal(self):
        #Lista val med värden från handen
        val = [i.GetValue() for i in self.hand]
        #Loopar varje element i hand
        #Här byter vi ut sträng mot digit.
        word = [w.replace('Knekt', '11').replace('Dam', '12').replace('Kung', '13').replace('Ess', '14') for w in val]
        #Onödigt gjort menmen
        val = word
        return val

    #Inför Stege skapar jag en lista med de riktiga värderna. Byter alltså ut ordet mot värdet.
    
    def GotStraight(self): #Kollar stege
        straights = 0 #sätter stege till 0
        straight = {} #gör en dict som sedan ska innehålla kortet och antalet
        val = self.DictVal() #hämtar en lista från funktionen dict_val() (felbenämnd!)
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
    
    def GotFarg(self):
        farger = [i.GetColor() for i in self.hand]
        flush = 0
        farg = {}
        for s in farger:
            if s not in farg.keys():
                farg[s] = 1
            else:
                farg[s] += 1
        if len(set(farg.values())) == 1:
            if self.GotStraight() != 1:
                flush = 1
            #self.view_hand()
        return flush
    #Samma princip som triss fast med färg istället. Vi behöver även se till så att vi inte har stege samtidigt
    #För då är det ju en färgstege och inte en färg

#Här kör vi Själva programmet
def main():
    n = int(input("Hur många simuleringar vill du göra: "))
    sumpar = 0
    sumtriss = 0
    sumkok = 0
    sumfarg = 0
    ant_sim = []
    san_par = []
    san_triss = []
    san_kok = []
    san_farg = []
    with alive_bar(n, bar='bubbles', spinner='waves2') as bar:
        for i in range(n):
            s = hand()
            ant_sim.append(i)
            sumpar += s.GotPar()
            sumtriss += s.GotSet()
            sumkok += s.GotKok()
            sumfarg += s.GotFarg()
            san_par.append(100*sumpar/(i+1))
            san_triss.append(100*sumtriss/(i+1))
            san_kok.append(100*sumkok/(i+1))
            san_farg.append(100*sumfarg/(i+1))
            bar()
    #Här skapar vi listor och intar som ska summera och lägga till i listan
    #Har även importerat en progressbar som visar hur lång tid det ska ta.

    p = input("Vilken typ av graf vill du plotta(cirkel(1)/stapel(2): ").lower()
    if p == '1' or p == 'cirkel':
        annat = 100 - san_par[-1] - san_triss[-1] - san_farg[-1] - san_kok[-1]
        labels = ['Annat','Par','Triss','Färg','Kåk']
        sizes = [annat,san_par[-1],san_triss[-1],san_farg[-1],san_kok[-1]]
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#66ffff']
        fig1, ax1 = plt.subplots(figsize=(5,5))
        porcent = sizes
        patches, texts = plt.pie(sizes, colors=colors, startangle=90, radius=1.2)
        labeld = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, porcent)]
        sort_legend = True
        if sort_legend:
               patches,labeld, dummy = zip(*sorted(zip(patches,labeld,sizes),key=lambda x:x[2],reverse=True))

        plt.legend(patches,labeld,loc='best', bbox_to_anchor=(-0.1,1.),fontsize=8)
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        ax1.axis('equal')  
        plt.tight_layout()
        plt.show()

        #Vet knappt vad detta gör! Men ville ha en snygg graf så grävde lite och hittade en fin!
        #Förstår delvis vad sakerna gör men långt ifrån allt!

    elif p =='2' or p == 'stapel':
        objects = 'Annat','Par','Triss','Färg','Kåk'
        annat = 100 - san_par[-1] - san_triss[-1] - san_farg[-1] - san_kok[-1]
        performance = annat,san_par[-1],san_triss[-1],san_farg[-1],san_kok[-1]
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#66ffff']
        font_title = mpl.font_manager.FontProperties(fname='C:/Users/danne/Downloads/Opensans/Opensans-Semibold.ttf')
        font_axis = mpl.font_manager.FontProperties(fname='C:/Users/danne/Downloads/Opensans/Opensans-Regular.ttf')
        y_pos = np.arange(len(objects))
        fig,ax = plt.subplots()
        bars = plt.bar(y_pos, performance, align='center', alpha=0.7,color=colors)

        #Tar bort onödiga linjer
        ax.spines['right'].set_visible(False)
        #ax.spines['left'].set_visible(False)
        #ax.spines['bottom'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color='#EEEEEE')
        ax.xaxis.grid(False)
        ax.set_ylabel('Sannolikhet i procent', labelpad=15, color='#333333',fontproperties=font_axis)
        ax.set_title('Poker - Sannolikhet och kombinationer ',fontproperties=font_title,pad=15,color='#333333')
        plt.xticks(y_pos, objects)
        for bar in bars.patches:
            txt = np.round(bar.get_height(), decimals=2)
            anot = txt.astype('str')
            plt.annotate(anot+'%', 
                        (bar.get_x() + bar.get_width() / 2, 
                        bar.get_height()), ha='center', va='center', xytext=(0, 10),
                        textcoords='offset points',fontsize = 10)
        plt.show()

        #Vet knappt vad detta gör! Men ville ha en snygg graf så grävde lite och hittade en fin
        #Förstår delvis vad sakerna gör men långt ifrån allt!


kora_igen = True
while kora_igen:
    main()
    while True:
        ask = input("Köra igen? (j/n)")
        ask = ask.lower()
        if ask == 'j':
            break
        else:
            kora_igen = False
            print("Okej, hejdå!")
            break

#Här tittar vi om vi kör programmet direkt från sidan, ibland när man importerar klasser osv så vill man 
#inte att de ska köras. Därför har man denna if sats


