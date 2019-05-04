# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 1_three_figures.py
@time: 2019/5/1 下午4:52
@description: 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

TOTAL = 0

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                TOTAL += 1
                print(i, j, k)

print("[Sum]Total : %d" % (TOTAL))