# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:11:00 2021

@author: danne
"""

from plot import plot


def program():
    while True:
        fraga = input("Vad vill du räkna ut sannolikheten för? (par/triss/kåk/färg/fyrtal)")
        simuleringar = int(input("Hur många simuleringar ska köras: "))
        if simuleringar > 10000000:
            print("För många simuleringar! Om du väljer att fortsätta kommer det ta ett tag för programmet att beräkna sannolikheten.")
            ask_fortsatta = input("Vill du fortsätta? (j/n) ")
            if ask_fortsatta == 'j':
                print("OK")
                pass
            else:
                print("Okej, börja om!")
                continue
        if fraga == 'par':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.__plot_par__()
            break
        elif fraga == 'triss':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.__plot_triss__()
            break
        elif fraga == 'färg':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.__plot_farg__()
            break
        elif fraga == 'kåk':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.__plot_kok__()
            break
        elif fraga == 'fyrtal':
            print("Vänligen vänta medans programmet räknar ut sannolikheten")
            s = plot(simuleringar)
            s.__plot_fyrtal__()
            break
        else:
            print("Du måste skriva par/triss/kåk/färg eller fyrtal!")
            continue


kora_igen = True
while kora_igen:
    program()
    while True:
        ask = input("Köra igen? (j/n)")
        print(ask)
        if ask == 'j':
            break
        else:
            kora_igen = False
            print("Okej, hejdå!")
            break