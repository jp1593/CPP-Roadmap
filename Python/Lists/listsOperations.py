# Accessing/Traversing List
shopping_list = ['Milk', 'Cereal', 'Bread']

# Access element
print(shopping_list[0])

# Verify existance of element
print('Milk' in shopping_list) #in operator has a complexity of O(N)

# Traverse the list
for i in shopping_list: 
    print(i)

# Access each element and change the value of each one 
for i in range(len(shopping_list)): 
    shopping_list[i] = "Test"
print(shopping_list)