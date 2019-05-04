# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 5_sort_number.py
@time: 2019/5/2 下午3:37
@description: 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""

numbers = []

# 输入3个数
for i in range(4):
    x = int(input('Integer %d : \n' % (i+1)))
    numbers.append(x)

# 排序
numbers.sort()

#打印出来
print('Sort numbers is : ')

for number in numbers:
    print(number)
