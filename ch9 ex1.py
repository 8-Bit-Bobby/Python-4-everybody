# Write a program that reads words in 'words.txt' and stores them as keys in a dictionary.
# It doesnt matter what the values are. Then you can use the 'in' operator as a fast way to 
# check whether a string is in the dictionary

word_count = dict()                                   # initalize a dictionary

fhand = open('words.txt')                             # opens 'words.txt'
for line in fhand: 
    words = line.split()
    for word in words:
        word_count[word] = 'value'                     # adds word to dictionary and sets it to 'value'

print(word_count)



