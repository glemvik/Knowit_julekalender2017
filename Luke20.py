# -*- coding: utf-8 -*-


from time import time

#-----------------------------------------------------------------------------#
#---------------------------------- M A I N ----------------------------------#
#-----------------------------------------------------------------------------#

start_time = time()

limit = 1024
result = sum((i * (i + 1) // 2) for i in range(1,limit+1))

# Print results
print('Result:', result)
print('Time:', time() - start_time)
