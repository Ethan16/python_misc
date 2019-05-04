# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 10_format_time.py
@time: 2019/5/2 下午5:20
@description: 
"""

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
