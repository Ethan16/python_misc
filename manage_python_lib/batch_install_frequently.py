# -*- coding: utf-8 -*-

"""
@Date    : 2018-01-04 22:01:00
@Author  : James (euler52201044@163.com)
@Link    : http://www.cnblogs.com/yongqin/
@file:   : batch_install_frequently.py
@Version : 1.0
@Change  : 2018-01-04 22:01:00
"""


import pip
from subprocess import call


# source1:[11](http://www.jb51.net/article/60255.htm)
# source2:[zhihu](https://www.zhihu.com/question/24590883)
# source3:[awesome-python-cn](https://github.com/jobbole/awesome-python-cn),git
# clone local.
installFailed = ['wxpython', 'pymc']
frequentlyLib = ['wget', 'prettytable', 'sh', 'progressbar', 'colorama', 'uuid', 'bashplotlib', 'delorean',
                 'pep8', 'pyvmomi', 'mock>=1.0', 'web.py', 'wxpython', 'pyopengl', 'pymo', 'pillow', 'django', 'pypi-uploader']
salmon = ['pymongo', 'testtools', 'docker-py<=1.7.2,>=1.6.0', 'python-subunit>=0.0.18',
          'testrepository', 'os-testr', 'selenium', 'paramiko', 'IPy', 'castro']
reptile = ['bs4', 'lxml', 'urllib3', 'requests', 'scrapy', 'beautifulsoup']
vnc = ['vncdotool', 'pywinauto', 'paramiko', 'rdpy']
openstack_lib = ['stevedore', 'sqlalchemy', 'eventlet']
auto = ['SendKeys']
web = ['django', 'tornado', 'web.py', 'flask']
db = ['cx_Oracle', 'pymongo', 'redis', 'mysql']
da = ['numpy', 'pandas', 'matplotlib',
      'scipy', 'keras', 'Seaborn', 'TensorFlow']

for fl in web + db:
    call("pip install "+fl, shell=True)
