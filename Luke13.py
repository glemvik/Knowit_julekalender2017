# -*- coding: utf-8 -*-


from time import time
import heapq


def order_of_choices(number):
    """
    Create order of choices for Alice ('0') and Bob ('1')
    """
    
    # Alice starts
    order = '0'
    
    # Order is decided by Thue-Morse
    while len(order) < number:
        to_append = ''
        
        # Find the bitwise negation of current order
        for element in order:
            to_append += str((int(element) + 1) % 2)
        
        # Append bitwise negation of current order to current order
        order += to_append
    
    return order[:number]

#-----------------------------------------------------------------------------#
#---------------------------------- M A I N ----------------------------------#
#-----------------------------------------------------------------------------#
start_time = time()

# Create priority queue of items based on (negative) values
stash = []
with open('Luke13_utbytte.txt') as file:
    for line in file:
        item, value = line.strip().split(', ')
        heapq.heappush(stash, (-int(value), item))

# Create order of choices
number_of_items = len(stash)
order = order_of_choices(number_of_items)

# Choose items
bob_value = 0
for i in range(number_of_items):
    value, item = heapq.heappop(stash)
    
    # Bob's turn
    if order[i] == '1':
        bob_value -= value
    
# Print results
print('Result:', bob_value)
print('Time:', time() - start_time)

# Assertions
assert(number_of_items == len(order))