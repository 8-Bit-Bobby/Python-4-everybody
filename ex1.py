# Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
# You can use the split('/') to break the URL into its component parts so you can extract the host name 
# for the socket connect call. Add error checking using try and except to handle the condition where the user enters
# an improperly formatted or non exsistant URL

import socket                                                                    # imports socket library

try:
    url = input('Enter a URL: ')                                                 # asks for URL
    host = url.split('/')[2]                                                     # splits URL to get host at index 2
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                   # creates socket connect
    mysock.connect((host, 80))                                                   # connects host to port 80
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'                                     # gets url at server
    cmd = cmd.encode()                                                           # encodes into bytes for delivery
    mysock.send(cmd)

    received = b''
    while True:
        data = mysock.recv(512)                                                  # recieves in 512 page chunks
        if len(data) < 1:
            break
        print(data.decode(), end='')

    mysock.close()
except:
    print('Invalid URL')
    quit()
    