# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 8_multiplication_table.py
@time: 2019/5/2 下午4:56
@description: 
"""
print('\nFollowing is multiplication table.')
for i in range(1, 10):
    print('')
    for j in range(1, i + 1):
        print('%d×%d=%d ' % (i, j, i * j), end='')
