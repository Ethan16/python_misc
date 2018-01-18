# -*- coding: utf-8 -*-

"""
@Date    : 2018-01-12 13:29:53
@Author  : Ethan (euler52201044@163.com)
@Link    : https://github.com/Ethan16
@file    : demo_data_analysis.py
@usage   : 
@Version : 1.0
@Change  : 2018-01-12 13:29:53
"""


import numpy


def main():
    lst = [[1, 4, 5], [4, 5, 99]]
    print(type(lst))

    np_lst = numpy.array(lst)
    print(type(np_lst))

    np_lst = numpy.array(lst, dtype=numpy.float)
    # bool,int,int8,int16,int32,int64,int128,uint8,uint16,uint32,uint64,uint128,float,float16,float32,float64,complex64/128
    print(type(np_lst))
    print np_lst.shape
    print np_lst.ndim  # 维度,dimensionality
    print np_lst.dtype
    print np_lst.itemsize
    print np_lst.size

    # 2 some Arrays
    print numpy.zeros([2, 4])
    print numpy.ones([3, 5])

    print numpy.random.rand(2, 5)
    print numpy.random.rand()
    print "Randint: "
    print numpy.random.randint(1, 10, 4)    #
    print "Randn: "
    print numpy.random.randn(2, 4)
    print "Choice: "
    print numpy.random.choice([10, 20, 30, 2, 45, 44])
    print "Distribute: "
    print numpy.random.beta(1, 10, 100)

    # 3 Array operation
    print numpy.arange(1, 11).reshape([2, -1])
    lst = numpy.arange(1, 11).reshape([2, -1])
    print numpy.exp(lst)
    print numpy.exp2(lst)
    print numpy.sqrt(lst)
    print numpy.sin(lst)
    print "Log: "
    print numpy.log(lst)

    print "\n"
    lst_one = numpy.arange(1, 25).reshape([6, -1])
    print lst_one
    print lst_one.sum(axis=0)

    print "\n"
    lst_two = numpy.array([[[1, 2, 3, 4],
        [4, 5, 6, 7]],
        [[7, 8 ,9, 10],
        [10, 11, 12, 13]],
        [[14, 15, 16, 17],
        [18, 19, 20, 21]]
        ])
    print lst_two.sum(axis=2)
    print "Max: "
    print lst_two.max(axis=1)
    print "Min: "
    print lst_two.min(axis=0)
    print "Dot: "
    # print numpy.dot(lst_one, lst_two)


if __name__ == '__main__':
    main()
