import os
import subprocess
import socket
from Crypto.Cipher import AES
from _thread import *

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


host = "192.168.56.102"
port = 8080
threadcount = 0
ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssocket.bind((host, port))
ssocket.listen(5)
if True:
    print ("Success creating socket")
    print ("Listening ...........")

else:
    print ("Fail")
    ssocket.close()

def clientThread(consocket,addr):
   while True: 
    try:
#        consocket, addr = ssocket.accept()
#        print ("\n\n********** ", addr , "connected to server  **********\n\n")
        com = consocket.recv(2048)
        temp = decrypt(com)
        cmd = temp.decode()
        while(cmd != "exit" and cmd != ""):
            print (addr, "  ", cmd)
            dout = encrypt(cmd)
            consocket.send(dout)
            com = consocket.recv(2048)
            dout = decrypt(com)
            cmd = dout.decode()
            if (cmd == "exit"):
                print ("broken")
                consocket.close()
                break
        consocket.close()
    except Exception:
        pass


while True:
    consocket, addr = ssocket.accept()
    print ("\n\n********** ", addr , "connected to server  **********\n\n")
    start_new_thread(clientThread,(consocket,addr ))
    threadcount += 1
    print ("Thread Number = " , threadcount)
consocket.close()
