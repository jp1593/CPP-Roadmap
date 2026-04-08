# Native array module
import array

first_array = array.array('i')
print(first_array)
second_array = array.array('i', [1,2,3,4,])
print(second_array)

# Numpy array
import numpy as np
first_np_array = np.array([], dtype=int)
print(first_np_array)
second_np_array = np.array([1,2,3,4], dtype=int)
print(second_np_array)