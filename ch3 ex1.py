# Rewrite your pay computation to give employee 1.5 times the hourly rate for hours worked over 40 hours.

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    overtime = hours - 40
    overtime = overtime * (rate * .5)

pay = hours * rate + overtime
print('Pay: ', pay)

