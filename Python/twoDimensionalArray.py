import numpy as np

# Day 1 - 11,15,10,6
# Day 2 - 10,24,11,5
# Day 3 - 12,17,12,8
# Day 4 - 15,18,14,9 

week_data = np.array([[11,15,10,6],[10,24,11,5],[12,17,12,8],[15,18,14,9]])
print(week_data)

"""
    # Append a column value
    print("\n Insert and append methods - Column")
    new_week = np.insert(week_data, len(week_data), [[3,6,9,2]], axis=1)
    print("\n ", new_week)

    new_week = np.append(week_data, [[3], [6],[9],[2]], axis=1)
    print("\n ", new_week)


    # Append a row value
    print("\n Insert and append methods - Row")
    new_week = np.insert(week_data, 0, [[47,12,34,2]], axis=0)
    print("\n ", new_week)

    new_week = np.append(week_data, [[1,2,3,4]], axis=0)
    print("\n ", new_week)
"""

# Accessing elements of array
print("\nFunction to access 2D array values based on the index: ")
def accessElements(array, rowIndex, columnIndex): 
    if rowIndex >= len(array) or columnIndex >= len(array): 
        print("The index established for the row or column exceedes the actual index of them")
    else: 
        print(array[rowIndex][columnIndex]) 

accessElements(week_data, 1, 1)

print("\nTraversal Search - 2D Array: ")
def traversalSearch(array): 
    for row in array: 
        for rowItem in row: 
         print(rowItem)
         
traversalSearch(week_data)

#Deletion of elements
print("\nActual array:\n", week_data)

column_deletion = np.delete(week_data, 1, 1)

print("\nColumn deletion:")
print(column_deletion)


row_deletion = np.delete(week_data, 3, 0)

print("\nRow deletion:")
print(row_deletion)