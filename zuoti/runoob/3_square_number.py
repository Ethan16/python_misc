# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 3_square_number.py
@time: 2019/5/2 下午2:56
@description: 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""

for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i;
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print('%d + 100       = %d * %d = %d' % (x, n, n, n * n))
            print('%d + 100 + 168 = %d * %d = %d' % (x, m, m, m * m))
            print('Square number is : %d' % (x))
