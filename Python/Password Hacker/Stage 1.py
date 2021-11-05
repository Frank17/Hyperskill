import socket
import sys

with socket.socket() as s:
  
    hostname, port, message = sys.argv[1:]
    s.connect((hostname, int(port)))
    
    s.send(message.encode())
    
    response = s.recv((1024)).decode()
    print(response)
