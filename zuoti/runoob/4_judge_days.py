# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 4_judge_days.py
@time: 2019/5/2 下午3:12
@description: 题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

# 输入年、月、日
year = int(input('Year : \n'))
month = int(input('Month : \n'))
day = int(input('Day : \n'))

sum_days = 0
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if not (0 < day < 32):
    print('Day error.')

if 0 < month < 13:
    sum_days = months[month - 1]
else:
    print('Month error.')

# 总天数
sum_days += day

# 处理闰月
leap = 0

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1

if (leap == 1) and (month > 2):
    sum_days += 1

# 打印出第几天
print('It is the %dth day.' % (sum_days))
