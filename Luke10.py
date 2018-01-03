# -*- coding: utf-8 -*-

from time import time
from collections import deque


def find_survivor(number):
    """
    Returns the last man standing of the christmas party. A bottle is passed
    around the table. If you get the bottle, the next person is eliminated. If
    the person before you get the bottle, you are eliminated. 
    """
    
    # Initialize the deque
    remaining_people = deque([i for i in range(1, number + 1)])
    
    # Iterate through the queue, until only one person is left
    is_serving = True
    while len(remaining_people) > 1:
        
        # Get current person
        person = remaining_people.popleft()
        
        # If the person gets the bottle
        if is_serving:
            remaining_people.append(person)
            is_serving = False
        
        # If the previous person had the bottle
        else:
            is_serving = True
    
    return remaining_people.popleft()


def V(k):
    
    if k == 2: return 1
    if k % 2 == 0: return V(k//2) * 2 - 1

    n = k // 2 + 1
    return ((V(n) - 2) % n + 1) * 2 - 1
        

#-----------------------------------------------------------------------------#
#---------------------------------- M A I N ----------------------------------#
#-----------------------------------------------------------------------------#
start_time = time()

number = 1500
survivor = find_survivor(number)

print('Result from queue:', survivor)
print('Result from formula:', V(number))
print('Time:', time() - start_time)




assert V(7) == 7
assert V(4) == 1
assert V(2) == 1
assert V(5) == 3
assert V(1500) == 953
