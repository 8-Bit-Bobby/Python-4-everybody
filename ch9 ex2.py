# Write a program that categorizes each mail message by which day of the week the commit was done. To do this
# look for lines that start with "From", then look for the third word and keep a running count of each of 
# the days of the week. At the end of the program print out the contents of your dictionary
# order does not matter

fname = input('Enter a file: ')
try:
    hand = open(fname)
except FileNotFoundError:
    print('Error, file not found: ', fname)
    quit()

day_count = {}

for line in hand:
    line = line.rstrip()
    words = line.split()

    if len(words) < 3 or words[0] != 'From':
        continue

    day = words[2]
    day_count[day] = day_count.get(day, 0) + 1

print(day_count)
