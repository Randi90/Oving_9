#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 19:22:52 2021

@author: Randi
"""
#eks:
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage 

    def __str__(self):
        return '__str__ for Car'


my_car=Car("red",98765)
print (my_car.color)


