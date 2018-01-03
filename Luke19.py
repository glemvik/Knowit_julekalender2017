#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:39:14 2017

@author: gunvor
"""

from time import time

#-----------------------------------------------------------------------------#
#---------------------------------- M A I N ----------------------------------#
#-----------------------------------------------------------------------------#

start_time = time()

# Read walking pattern
with open('Luke19_pattern.txt') as file:
    
    moves = []    
    for line in file:
        steps, direction = line.split(', ')
        moves.append((int(steps.strip()), direction.strip()))

# Create field
dimension = 50
field = [['#' for j in range(dimension)] for i in range(dimension)]

# Make pattern
x,y = dimension//2, dimension//2
for move in moves:
    steps, direction = move
    
    if direction == 'north':
        
        # Check that we stay inside field
        if y - steps < 0:
            print('ERROR: walking out of field in north direction')
            break
    
        # Walk 'steps' north    
        for step in range(1, steps + 1):
            field[y - step][x] = ' '
        y = y - steps
    
    elif direction == 'south':
         
        # Check that we stay inside field
        if y + steps > dimension - 1:
            print('ERROR: walking out of field in south direction')
            break

        # Walk 'steps' south        
        for step in range(1, steps + 1):
            field[y + step][x] = ' '
        y = y + steps

    elif direction == 'west':
        
        # Check that we stay inside field
        if x - steps < 0:
            print('ERROR: walking out of field in west direction')
            break

        # Walk 'steps' west        
        for step in range(1, steps + 1):
            field[y][x - step] = ' '
        x = x - steps

    elif direction == 'east':
        
        # Check that we stay inside field
        if x + steps > dimension - 1:
            print('ERROR: walking out of field in east direction')
            break
        
        # Walk 'steps' east
        for step in range(1, steps + 1):
            field[y][x + step] = ' '
        x = x + steps

# Print pattern
for line in field:
    for entry in line:
        print(entry, end='')
    print()

# Print results
print('Result: batman')
print('Time:', time() - start_time)