#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:22:14 2018

@author: johnbaltes
"""

def add(x, y):
    return x + y;

# lamda annoymous functions
    
lambda x, y: x+y
(lambda x, y: x+y)(10, 5)
#this will get auto destroyed cause has no function
#do not do the above


#define them like this, easier to right short functions
add = lambda x, y: x+y

#First Class Function

def who(data, identify):
    return identify(data)

def my_identifier_fuction(some_data):
    return some_data['name']

user = {'name': 'John', 'surname': 'Baltes'}
print(who(user, lambda x: x['name']))