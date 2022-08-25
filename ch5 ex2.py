# Write another program that prompts for a list of numbers as above and at the end prints out the 
# maximum and minimum of the numbers instead of the average


maximum = None
minimum = None

while True:
    num = input('Enter a number: ')                 # asks for number
    if num == 'done':
        break

    try:
        number = int(num)                           # changes input to integer value
    except:
        print('Invalid data')
        continue

    
    if maximum is None or number > maximum:         # finds largest number
        maximum = number
    if minimum is None or number < minimum:         # finds smallest number
        minimum = number

print('Max:', maximum)
print('Min:', minimum)
