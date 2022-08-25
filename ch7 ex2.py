# Write a program to prompt for a file name, and then read through the file and look for lines of thr form
# 'X-DSPAM-Confidence: 0.8475'
# When you encounter a line that starts with 'X-DSPAM-Confidence:' pull apart the line to extract the floating
# point number on the line. Count these lines and then compute the total of the spam confidence values
# from these lines. When you reach the end of the file, print out the average spam confidence


fname = input('Enter a file name: ')
try:
    hand = open(fname)
except FileNotFoundError:
    print('Error, file not foundL ', fname)
    quit()

num_lst = []                                                      # initalizes a list

for line in hand:
    if line.startswith('X-DSPAM-Confidence:'):                    # checks for lines that start with 'X-DSPAM..'
        dspam = line.find(':')                                    # finds the ':'
        number = line[dspam+1:]                                   # slices line from after ":"
        number = float(number)                                    # converts string number to float number
        num_lst.append(number)                                    # adds float number to list

print(sum(num_lst)/len(num_lst))                                  # computes and prints average



