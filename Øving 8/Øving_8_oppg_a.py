#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:19:11 2021

@author: Randi
"""

# Ordteller for tekstfil:
#   Les inn ei tekstfil   # 1:lese gjennom en tekstfil
#   Finn alle ordene   # 2:For hvert ord i tekstfila skal programmet registrere ordet og linjenummeret der ordet først forekommer i et dictionary
#   Tell antall forekomster av hvert ord   #3:skrive ut ordene og linjenumrene


ordliste = dict()
linje_nummer=0

with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for linje in fila:
        
        ordene = linje.split()
        linje_nummer += 1
        for ordet in ordene:
            ordet = ordet.lower()
            ordet=ordet.strip(",.()*")
            #ordliste[ordet] = linje_nummer
            if ordet in ordliste:
                
                linje_nummer = ordliste[ordet]
                
                #ordliste[ordet] = linje_nummer
            else:
                ordliste[ordet] = linje_nummer
    for ordet in ordliste:
        print(f"Ordet {ordet} forekommer på linje {ordliste[ordet]}")


        
#line_num = 0
                    
                  #  line_num += 1
                 
                       # print (line_num)
        
        