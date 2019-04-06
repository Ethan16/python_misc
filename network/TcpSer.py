# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: TcpSer.py
@time: 19-3-24 下午12:28
"""


from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")

    tcpCliSock, addr = tcpSerSock.accept()

    print("...connected from:", addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)

        if 's' in data:
            tcpCliSock.send("[Server]Client send me s.\n")

        if not data:
            data = "nothing"
            tcpCliSock.send("[Server]Client send me nothing.\n")
            # break

        tcpCliSock.send("[%s] %s" % (ctime(), data))

        # tcpCliSock.close()

tcpSerSock.close()