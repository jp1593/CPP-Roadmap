from array import array as arr
from array import * 
# 1. Create an arrray and traverse
print("\nPoint 1")
basic_array = arr('i', [1,2,3,4])

for i in basic_array: 
    print(i)
    
# 2. Access individual elements trough indexes
print("\nPoint 2")
""" Change the number inside the [] to have a different output value from the elements in the array """
print(basic_array[0])

# 3. Append any value to the array using append() method
print("\nPoint 3")
basic_array.append(10)
print(basic_array)

# 4. Insert value in an array using insert method()
print("\nPoint 4")
basic_array.insert(2, 100)
print(basic_array)

# 5. Extend python array using extend() method
print("\nPoint 5")
values_to_add = 67,48
basic_array.extend(values_to_add)
print(basic_array)

# 6. Add items from list into array using fromlist() method
print("\nPoint 6")
list = [1000,600,20,23, 2, 3]
basic_array.fromlist(list)
print(basic_array)

# 7. Remove any array element using remove() method
print("\nPoint 7")
basic_array.remove(2)
print(basic_array)

# 8. Remove last array element using pop() method
print("\nPoint 8")
basic_array.pop(0)
print(basic_array)

# 9. Fetch any element through its index using index() method
print("\nPoint 9")
print(basic_array.index(2))

# 10. Reverse a python array using reverse() method
print("\nPoint 10")
basic_array.reverse()
print(basic_array)

# 11. Get array buffer information trough buffer_info() method
print("\nPoint 11")
print(basic_array.buffer_info()) 

# 12. Check for number of occurences of an element using count() method
print("\nPoint 12")
print(basic_array.count(3))

# 13. Convert array to string using tostring() method
print("\nPoint 13")
str_array = basic_array.tobytes() 
print(str_array)

print('Reconverted String')
int_array = arr('i')
int_array.frombytes(str_array)
print(int_array)

# 14. Convert array to a python list with same elements using tolist() method
print("\nPoint 14")
basic_array.tolist()
print(basic_array)

# 15. Append a string to char array using fromstring() method
print("\nPoint 15")
char_array = arr('u', ['c', 'o', 'c','a'])
string_appendance = arr('u', 'Cola')
char_array.frombytes(string_appendance.tobytes())
print(char_array)

# 16. Slice Elements from an array
print("\nPoint 16")
element_slice = basic_array[1:9]
print(element_slice)




