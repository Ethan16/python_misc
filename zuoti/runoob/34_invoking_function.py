# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 34_invoking_function.py
@time: 2019/5/4 下午6:30
@description: 
"""


def hello_world():
    print('Hello python!')


def three_hellos():
    for i in range(3):
        hello_world()


if __name__ == '__main__':
    three_hellos()
