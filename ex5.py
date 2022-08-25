


import socket

try:
    url = input('Enter a URL: ')
    host = url.split('/')[2]
except:
    print('Invalid URL!')
    quit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

recieved = b''       # creates empty byte string

while True:
    data = mysock.recv(512)
    if len(data) < 1:
         break
    recieved += data
    
recieved = recieved.decode()
start = recieved.find('But')
print(recieved[start:])
