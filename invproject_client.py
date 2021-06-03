import os
import socket
import sys
import paramiko
import getpass
from Crypto.Cipher import AES

en = os.urandom(16)
de = os.urandom(16)

def encrypt(message):
    obj = AES.new(b"aabbccddeeffgghh", AES.MODE_CFB,b"aabbccddeeffgghh")
    enc = obj.encrypt(message)
    return enc

def decrypt(message):
    obj = AES.new(b"aabbccddeeffgghh", AES.MODE_CFB,b"aabbccddeeffgghh")
    dec = obj.decrypt(message)
    return dec


print ("\n\n   Welcome to nash's SSH server   \n\n")
uname = input("  Enter username	: ")
passw = getpass.getpass(prompt = "  Enter password	: ")
p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
if(uname == "zahinruslee99", passw == "Password5712"):
        p.connect("192.168.56.102", port=22, username= uname, password = passw)
        print("\n**********Connection Passed**********\n\n")
else:
        print("  Wrong username/password")
        p.close()
        exit()

servername = "192.168.56.102"
port = 8080
csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csock.connect((servername,port))
cmd = input("  Enter cmd : ")
while cmd != "exit":
    eout = encrypt(cmd)
    csock.send(eout)
    cont = csock.recv(2048)
    dout = decrypt(cont)
    cmd = dout.decode()
    print ("  Executing " ,cmd,"...........")
    stdin,stdout,stderr = p.exec_command(cmd)
    b = stdout.read()
    c = stderr.read()
    print ("\n",b.decode('utf-8'))
    print ("\n",c.decode('utf-8'))
    cmd = input("  Enter cmd : ")
    if cmd == "exit":
        sys.exit()
csock.close()
p.close()
sys.exit()
