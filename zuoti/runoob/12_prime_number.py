# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 12_prime_number.py
@time: 2019/5/3 下午3:54
@description: 题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""

from math import sqrt

# 素数个数计数
number = 0
# 素数标记
leap = 1

for m in range(101, 201):
    k = int(sqrt(m + 1))
    # 核心算法。判断是否素数
    for n in range(2, k + 1):
        if m % n == 0:
            leap = 0
            break
    if leap == 1:
        print('%-5d' % (m), end='')
        number += 1
        if number % 10 == 0:
            print('')
    leap = 1

print('\nThe total is %d .' % (number))
