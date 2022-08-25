# encapsulate the previous code in a function named 'count', and generalize it so that it accepts the string and
# letter as arguments.


def count(string, letter):
    counts = 0
    for letter1 in string:
        if letter1 == letter:
            counts += 1
    return counts

string = input('Enter the sentance you would like to search through: ')
letter = input('Enter your letter: ')
print(count(string, letter), 'is how many times this letter appears!')

        
