# Use urllib to replicate the previous exercise of (1) retrieving the document from an URL, 
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters as the
# output of your program. Do not display the paragraph text, only count them.

import urllib.request                                                  # imports urllib.request function

url = input('Enter a URL: ')                                           # asks for url
fhand = urllib.request.urlopen(url).read()                             # urllib does all the socket connect work and gives back file
fhand = fhand.decode()                                                 # data is decoded

print(fhand[:3000])                                                    # prints up to 3000 characters
print(len(fhand))                                                      # prints length of file




            
