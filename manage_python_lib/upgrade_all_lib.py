# -*- coding: utf-8 -*-

"""
@Date    : 2018-01-04 21:57:21
@Author  : James (euler52201044@163.com)
@Link    : http://www.cnblogs.com/yongqin/
@file:   : upgrade_all_lib.py
@Version : 1.0
@Change  : 2018-01-04 21:57:21
"""


import pip


from subprocess import call
for dist in pip.get_installed_distributions():
    call("pip install --upgrade "+dist.project_name, shell=True)
