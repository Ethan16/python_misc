# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: TcpCli.py
@time: 19-3-24 下午12:29
"""


from socket import *

HOST = '127.0.0.1'
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input("> ")
    # if not data:
    #     break

    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break

    print(data)

tcpCliSock.close()

