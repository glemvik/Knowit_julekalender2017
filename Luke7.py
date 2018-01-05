# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:13:11 2017

@author: gle001
"""
from time import time

start_time = time()

ciphertext = 'OTUJNMQTYOQOVVNEOXQVAOXJEYA'

# To get position of character in alphabet
correction = ord('A') - 1

# Decrypt
plaintext = ''
for letter in ciphertext:
    """
    Encryption: y = (3*ascii_value - 2 * correction) % 26 + correction
    Decryption: x = ((y + correction) * 3_inverse + correction) % 26
    """
    decrypted_letter = ((ord(letter) + correction) * 9 + correction + 1) % 26    
    plaintext += chr(decrypted_letter + correction + 1)

# Results
print('Result:', plaintext)
print('Time:', time() - start_time)