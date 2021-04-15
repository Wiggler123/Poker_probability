# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:11:00 2021

@author: danne
"""

from plot import plot


def program():
    while True:
        fraga = input("Vad vill du räkna ut sannolikheten för? (par/triss/kåk/färg/fyrtal/stege/färgstege/royal flush)").lower()
        simuleringar = int(input("Hur många simuleringar ska köras: "))
        if simuleringar > 10000000:
            print("För många simuleringar! Om du väljer att fortsätta kommer det ta ett tag för programmet att beräkna sannolikheten.")
            ask_fortsatta = input("Vill du fortsätta? (j/n) ").lower()
            if ask_fortsatta == 'j':
                print("OK")
                pass
            else:
                print("Okej, börja om!")
                continue
        if fraga == 'par':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.plot_par()
            break
        elif fraga == 'triss':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.plot_triss()
            break
        elif fraga == 'färg':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.plot_farg()
            break
        elif fraga == 'kåk':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.plot_kok()
            break
        elif fraga == 'fyrtal':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.plot_fyrtal()
            break

        elif fraga == 'stege':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.plot_stege()
            break
        elif fraga == 'färgstege':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.plot_fargstege()
            break
        elif fraga == 'royal flush':
            s = plot(simuleringar)
            s.plot_royal_flush()
            break
        else:
            print("Du måste skriva par/triss/färg/kåk/stege/fyrtal/färgstege eller royal flush!")
            continue
            


kora_igen = True
while kora_igen:
    program()
    while True:
        ask = input("Köra igen? (j/n)")
        ask = ask.lower()
        if ask == 'j':
            break
        else:
            kora_igen = False
            print("Okej, hejdå!")
            break