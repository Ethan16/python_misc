# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 17_count_character.py
@time: 2019/5/4 下午3:56
@description: 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
"""

import string

input_string = input('请输入一个字符串 : \n')

letters = 0
space = 0
digit = 0
others = 0
i = 0

while i < len(input_string):
    c = input_string[i]
    # i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
    i += 1

print('char = %d, space = %d, digit = %d, other = %d' % (letters, space, digit, others))
