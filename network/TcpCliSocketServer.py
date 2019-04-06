# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: TcpCliSocketServer.py
@time: 19-3-25 下午10:47
"""

# import SocketServer
from socket import *

HOST = '127.0.0.1'
# HOST = ' localhost '
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    data = raw_input('> ')

    # if not data:
    #     break

    tcpCliSock.send('%s\r\n' % data)

    data = tcpCliSock.recv(BUFSIZE)

    # if not data:
    #     break

    print data.strip()
    # tcpCliSock.close()
