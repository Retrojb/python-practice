#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:22:13 2018

@author: johnbaltes
Functions

 for n in range(2,100):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number')

"""

#name: input('Enter your name: ')
#print(f'hello {name}')

def greet():
    name = input('Enter your name: ')
    print(f'Good Evening, {name}') 
    ##calling a function
greet() #this runs the above function

def check_primes():
    for num in range(2, 20):
        check_if_prime(num) # num is an arguement, being passed in from the for loop
        
def check_if_prime(n): # n is called the parameter function can receive a value
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number')


check_primes()


def adding():
    print('The Python Adding Machine')
    num_one = float(input('First number: '))
    second_num = float(input('Second number: '))
    sum = num_one + second_num
    print(f'the sum of {num_one} + {second_num} is {sum}')
    print('---- ----- ----- ------ -----')
def subtraction():
    print('The Python Subtracting Machine')
    num_one = float(input('Enter a first number: '))
    second_num = float(input('Enter a second number: '))
    difference = num_one - second_num
    print(f'the difference of {num_one} - {second_num} is {difference}')
    print('---- ----- ----- ------ -----')   
def multiplication():
    print('The Python Multiplication Machine')
    num_one = float(input('Enter the first number: '))
    second_num = float(input('Enter the second number: '))
    product = num_one * second_num
    print(f'the sum of {num_one} + {second_num} is {product}')
    print('---- ----- ----- ------ -----')
def division():
    print('The Python Division Machine')
    num_one = int(input('Enter the Divdend : '))
    second_num = int(input('Enter the Divisor: '))
    quotient = num_one / second_num
    print(f'the division of {num_one} divided by {second_num} is {quotient}')   
    print('---- ----- ----- ------ -----')
def power():
    print('The Python Division Machine')
    num_one = int(input('Enter a the root: '))
    second_num = int(input('To the power of: '))
    sum = num_one**second_num
    print(f'the exponent of {num_one} + {second_num} is {sum}') 
adding()
subtraction()
multiplication()
division()
power()