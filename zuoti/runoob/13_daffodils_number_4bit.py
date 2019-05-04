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
James:此题是计算 4位 水仙花数的，即一个四位数=其各位数字四次方和
4位"水仙花数"有3个：
1634  = 1^4 + 6^4 + 3^4 + 4^4
8208  = 8^4 + 2^4 + 0^4 + 8^4
9474  = 9^4 + 4^4 + 7^4 + 4^4
"""

for n in range(1000, 10000):
    thousands = int(n / 1000)
    hundreds = int((n - thousands * 1000) / 100)
    # print('hundreds is : %d' % (hundreds))
    tens = int((n - thousands * 1000 - hundreds * 100) / 10)
    # print('tens is : %d' % (tens))
    single = (n - thousands * 1000 - hundreds * 100 - tens * 10)
    # print('single is : %d' % (single))

    # print('Daffodils number is : ')
    biquadrate = thousands ** 4 + hundreds ** 4 + tens ** 4 + single ** 4
    if n == biquadrate:
        # import pdb;pdb.set_trace()
        print('%-5d = %d^4 + %d^4 + %d^4 + %d^4' % (n, thousands, hundreds, tens, single))
