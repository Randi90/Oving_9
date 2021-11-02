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

with open("oving_1_rein_tekst.txt", "r") as filen:
    for linje in filen:
       linje_nummer += 1
       ordene = linje.split() 
       
       for ordet in ordene:
            ordet = ordet.lower()
            if ordet in ordliste:
                ordliste[ordet]=linje_nummer
                #finnes ordet i dictonary allerede
                #linje_nummer = ordliste[ordet]
               
                #ordliste[ordet] = teller#viss ordent ikke fins i ordlista, settes det inn
                #else:
                    #ordliste[ordet] = 1
                    
                # for num, linje in enumerate(filen,1):
                #     if ordet in ordliste:  
                #         #linje.finn(ordene) >=0
                #         num=ordliste[ordet]
                #         num+=1
                #         ordliste[ordet]=num
                #   #  else:
               
                
    for ordet in ordliste: #for alle ordene i ordlisten
        print(f"Ordet {ordet} forekommer {ordliste[ordet]} linjenummer:")
                


        
#line_num = 0
                    
                  #  line_num += 1
                 
                       # print (line_num)
        
        