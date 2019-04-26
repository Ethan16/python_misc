# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: demo_urllib.py
@time: 2019/4/7 下午12:33
@description: 
"""


from urllib import request

with request.urlopen('https://t1.onvshen.com:85/gallery/22162/29420/0.jpg') as f:
    data = f.read()
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s : %s' % (k, v))
    print('Data: ', data.decode('utf-8'))