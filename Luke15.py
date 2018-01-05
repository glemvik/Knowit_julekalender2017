# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:59:12 2017

@author: gle001
"""

from time import time

def find_cuts(trees):
    """
    Returns the number a list of the number of trees that are cut at each 
    iteration, when all trees are cut by the height of the smallest tree.
    """
    
    # Sort for easy finding smallest tree
    trees = sorted(trees)
    
    # Perform cuts until all trees have zero height
    number_of_cuts = []
    while len(trees) > 0:
        
        # Get smallest tree. All trees in list will be cut at this iteration
        cut = trees[0]
        number_of_cuts.append(len(trees))
        
        # Update list of trees
        trees = [(tree - cut) for tree in trees if (tree - cut) > 0]
    
    return number_of_cuts


#---------------------------------------------------------------------------#
#--------------------------------- M A I N ---------------------------------#
#---------------------------------------------------------------------------#

start_time = time()

trees = [23, 74, 26, 23, 92, 92, 44, 13, 34, 23, 69, 4, 19, 94, 94, 38, 14, 9, 51, 98, 72, 46, 17, 25, 21, 87, 99, 50, 59, 53, 82, 24, 93, 16, 88, 52, 14, 38, 27, 7, 18, 81, 13, 75, 80, 11, 29, 39, 37, 78, 55, 17, 78, 12, 77, 84, 63, 29, 68, 32, 17, 55, 31, 30, 3, 17, 99, 6, 45, 81, 75, 31, 50, 93, 66, 98, 94, 59, 68, 30, 98, 57, 83, 75, 68, 85, 98, 76, 91, 23, 53, 42, 72, 77]
number_of_cuts = find_cuts(trees)

print('Result:', number_of_cuts)
print('Time:', time() - start_time)