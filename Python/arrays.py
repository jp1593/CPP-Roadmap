# Native array module
import array

# Array definition + initialization
first_array = array.array('i')
second_array = array.array('i', [1,2,3,4,])
print(second_array)
# .insert(x,y) = inserts the value in a specific index, x = index, y = value
# append(x) = inserts the value at the end of the array
second_array.insert(4,6)
print(second_array)


# Numpy array
import numpy as np

# Array definition + initialization
first_np_array = np.array([], dtype=int)
second_np_array = np.array([1,2,3,4], dtype=int)
print(second_np_array)

""" Numpy requires to re-assign the value to a variable, since np.insert is a fucntion that
threats the array as a read-only. """ 

second_np_array = np.insert(second_np_array, 1, 20)
print(second_np_array)

# Traversal Array
""" Function of visiting each element of the array until the end of it """
def TraverseArray(array): 
    for i in array: 
        print(i)

TraverseArray(second_array)
