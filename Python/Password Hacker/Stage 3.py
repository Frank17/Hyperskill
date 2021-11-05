import socket
import sys
import itertools as it

# before running the program, download the file used from here:
#       https://stepik.org/media/attachments/lesson/255258/passwords.txt
# then save it as passwords.txt and upload it to the same directory of execution

with socket.socket() as s, open("password.txt") as pwd_file:
    
    hostname, port = sys.argv[1:]
    s.connect((hostname, int(port)))

    pwd_list = pwd_file.read().split('\n')

    for pwd in pwd_list:
        pwds = (''.join(p) for p in it.product(
                *zip(pwd.lower(), pwd.upper())
        ))

        for pwd in pwds:
            s.send(pwd.encode())

            if s.recv(1024) == b'Connection success!':
                print(pwd)
                exit()
