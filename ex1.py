# Write a program that repeatedly asks for numbers until the user enters 'done'.
# Once 'done' in entered, print out the total, count, and average of numbers.
# If the user enters anything other than a number, detect the mistakke using try and except
# and print an error message and skip to the next number

total = 0
count = 0

while True:
    num = input('Enter a number: ')
    if num == 'done':                                   # checks if input is = 'done'
        break

    try:
        number = int(num)                               # checks if input can be converted to integer
    except:
        print('Invalid input')
        continue
 
    total = total + number                               # adds up total           
    count += 1                                           # increments count of entered numbers

average = total/count                                    # computes average
print(total, count, average)





