#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:33:04 2018

@author: johnbaltes
Loop keywords
"""

##break

cars = ['ok', 'ok', 'ok', 'ok', 'defective', 'ok', 'ok']

for car_status in cars:
    if car_status == 'defective':
        print('car is defective')
        break
    print(f'This car is {car_status}')

##Continue 
for num in range(2,10):
    if num % 2 == 0:
        print(f'found an even number {num}')
        continue
    print(f'found a number {num}')
    
##Prime number search
    
for n in range(2,1000):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number')
            