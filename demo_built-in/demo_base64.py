# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: demo_base64.py
@time: 2019/4/7 上午8:57
@description: 
"""

import base64

encode = base64.b64encode(b'i love you.')
print(encode)

decode = base64.b64decode(b'aSBsb3ZlIHlvdS4=')
print(decode)