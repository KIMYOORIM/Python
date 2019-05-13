
import socket

size = 1024
host = '' # all ip that I want to service
port = 8001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(5) # maximum trial count
c, addr = sock.accept()
data = c.recv(size)
if data:
    f = open("receivedData.txt", 'a')
    print("client ip ", addr[0])
    f.write(addr[0])
    f.write(":")
    f.write(data.decode("utf-8"))
    f.close()
sock.close()







