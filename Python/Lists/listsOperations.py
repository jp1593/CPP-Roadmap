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

# Slicing and deletion on a List

# Slicing
list_slice = exampleList[2:12]
print(list_slice)

# Changing values with slice usage
list_slice[:2] = [123, 'This is']
print(list_slice)

# Deletion

# pop()
list_slice.pop(0)
print(list_slice)
list_slice.pop()
print(list_slice)

# delete()
del list_slice[0]
print(list_slice)

# remove()
list_slice.remove(4)
print(list_slice)

# Element Search
# in operator
search_list = [10, 20, 30, 33, 40, 44, 27, 99, 102] 
print(search_list)

target = 27 
if target in search_list: 
    print(f"{target} is in List")
else: 
    print(f"{target} isn't in the List")

# Linear Search
def linear_search(list, target): 
    for i, value in enumerate(list): 
        if value == target: 
            return (f"Target value: {value}, is in index: {i}")
    return -1

print(linear_search(search_list, target))

# List opeartions / functions
a = [1,2,3,4]
b = [5,6,7,8]

# + operator
print(a+b)

# * operator
print(a*2)

# len()
print(len(a))

# max()
print(max(a))

# min()
print(min(a))

# sum() 
print(sum(a))

# Exercise - List operators average based on inputs entered by the user
total = 0
count = 0
values_list = [] 
while(True): 
    inp = input('Enter a number:')
    if inp == 'done': 
        result = sum(values_list) / len(values_list)
        break
    values_list.append(float(inp))
print("Average", result)