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
James:此题是计算 5位 水仙花数的，即一个5位数=其各位数字5次方和
5位"水仙花数"有3个：
54748 = 5^5 + 4^5 + 7^5 + 4^5 + 8^5
92727 = 9^5 + 2^5 + 7^5 + 2^5 + 7^5
93084 = 9^5 + 3^5 + 0^5 + 8^5 + 4^5
"""

for n in range(10000, 100000):
    ten_thousands = int(n / 10000)
    thousands = int((n - ten_thousands * 10000) / 1000)
    hundreds = int((n - ten_thousands * 10000 - thousands * 1000) / 100)
    # print('hundreds is : %d' % (hundreds))
    tens = int((n - ten_thousands * 10000 - thousands * 1000 - hundreds * 100) / 10)
    # print('tens is : %d' % (tens))
    single = (n - ten_thousands * 10000 - thousands * 1000 - hundreds * 100 - tens * 10)
    # print('single is : %d' % (single))

    # print('Daffodils number is : ')
    fifth_power =ten_thousands ** 5 + thousands ** 5 + hundreds ** 5 + tens ** 5 + single ** 5
    if n == fifth_power:
        # import pdb;pdb.set_trace()
        print('%-5d = %d^5 + %d^5 + %d^5 + %d^5 + %d^5' % (n, ten_thousands, thousands, hundreds, tens, single))
