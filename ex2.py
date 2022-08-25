# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
# by printing a message and exciting the program. 

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input ')
    quit()

if hours > 40:
    overtime = hours - 40
    overtime = overtime * (rate * .5)

pay = hours * rate + overtime
print('Pay: ', pay)
