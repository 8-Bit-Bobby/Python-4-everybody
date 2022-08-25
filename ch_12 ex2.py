# Change your socket program so that it counts the number of characters it has received and stops displaying
# any text after it has shown 3000 characters. The program should retrieve the entire document and count
# the total number of characters and display the count of the number of characters at the end of the document.


import socket                                                                    # imports socket library

try:
    url = input('Enter a URL: ')                                                 # asks for URL
    host = url.split('/')[2]                                                     # splits URL to get host at index 2
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                   # creates socket connect
    mysock.connect((host, 80))                                                   # connects host to port 80
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'                                     # gets url at server
    cmd = cmd.encode()                                                           # encodes into bytes for delivery
    mysock.send(cmd)
    
    received = b''                                                               # creates an empty byte string
    while True:
        data = mysock.recv(512)                                                  
        if len(data) < 1:
            break
        received += data                                                         # adds data to byte string
    received = received.decode()                                                 # decodes data
    print(received[:3000])                                                       # prints out up to 3000 words
    print(len(received))                                                         # prints length of data                   

    mysock.close()
except:
    print('improperly formatted or non exsistant url')

