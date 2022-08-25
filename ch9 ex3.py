# Write a program to read through a mail log, build a histogram using a dictionary to count how
# many messages have come from each email address, and print the dictionary

fname = input('Enter a file: ')                                                   # asks for a file
try:
    hand = open(fname)
except FileNotFoundError:                                                         # checks if file can be located
    print('Error, file not found: ', fname)
    quit()

email_address_log = {}                                                            # initalize a dictionary

for line in hand:
    line = line.rstrip()
    words = line.split()

    if len(words) < 3 or words[0] != 'From':                                       # searchs for non whitespace lines
        continue                                                                   # and lines not beginning with 'From'
                                                                                   
    email = words[1]                                                               # finds email
    email_address_log[email] = email_address_log.get(email, 0) + 1                 # increments email in dictionary

print(email_address_log)
