# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: debug.py
@time: 19-3-11 下午10:31
"""

# import subprocess
import pexpect, subprocess


def debug_expect():
    cmd = "sudo apt-get install -y python-dev"
    process = pexpect.spawn(cmd, timeout=30)
    process.expect("sudo")
    process.send("deepin77zyc\n")
    output = process.read()
    print(output)
    cmd = "sudo apt-get update;sudo apt-get upgrade;sudo apt-get install -y python-dev"
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    # debug_getpass()
    debug_expect()
