import numpy as np
import sys
list_array = np.arange(10000)
list_p = list(range(10000))
Lst_size=sys.getsizeof(list_array)
arr_size=list_array.nbytes

import time
start_time=time.time()
s_lst=sum(list_p)
end_time=time.time()
print(s_lst)
total_time=(end_time-start_time)*10000
print("Total time taken by list:",total_time)

start_time=time.time()
list_array=sum(list_array)
end_time=time.time()
total_time=(end_time-start_time)*10000
print("Total time taken by numpy array",total_time)


