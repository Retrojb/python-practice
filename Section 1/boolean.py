#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:22:03 2018

@author: johnbaltes
"""

truthy = True
falsy = False;

age = 20;
is_over_age = age >= 18;
is_under_age = age <= 18;
is_twenty = age == 20;
print(is_over_age)
print(is_under_age)
print(is_twenty)

my_number = 10
user_numer = int(input("Enter a number: "))

print(my_number == user_numer)

age >= 18 and age < 65

yes = True and True
no = True and False

print(no);

"""
'or is used to get the second value if the one is False.
 If the first one is True it gets the first value

"""

which_one_is_it = True or False
second_one = False or True
first_one = True or False;
neither = False or False
absolute = not False;  # True

print(absolute);

another_no = not True #False

is_programmer = True
is_learning = False
is_designer = False
great_guys = (is_programmer or is_designer) and not is_learning  # either programmer or designer and is learning 
print(great_guys)