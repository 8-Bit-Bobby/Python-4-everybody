# Add code to the previous program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has beeen created, look through the 
# dictionary using a maximum loop to find who has the most messages and print how many messagaes
# that person has.

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

#print(email_address_log)

max_address = ""
maximum = 0

for mail in email_address_log:
    if email_address_log[mail] > maximum:
        max_address = mail
        maximum = email_address_log[mail]

print(max_address, maximum)
