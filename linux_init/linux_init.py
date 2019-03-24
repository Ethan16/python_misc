# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: linux_init.py
@time: 19-3-10 下午1:10
"""

from subprocess import call
import pexpect


class LinuxInit():
    def __init__(self):
        pass

    # 0.更新源和软件
    def update_env(self):
        # cmd = "sudo apt-get update;sudo apt-get upgrade;sudo apt-get install -y python-dev"
        install_cmd = "sudo apt-get install -y python-dev"
        process = pexpect.spawn(install_cmd, timeout=30)
        process.expect("sudo")
        process.send("xxx\n")
        output = process.read()
        print(output)

    # 1.创建目录
    def create_directory(self):
        cmd = "cd $HOME;mkdir lib;cd lib;mkdir tool src doc;ls -l"
        call(cmd, shell=True)
        call("ls -l", shell=True)

    # 2.安装软件:git/vim/pip
    # [done]getpass input password.
    def install_software(self):
        install_cmd = "sudo apt-get install -y git vim python-pip mongodb curl docker docker.io mysql-server mysql-client libmysqlclient-dev"
        process = pexpect.spawn(install_cmd, timeout=30)
        process.expect("sudo")
        process.send("xxx\n")
        output = process.read()
        print(output)

    # 3.安装第三方库
    def pip_install(self):
        third_libs = ['wget', 'pep8', 'scrapy', 'paramiko', 'django', 'pymongo', 'selenium', 'mysql', 'numpy', 'pandas',
                      'tensorflow', 'testrepository', 'opencv-python']
        for third_lib in third_libs:
            call("pip install " + third_lib, shell=True)

    # 4.下载源码
    def download_src(self):
        src_addr = ['git@github.com:Ethan16/python_misc.git', 'git@github.com:Ethan16/crawl.git',
                    'git@github.com:Ethan16/c_cpp_misc.git', 'git@github.com:Ethan16/tcl_misc.git',
                    'git@github.com:Ethan16/shell_misc.git', 'git@github.com:Ethan16/bat_ps_misc.git']
        public_addr = ['https://github.com/torvalds/linux.git', 'https://github.com/qemu/qemu.git',
                       'https://github.com/stanzhai/be-a-professional-programmer.git',
                       'https://github.com/jobbole/awesome-python-cn.git',
                       'https://github.com/scrapy/scrapy.git', 'https://github.com/SeleniumHQ/selenium.git',
                       'https://github.com/wangshub/Douyin-Bot.git', 'https://github.com/tensorflow/tensorflow.git',
                       'https://github.com/cuanboy/ScrapyProject.git']
        # call("cd $HOME/lib/src/")
        for src in src_addr + public_addr:
            call("cd $HOME/lib/src/;git clone " + src, shell=True)
        call("ls -l")


if __name__ == '__main__':
    init = LinuxInit()
    init.update_env()
    init.create_directory()
    init.install_software()
    init.pip_install()
    init.download_src()
