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
James:此题是计算 6位 水仙花数的，即一个6位数=其各位数字6次方和
6位"水仙花数"有1个：
548834 = 5^6 + 4^6 + 8^6 + 8^6 + 3^6 + 4^6
"""

for n in range(100000, 1000000):
    lakhs = int(n / 100000)
    ten_thousands = int((n - lakhs * 100000) / 10000)
    thousands = int((n - lakhs * 100000 - ten_thousands * 10000) / 1000)
    hundreds = int((n - lakhs * 100000 - ten_thousands * 10000 - thousands * 1000) / 100)
    tens = int((n - lakhs * 100000 - ten_thousands * 10000 - thousands * 1000 - hundreds * 100) / 10)
    single = (n - lakhs * 100000 - ten_thousands * 10000 - thousands * 1000 - hundreds * 100 - tens * 10)

    sixth_power = lakhs ** 6 + ten_thousands ** 6 + thousands ** 6 + hundreds ** 6 + tens ** 6 + single ** 6
    if n == sixth_power:
        # import pdb;pdb.set_trace()
        print('%-6d = %d^6 + %d^6 + %d^6 + %d^6 + %d^6 + %d^6' % (n, lakhs, ten_thousands, thousands, hundreds, tens, single))
