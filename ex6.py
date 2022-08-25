# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and 
# minimum of the numbers at the end when the user enters 'done'. write the program to store the numbers
# the user enters in a list and use the max() and mmin() functions to compute maximum and minimum
# numbers after the loop completes

num_lst = []

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        number = float(num)
    except:
        print('invalid input')
        continue

    num_lst.append(number)

print('Maximum: ', max(num_lst))
print('Minimum: ', min(num_lst))


