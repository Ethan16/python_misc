# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 11_rabbit_number.py
@time: 2019/5/2 下午5:27
@description: 
"""

f1 = 1
f2 = 1

for i in range(1, 22):
    print('%12ld %12ld' % (f1, f2), end='')
    if (i % 3) == 0:
        print('')
    f1 = f1 + f2
    f2 = f1 + f2
