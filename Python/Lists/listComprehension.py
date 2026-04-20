# Basic way to iterate a list and create another one based on operations of the first one
prev_list = [1,2,3]
new_list = []

for i in prev_list: 
    doubled = i * 2
    new_list.append(doubled)

# List comprehension
comprehension_list = [i*2 for i in prev_list]
print(new_list)
print(comprehension_list)

# List comprehension conditional
example_list = [-1, 10, 20, -12, -20, 4, 6, -17]
negative_square_list = [number**2 for number in example_list if number < 0]
print(negative_square_list)

sentence = "Retro Gaming"
only_consonants = [letter for letter in sentence if letter not in ['a', 'e', 'i', 'o', 'u', ' ']]
print(only_consonants)

