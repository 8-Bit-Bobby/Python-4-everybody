# Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert
# all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation
# or anything other than the letters a-z.

import string                                                                       # imports string library

fname = input('Enter a file: ')

try:
    hand = open(fname)
except FileNotFoundError:
    print('Error, file not found: ', fname)
    quit()

letter_count = {}                            
for line in hand:
    line = line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))                 # removes any punctuation and special characters
    line = line.translate(str.maketrans('', '', string.digits))                      # removes any digits
    line = line.lower()
    words = line.split()

    for word in words:
        for letter in word:
            letter_count[letter] = letter_count.get(letter, 0) + 1                   # searches for and adds letters to dictionary

letter_frequeancy_list = []
for letter, count in list(letter_count.items()):
    letter_frequeancy_list.append((count, letter))                                   # adds tuple pairs to list
    letter_frequeancy_list.sort(reverse=True)
for count, letter in letter_frequeancy_list:
    print(letter, count)


