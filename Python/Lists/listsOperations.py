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

# Update and Inserting values in a List
exampleList = [1,2,3,4,5,6,7]
print(exampleList)

# Update specific value
exampleList[1] = 100
print(exampleList)

# Insert of elements
# 1. Insert element to the beggining of the list
exampleList.insert(0, 200)
print(exampleList)
# 2. Insert element to any given space in the list
exampleList.insert(4, "SpaceJump")
print(exampleList)
# 3. Insert element to the end of the list
exampleList.append("Last")
print(exampleList)
# 4. Insert another list into the list
exampleList.extend([1,2,3,4])
print(exampleList)
