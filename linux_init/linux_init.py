# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: linux_init.py
@time: 19-3-10 下午1:10
"""

import os


class LinuxInit():
    def __init__(self):
        pass

    # 1.创建目录
    def create_directory(self):
        cmd = 'cd $HOME;mkdir lib;cd lib;mkdir tool src doc;ls -l'
        os.system(cmd)

    # 2.安装软件:git/vim/pip
    def install_software(self):
        install_cmd = 'sudo apt-get install -y git vim python-pip mongodb curl docker docker.io mysql-server mysql-client libmysqlclient-dev'
        os.system(install_cmd)

    # 3.安装第三方库
    def pip_install(self):
        pass

    # 4.下载源码
    def download_src(self):
        pass


if __name__ == '__main__':
    pass
