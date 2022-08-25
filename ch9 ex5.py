# This program records the domain name where the message was sent from instead of who the mail
# came from. wt the end of the program, print out the contents of your dictionary

fname = input('Enter a file: ')                                                     # asks for file

try:
    hand = open(fname)
except FileNotFoundError:                                                           # checks if file exists
    print('error, file not found: ', fname)
    quit()

domain_name = {}                                                                    # creates dictionary

for line in hand:
    line = line.rstrip()
    words = line.split()

    if len(words) < 3 or words[0] != 'From':                                        # searches for lines starting with from
        continue

    address = words[1]
    domain = address.split('@')[1]                                                  # finds domain name
 
    domain_name[domain] = domain_name.get(domain, 0) + 1                            # adds to dictionary

print(domain_name)





