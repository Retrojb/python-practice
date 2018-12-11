#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:20:02 2018

@author: johnbaltes
"""

primes = [2,3,5,7,11,13]

for prime in primes:
    print(f'{prime} is a prime number')
    
kids_age = [4, 6, 9]

for age in kids_age:
    print(f'I have a {age} year old kid')
    
for i in range(20):
    print(i)
    ##range doesnt produce a list it is a generator
    
my_friends = {
        'Jose': 6,
        'Bob': 5,
        'Amy': 10
    }
for name in my_friends:
    print(f'I last saw {name} {my_friends[name]} days ago')

##OTHER OPTION IN PYTHON^3.0.0
for name, days in my_friends.items():
    if name == 'Jose':
        print('I know Jose')
    print(f'I last saw {name} {days} days ago')
    
print(my_friends.items())
for t in [('Jose', 6), ('Bob', 5), ('Amy', 10)]:
    ##prints a tupil
    ##n = name and v = value python sees that you want n to be the first thing in the tuple and v the second  making them equal to t
    n,v = t
    print(n)
    print(t)

who_do_I_know = 'Bob'
if who_do_I_know in my_friends:
    print(f'I know Bob')