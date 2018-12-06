#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:09:17 2018

@author: johnbaltes
if loops

"""

programmer = True
is_programmer = False
is_awesome = True

if programmer is True:
    print("Cool dude")
    
if is_programmer is True:
    print("poop dick")
else:
    print("you suck")

if is_programmer is False:
    print("Why wouldn't you be")
else:
    print("You're awesome")

if is_programmer is False or is_awesome is False :
    print('Way to Go')
elif is_programmer is False and is_awesome is True : 
    print('Wow')
else:
    print('error')