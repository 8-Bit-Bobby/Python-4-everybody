# Write a program to read through a file and print the contents of the file (line by line) all in upper case.


fname = input('Enter a file name: ')                        # asks for a file
try:
    fhand = open(fname)                                     # checks to see if file can be opened
except FileNotFoundError:                                   # if not, error is sent back and program ends
    print('Error, file not found: ', fname)
    exit()

for line in fhand:                                          # searches lines in file
    line = line.strip()                                     # strips whitespace
    print(line.upper())                                     # prints lines in uppercase

    