from time import time


def sum_of_series(limit):
    
	"""
    Returns the sum of the first 'limit' numbers in the series where:
	* Every entry is at least as big as the previous (a_(i+1) >= a_i)
	* The value in the a_i describes the number of occurrences of number i
	* The series start at a_i = 1
	"""

	# Prepare values
	a = [1]
	index = 1
	number = 2

	# Build the series
	while True:    
        	
		# Find the number of occurrences of 'number'    
		if len(a) <= index:        
			occurrences = number    
		else:        
			occurrences = a[index]    
    
		# Append 'number' to the series 'occurrences' amount of times    
		for i in range(occurrences):        
            		
			# Return when we reach the 'limit' number of entries        
			if len(a) == limit:            
				return sum(a)        
			else:            
				a.append(number)    
        	
		# Increment counters    
		number += 1    
		index += 1

#------------------------------------------------------------------------------#
#---------------------------------- M A I N -----------------------------------#
#------------------------------------------------------------------------------#

start_time = time()

limit = 1000000 

print('Result:', sum_of_series(limit))
print('Time:', time() - start_time)