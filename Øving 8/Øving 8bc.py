#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:49:00 2021

@author: Randi
"""

class Spørsmål:
    def __init__(self, spørsmål, svar, alternativ):
        self.spørsmål=spørsmål
        self.svar=svar
        self.alternativ=alternativ
        
    def __str__(self):
        tekst=self.spørsmål +"\n"
        for i in range(len(self.alternativ)):
            tekst += f"({i+1}) {self.alternativ[i]} \n"
        return tekst
    
    def sjekk_svar(self):
        svar_bruker=int(input("hva er svaret? "))
        if svar_bruker == self.svar:
            print("riktig")
        else: 
            print("ikke riktig")
        

quiz = Spørsmål("Hva er hovedstaden i Norge? ",1, ["Oslo","Trondheim","Stavanger"])
quiz1 = Spørsmål("Hvilken farge er en pære? ",2, ["rød","grønn","brun"])

print(quiz)
quiz.sjekk_svar()

print(quiz1)
quiz1.sjekk_svar()

#funksjon med lister av spørsmål som me ønske å spør bruker
#def run_test(spørsmål):
    #score=0
    #for spørsmål in spørsmål:
        #brukerens svar til spørsmålet
        #svar=input(spørsmål.spørsmål)
        #kjekke om svaret er korekt
        #if svar==spørsmål.svar:
            #brukeren får et poeng om svaret er riktig
            #score+=1
    #viser hvor mange spørsmål brukeren fikk riktig
    #print("Du fikk" +str(score) + "/" + "3"+ "riktig")
    
#run_test(spørsmål)