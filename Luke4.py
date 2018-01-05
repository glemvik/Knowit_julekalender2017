#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:43:26 2017

@author: gunvor
"""
from time import time
from collections import Counter

def is_palindrome(word):
    """
    Returns True if 'word' is a palindrome, and False if not
    """    
    return word == word[::-1]


def permutation_is_palindrome(word):
    """
    Check if more than one letter has odd frequency. If True, then no 
    permutation of the word is a palindrome, if False then some permutation is
    a palindrome.
    """
    
    # Count frequency of the letters in the word
    c = Counter(word)
    
    # Check how many frequencies are odd
    odd = 0
    for key,value in c.items():
        if value % 2 != 0:
           odd += 1 
    
    if odd > 1:
        return False
    else:
        return True

#-----------------------------------------------------------------------------#
#---------------------------------- M A I N ----------------------------------#
#-----------------------------------------------------------------------------#

start_time= time()

count = 0    
with open('Word_list.txt') as file:
    for word in file:
        word = word.strip()
        if not is_palindrome(word) and permutation_is_palindrome(word):
            count += 1
            
print('Result:', count)
print('Time:', time() - start_time)
