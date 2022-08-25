# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regulare expression and count the number of lines that matched the regular expression

import re                                                                       # imoport regular expression library

fname = input('Enter a file: ')
regex = input('Enter a regular expression: ')
counts = 0

try:
    hand = open(fname)
except FileNotFoundError:
    print('Error, file not found: ', fname)
    quit()

for line in hand:
    line = line.rstrip()
    if re.search(regex, line):                                                 # search for given expression in given line
        counts += 1

print(fname, 'had', counts, 'lines that matched', regex)


