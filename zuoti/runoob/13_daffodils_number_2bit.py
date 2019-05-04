# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 13_daffodils_number.py
@time: 2019/5/3 下午4:13
@description: 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
2位水仙花数有0个：
"""

for n in range(10, 100):
    tens = int(n / 10)
    single = (n - tens * 10)

    square = tens ** 2 + single ** 2
    if n == square:
        print('%-4d' % (n), end='')
