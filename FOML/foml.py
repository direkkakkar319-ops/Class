import numpy as np 

arr = np.array([1, 2, 0, 0, 0, 2, 4])

print(np.nonzero(arr))

# Shallow copy
arr2 =  arr.view()
# deep copy
arr3 = arr.copy()