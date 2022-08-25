# Write awhile loop that starts at the last chacter in the string and works its way backwards to the first character
# in the string, printing each letter on a seperate line, except backwards.

word = 'banana'

index = len(word)-1                              # finds last character in string

while index >= 0:
    letter = word[index]                         # prints out letters in word backwards
    print(letter)
    index = index - 1
