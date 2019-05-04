# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 9_sleep.py
@time: 2019/5/2 下午5:12
@description: 
"""

import time

myDict = {1: 'a', 2: 'b'}

for key, value in dict.items(myDict):
    print(str(key) + ' ' + str(value))
    time.sleep(1)
