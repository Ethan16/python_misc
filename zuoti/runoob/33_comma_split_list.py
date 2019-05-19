# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 33_comma_split_list.py
@time: 2019/5/4 下午6:22
@description: 题目：按逗号分隔列表。
程序分析：无。
"""

L = [1, 2, 3, 4, 5, 6]
S1 = ','.join(str(n) for n in L)
print(S1)