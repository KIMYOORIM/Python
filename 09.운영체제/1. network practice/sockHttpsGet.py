
import ssl

import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.naver.com', 443))

s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)

s.sendall(b"GET / HTTP/1.1\r\nHost: daum.net\r\n\r\n")



while True:



    received = s.recv(4096)
    print(received.decode("utf-8"))

    if not received:

      s.close()

      break

