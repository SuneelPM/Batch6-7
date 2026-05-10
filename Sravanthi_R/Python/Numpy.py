# import numpy as np 
# list=np.arange(10)
# print(list)

# import numpy as np
# s=list(range(10))
# print(s)

import numpy as np
import sys
import time
arr=np.arange(1000)
listarr=list(range(1000))
list_size=sys.getsizeof(listarr)
arr_size=arr.nbytes
print(list_size)
print(arr_size)

start_time=time.time()
sum_list=np.sum(listarr)
end_time=time.time()
total_time=(end_time-start_time)*1000
print("Total time taken by list",total_time)

start_time=time.time()
sum_array=np.sum(arr)
end_time=time.time()
total_time=(end_time-start_time)*1000
print("Total time taken by numpy array",total_time)