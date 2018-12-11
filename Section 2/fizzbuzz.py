#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:49:14 2018

@author: johnbaltes
"""

num = 0 

for num in range(0,101):
    for x in range(0, num):
        if num % x == 3:
            print('fizz')
            continue
    else:
        print(num)
   