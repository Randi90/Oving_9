#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:38:54 2021

@author: Randi
"""

ordliste = dict()
teller=0

with open("oving_1_rein_tekst.txt", "r") as filen:
    for linje in filen:
       ordene = linje.split()
       for ordet in ordene:
            ordet = ordet.lower()
            if ordet in ordliste:
                teller = ordliste[ordet]
                teller += 1 
                ordliste[ordet] = teller
                ordliste[ordet] = 1
                    
                for num, linje in enumerate(filen, 1):
                    if ordet in linje:
                        num=ordliste[ordet]
                        num+=1
                        ordliste[ordet]=num
                   # else:
                         #print("linjenummer:", num)
                
                
            for ordet in ordliste: #for alle ordene i ordlisten
                print(f"Ordet {ordet} forekommer: {ordliste[ordet]}, linjenummer: ",num)