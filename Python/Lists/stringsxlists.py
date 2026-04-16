# Strings and Lists

# list()
stringVariable = "SuperJam"
conversion = list(stringVariable)
print(conversion)

# split()
multipleWords = "Space Jam Universe"
print(multipleWords.split())

wordsWithoutSpace = "Carrot-of-the-bony"
delimiter = '-'
listOfWords  = wordsWithoutSpace.split(delimiter)
print(listOfWords)

# joint()
print(delimiter.join(listOfWords))