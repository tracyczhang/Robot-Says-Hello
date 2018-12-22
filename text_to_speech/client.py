#! /usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "128.62.55.181"
port = 
s.connect((host,port))

def ts(str):
   s.send('e'.encode()) 
   data = ''
   data = s.recv(1024).decode()
   print (data)

while 2:
   r = input('enter')
   ts(s)

s.close ()
