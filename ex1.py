# revise a previous program as follows: Read and parse "From" lines and pull out the addresses from the line
# Count the number of messages from each person using a dictionary
# after all the data has been read, print the person with the most commits by creating a list of (count, email)
# tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

fname = input('Enter a file: ')

try:
    hand = open(fname)
except FileNotFoundError:
    print('Error, file not found: ', fname)
    quit()

address_name = {}                                                                # creates dictionary

for line in hand:
    line = line.rstrip()
    words = line.split()

    if len(words) < 3 or words[0] != 'From':                                     # searches for lines with "from"
        continue

    address = words[1]                                                           # finds address name
    address_name[address] = address_name.get(address, 0) + 1                     # adds address name to dictionary

address_lst = []                                                                 # creates a list
 
for mail, count in list(address_name.items()):
    address_lst.append((count, mail))                                            # adds tuple pairs to list
    address_lst.sort(reverse=True)
for count, mail in address_lst[:1]:                                              # searches for top tuple pair
    print(mail, count)                                                           # prints address name with most  commits

