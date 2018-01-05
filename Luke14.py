# Hello World program in Python

from time import time    
    
def number_of_ways(steps, moves):
    """
    Returns the number of ways of walking up a staircase of 30 steps by taking
    1, 2 or 3 steps at a time.
    """
    
    # Prepare table and base case for DP
    T = [0 for i in range(steps + 1)]
    T[0] = 1
    
    # Solve subproblems
    for i in range(len(T)):
        for move in moves:
            if i - move >= 0:
                T[i] += T[i - move]
    
    return T[1:]


#------------------------------------------------------------------------------#
#----------------------------------- M A I N ----------------------------------#
#------------------------------------------------------------------------------#

start_time = time()

# Initialize
steps = 30
moves = [1,2,3]

# Calculate
number = number_of_ways(steps, moves)

print('Result:', number[-1])
print('Time:', time() - start_time)