# Write a program to look for the lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average of the integer

import re                                                                 # imports regex library
import math                                                               # imports math library
 
fname = input('Enter a file: ')

try:
    hand = open(fname)
except FileNotFoundError:                                                 # checks if file exists
    print('Error, file not found: ', fname)
    quit()

num_lst = []
for line in hand:
    line = line.rstrip()
    num = re.findall('^New Revision: ([0-9]*)', line)                    # searches and finds all lines of the form 'New Revision: (0-9)*'
    for number in num:
        number = int(number)                                             # converts string number to int number
        num_lst.append(number)

print(math.floor(sum(num_lst) / len(num_lst)))                           # math.floor rounds down number 






