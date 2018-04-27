# -*- coding: utf-8 -*-

"""
@Date    : 2018-01-12 13:30:53
@Author  : Ethan (euler52201044@163.com)
@Link    : https://github.com/Ethan16
@file    : da_learn_data.py
@usage   : 
@Version : 1.0
@Change  : 2018-01-12 13:30:53
"""

import numpy


a = numpy.array([1, 2, 3])

# print type(a)

# print a.shape

a = a.reshape((1, -1))

# print a.shape

a = numpy.array([1, 2, 3, 4, 5, 6])

a = a.reshape((2, -1))

print a.shape
print a
