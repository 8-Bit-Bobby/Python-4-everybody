# This program counts the distibution of the hour of the day for eah of the messages. You can pull the hour from 
# the "From" line by finding the time string and then splitting that string into parts using the ":" character.
# Once you have accumalated the counts for each hour, prints out the counts, one per line, sorted by hour as shown below
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


fname = input('Enter a file: ')

try:
    hand = open(fname)
except FileNotFoundError:
    print('Error, file not found: ', fname)
    quit()  

hour_count = {}    

for line in hand:
    line = line.rstrip()
    words = line.split()

    if len(words) < 3 or words[0] != 'From':                                         # checks for lines that start with "From"
        continue

    hour = words[5][:2]                                                              # locates the hour in the line
    hour_count[hour] = hour_count.get(hour, 0) + 1                                   # adds hour to dictionary

hour_list = []                                                                       # creates a list

for hour, count in list(hour_count.items()): 
    hour_list.append((hour, count))                                                  # adds tuples pairs to list
    hour_list.sort()
for hour, count in hour_list:
    print(hour, count)                                                               # prints hour, count sorted by hour

