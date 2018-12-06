#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:19:38 2018

@author: johnbaltes
"""

set1 = {1, 2, 3, 6}
set2 = {4, 2, 3, 6}

#-- intersection of a set elements that match between the two lists

print(set1.intersection(set2))

print(set1.union(set2))

print(set1.difference(set2))

#-- EXTENSION OF SETS
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
user_input = input('Add the name of a friend: ')
# Add the name to the empty set
nearby_people.add(user_input)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(nearby_people)