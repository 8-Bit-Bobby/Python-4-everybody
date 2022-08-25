# Write a program to read through the mail box data and when you find lines that start  with 'From'
# you will split the line into words using the split function. We are interested in who sent the message, 
# which is the second word on the From line
# Parse the From line and print out the second word for each From line, then you will also count the number
# of From lnes and print out the count at the end.

fname = input('Enter a file: ')

try:
    hand = open(fname)
except FileNotFoundError:
    print('Error, file not found ', fname)
    quit ()

counts = 0
for line in hand:
    line = line.rstrip()
    words = line.split()

    if len(words) < 3 or words[0] != 'From':              
        continue

    sender = words[1]                                                    # finds who sent the message
    counts += 1                                                          # increments count of lines with 'From'
    print(sender)                                                        # prints out all message senders

print('There were', counts, 'lines with From as the first word')

