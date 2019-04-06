# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: tsTservTW.py
@time: 19-3-31 下午3:24
"""

from twisted.internet import protocol, reactor
from time import ctime

PORT = 6666

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        client = self.client = self.transport.getPeer().host
        print('...connected from : ', client)

    def dataReceived(self, data):
        return self
