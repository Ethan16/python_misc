# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 15_achievement_grade.py
@time: 2019/5/3 下午8:50
@description: 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""


score = int(input('输入分数 : '))

if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print('%d 成绩等级为: %s' % (score, grade))