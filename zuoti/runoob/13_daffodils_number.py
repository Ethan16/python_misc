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
3位水仙花数有4个：
153   = 1^3 + 5^3 + 3^3
370   = 3^3 + 7^3 + 0^3
371   = 3^3 + 7^3 + 1^3
407   = 4^3 + 0^3 + 7^3
"""

for n in range(100, 1000):
    hundreds = int(n / 100)
    # print('hundreds is : %d' % (hundreds))
    tens = int((n - hundreds * 100) / 10)
    # print('tens is : %d' % (tens))
    single = (n - hundreds * 100 - tens * 10)
    # print('single is : %d' % (single))

    # print('Daffodils number is : ')
    cube = hundreds ** 3 + tens ** 3 + single ** 3
    if n == cube:
        # import pdb;pdb.set_trace()
        print('%-5d = %d^3 + %d^3 + %d^3' % (n, hundreds, tens, single))
