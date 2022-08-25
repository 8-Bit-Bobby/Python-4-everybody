# # Sometimes when programmers get bored or want to have a little fun, they add a harmless easter egg to their program.
# Modify the program that prompts the user for a file name so that it prints a funny message when the user types
# in 'na na boo boo'. The program should behave normally for all other files which exist and dont exist.

fname = input('Enter a file name: ')

if fname.startswith('na na boo boo'):                                       # adds hidden easter egg
    print('NA NA BOO BOO TO YOU - You have been punked bitch!')
    quit()

try:
    hand = open(fname)
except FileNotFoundError:
    print('Error, file not foundL ', fname)
    quit()

num_lst = []

for line in hand:
    if line.startswith('X-DSPAM-Confidence:'):
        dspam = line.find(':')
        number = line[dspam+1:]
        number = float(number)
        num_lst.append(number)

print('Average Spam confidence: ', sum(num_lst)/len(num_lst))
