# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: TcpSerSocketServer.py
@time: 19-3-25 下午10:38
"""

import SocketServer
from time import ctime

# HOST = '127.0.0.1'
HOST = ''
PORT = 6666
ADDR = (HOST, PORT)


class MyRequestHandler(SocketServer.StreamRequestHandler):
    def handler(self):
        # print('...connected from:', self.client_address)

        # self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
        # [todo]no recevie method.stop here.
        self.data = self.request


tcpSer = SocketServer.TCPServer(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpSer.serve_forever()
