# Rewrite your pay computation with time and a half for overtime and create a function called computepay
# which takes two parameters (hours and rate)


def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        extra_pay = overtime * (rate * .5)
        pay = hours * rate + extra_pay
        return pay


try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Bad data')
    quit()

print(computepay(hours, rate))

