#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:05:34 2018

@author: johnbaltes
"""

numbers = list(range(11))

## the old way
doubled_numbers = []
for num in numbers:
    doubled_numbers.append(num * 2)
print(doubled_numbers)

##List Comphrehension

doubles = [n*2 for n in numbers]
print(doubles)

phrases = [f'I am {age} years old' for age in doubles]
print(phrases)

items_list = ['turkey', 'read', 'cheese']
uppercase_items = [item.upper() for item in items_list]

evens = [n for n in numbers if n % 2 == 0]
print(evens)

friends = ['rolf', 'anna', 'charlie']
guests = ['Mary', 'Jose', 'ruth']

present_friends = [name.capitalize() for name in guests if name.lower() in friends]
print(present_friends)