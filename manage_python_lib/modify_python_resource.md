# -*- coding: utf-8 -*-

"""
@Date    : 2018-01-04 22:02:50
@Author  : James (euler52201044@163.com)
@Link    : http://www.cnblogs.com/yongqin/
@file:   : modify_python_resource.md
@Version : 1.0
@Change  : 2018-01-04 22:02:50
"""

## 方法一
pip -i http://pypi.douban.com/simple install Flask -- trusted-host pypi.douban.com

## 方法二
1. Linux
$mkdir ~/.pip
$cd .pip;touch pip.conf
$vim pip.conf                     #windows上，编辑 pip.ini 文件
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple/

2. Windows
\Lib\site-packages\pip\models\index.py

#PyPI = Index('https://pypi.python.org/')  
PyPI = Index('https://pypi.douban.com/')