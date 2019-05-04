# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 18_isotopic_number.py
@time: 2019/5/4 下午4:16
@description: 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
注意:Python3中reduce不是内建函数了，需要引用进来。Python2中是内建函数，可以直接使用。
https://blog.csdn.net/mouday/article/details/78910056
"""

from functools import reduce

Tn = 0
Sn = []

n = int(input('n = '))
a = int(input('a = '))

for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

Sn = reduce(lambda x, y: x + y, Sn)

print('计算和为 : %d' % (Sn))
