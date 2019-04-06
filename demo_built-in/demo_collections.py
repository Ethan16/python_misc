# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence
@contact: euler52201044@sina.com
@file: demo_collections.py
@time: 19-4-6 下午22:59
"""

from collections import namedtuple, deque

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])
q = deque(['a', 'b', 'c'])
q.append('x')
q.append('y')
print(q)
