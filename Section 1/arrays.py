#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:07:58 2018

@author: johnbaltes
"""

my_list_variable = ["hi", "Hello", "Poop"]
my_tuples_variable = ("hi", "Hello", "Poop")
my_set_variable = {"hi", "Hello", "Poop"}

print(my_list_variable)
print(my_tuples_variable)
print(my_set_variable)

print(my_list_variable[0]+' '+ my_list_variable[2]) #called a subscript or indexing

#-- Use lists can append and index
#-- Adding a variable DOES NOT WORK ON TUPLES
#-- you have to add to it and dont forget to add the comma at the end to add it on. 
#-- Sets can not contain duplicates and has no order

my_list_variable.append("Fuck Off")
print(my_list_variable)

my_tuples_variable = my_tuples_variable + ('Shit',)
print(my_tuples_variable)

my_set_variable.add('bitch')
print(my_set_variable)

