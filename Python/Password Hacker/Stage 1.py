import socket
import sys
import itertools as it

with socket.socket() as s:
  
    # 1: connect to the given address
    hostname, port = sys.argv[1:]
    s.connect((hostname, int(port)))

    # 2: construct a string of all possible characters in passwords
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    for i in range(1, len(chars)+1):
        # 3: create combinations of characters
        cbs = (''.join(i) for i in it.product(chars, repeat=i))
        
        # 4: iterate over the combinations and send each item out as a potential password
        for pwd in cbs:
            s.send(pwd.encode())

            # 5: if the server client returns 'Connection success!' as the response, the
            #    password passes the test and we exit the loop immediately
            if s.recv(1024) == b'Connection success!':
                print(pwd)
                exit()
