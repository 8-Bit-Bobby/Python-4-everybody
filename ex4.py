# Shakespeare used over 20,000 words in his works. But how would you determine that?
# How would you produce the list of all the words that Shakespeare used? Would you download
# all his work, read it and track all unique words by hand? lets use Python to achieve this instead.
# list all unique words, sorted in alphabetical order, that are stoed in a file called 'romeo.txt'


unique_words = []                                                      # initalizes a list

fname = input('Entera file name: ')                                    # asks for file
try:
    hand = open(fname)                                                 # checks if file can be located and opened
except FileNotFoundError:                                              
    print('Error, file not found: ', fname)
    quit()

for line in hand:                                                      # searches lines in file
    line = line.rstrip()                                               # strips whitespace                 
    words = line.split()                                               # splits each line into words
    for word in words:
        if word not in unique_words:                                   # checks if word is in list
            unique_words.append(word)                                  # adds word to list
        
unique_words.sort()                                                    # sorts list
print(unique_words)
