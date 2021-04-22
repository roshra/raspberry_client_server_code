import socket

'''Create a socket object'''
socket_obj = socket.socket()

'''accept connection from any host'''
host = ""

'''Print host'''
print("Hostname is {}".format(host))

'''port to bind'''
port = 12345

'''Bind a port'''
socket_obj.bind((host,port))

'''wait for client connection'''
socket_obj.listen(5)

'''Establish connection with client'''
c,addr = socket_obj.accept()

'''print connection achieved'''
print("Got connection from client {}".format(addr))

'''Send a message to client'''
c.send("Thanks for connecting from raspi")
c.close()


