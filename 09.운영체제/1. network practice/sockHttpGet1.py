import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.nate.com", 80))


data = ''
try:
    sock.sendall(b"GET / HTTP/1.1\r\nHost: nate.com\r\n\r\n")
    data = sock.recvfrom(1024)
except socket.error:
    print ("Socket error", socket.errno)
finally:
    print("closing connection")
    sock.close()

strdata = data[0].decode("utf-8")
print( strdata.splitlines())

