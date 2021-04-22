import socket

'''Create socket object'''
socket_obj = socket.socket

'''host to connect - this is the server that you like to connect to'''
host = '192.168.0.106'

'''Port set'''
port = 12345

'''Socket object created'''
socket_obj.connect((host,port))
print(socket_obj.recv(1024))

'''Socket closed'''
socket_obj.close()
