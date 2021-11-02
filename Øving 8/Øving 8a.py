#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:45:06 2021

@author: Randi
"""

# Ordteller for tekstfil:
#   Les inn ei tekstfil   # 1:lese gjennom en tekstfil
#   Finn alle ordene   # 2:For hvert ord i tekstfila skal programmet registrere ordet og linjenummeret der ordet først forekommer i et dictionary
#   Tell antall forekomster av hvert ord   #3:skrive ut ordene og linjenumrene


ordliste = dict()
teller=0

with open("oving_1_rein_tekst.txt", "r") as filen:
    for linje in filen:
       ordene = linje.split()
       for ordet in ordene:
            ordet = ordet.lower()
            if ordet in ordliste:#finnes ordet i dictonary allerede
                teller = ordliste[ordet]
                teller += 1 
                ordliste[ordet] = teller
            else:
                ordliste[ordet] = 1
                    
                for num, linje in enumerate(filen, 1):
                    if ordet in ordliste:
                        num=ordliste[ordet]
                        num+=1
                        ordliste[ordet]=num
                    #else:
                         #print('linjenummer:', num)
                
                
            for ordet in ordliste: #for alle ordene i ordlisten
                print(f"Ordet {ordet} forekommer {ordliste[ordet]} linjenummer: ",num)
        
        




    


#def index(filename,word_list):

    #infile = open(filename, 'r')
   # dct = {}
    #count = 0
   # for line in file:
        #count += 1
       # newLine = line.replace('\n', ' ')
        #if newLine == ' ':
            #continue
        #newLine2 = removePunctuation(newLine)
        #split_line = newLine2.split()
        #for word in word_list:
           # if word in split_line:
                #if word in dct:
                  #  dct[word] += [count]
               # else:
                   # dct[word] = [count]
   # for word in word_list:
        #print('{:12} {}'.format(word,dct[word]))
 #infile.close()
        