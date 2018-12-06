#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:28:17 2018

@author: johnbaltes
"""

#gathering the users name, age, and how many months old they are

input_name = input('Enter your name: ')

print(f'Hello, {input_name}')

input_age = input('Enter your age: ')
months = int(input_age)

print(f'You have lived for {months * 12 } months')

#should be written like this

input_age2 = int(input('Enter you age: '))
seconds = input_age2 * 365 * 24 * 60 * 60
print(f'You have lived for {seconds} seconds')
print(f'You have lived for {input_age2 * 3.154e+7} seconds')