# -*- coding: utf-8 -*-

from time import time
from math import sqrt

def mirptall(primes):
    """
    Returns all positive 'mirptall' smaller than 'number', where 'mirptall' are
    primes which are also primes when the digits are reversed without being 
    palindromes.
    """
    
    # INITIALIZE
    primes = set(primes)
    mirptall = []
    
    # WORK THROUGH SET OF PRIMES
    while primes:
        prime = primes.pop()
        reverse_prime = int(str(prime)[::-1])
        
        # IF NOT PALINDROME AND REVERSE OF PRIME IS PRIME
        if prime != reverse_prime and reverse_prime in primes:
            
            # ADD BOTH 'MIRPTALL' AND REMOVE FROM SET OF PRIMES
            mirptall.append(prime)
            mirptall.append(reverse_prime)
            primes.remove(reverse_prime)
        
    return mirptall

def primes(number):
    """
    Returns an array of all primes smaller than 'number'.
    """
    
    # INITIALIZE
    primes = [2]
    
    # WORK THROUGH LIST
    for number in range(3, number):
        index = 0
        is_prime = True
        
        # CHECK DIVISIBILITY BY PRIME NUMBERS
        while index < len(primes) and primes[index] < sqrt(number) + 1:
            
            # DIVISIBLE BY OTHER PRIME -> NOT PRIME
            if number % primes[index] == 0:
                is_prime = False
                break
            
            index += 1

        # IF NOT DIVISIBLE BY OTHER PRIMES -> APPEND TO PRIMES            
        if is_prime:
            primes.append(number)
    
    return primes

#-----------------------------------------------------------------------------#
#---------------------------------- M A I N ----------------------------------#
#-----------------------------------------------------------------------------#
start_time = time()

number = 1000

# FIND PRIMES BELOW 'number'
primes = primes(number)

# FIND 'MIRPTALL' AMONG PRIMES
mirptall = mirptall(primes)

print('Result:', len(mirptall))
print('Time:', time() - start_time)