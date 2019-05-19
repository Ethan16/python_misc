# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 20_free_fall_height.py
@time: 2019/5/4 下午5:08
@description: 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
程序分析：无
"""

tour = []
height = []

hei = 100.0
tim = 10

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)

print('总高度: tour = {0}'.format(sum(tour)))
print('第10次反弹高度为: height = {0}'.format(height[-1]))
