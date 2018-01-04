#!C:\python27

"""
实现的大体思路：
	1.ssh远程到HCI上，执行命令。拿到虚拟机的vnc端口号。paramiko|base64
	2.vnc远程连接虚拟机。vncdotool
	3.执行登录Windows命令。pywinauto/vncdotool/PyAutoIt/opencv/selenium/
		a.直接获取Windows登录窗口的元素，设置认证信息，点击登录。？
		b.开机后，设置无密登录，重启后直接进入Windows。http://blog.csdn.net/sogouauto/article/details/44622099
		c.通过VMTools的通道，传入某些命令，作用与UI填入认证信息一致。？
		d.rdpy:重量级。https://github.com/citronneur/rdpy
"""

import os
import paramiko
import vncdotool
import re
import time
import base64

hostIP="200.201.216.32"
hostPort="22"
hostUser="root"
hostPwd="sangfor123sangfornetwork"
vmID="8118753741844"
vmVNCPort=""
vmUser="Adminisrator"
vmPwd="Sangfor123"
logFile=os.getcwd()+os.path.sep+"vnc_console"+time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+".log"

#create log file.
if not os.path.exists(logFile):
	file=open(logFile,'wb')
	file.close()

#ssh连接host，并执行命令。需要执行的命令包括：1.关闭防火墙；2.qm monitor ${vmid}；
#3.qm> sendkey ctrl-alt-delete；4.qm> info vnc (获取虚拟机的vnc端口号)
def sshHostExecCmd(hostip,port,hostuser,hostpwd,execcmd,logFile):
	paramiko.util.log_to_file(logFile)
	key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))  #问题1：里面要如何设置？

	s=paramiko.SSHClient()
	#s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.get_host_keys().add(hostip, 'ssh-rsa', key)
	s.connect(hostname=hostname, port=port, username=username, password=password)

	stdin, stdout, stderr = s.exec_command(execcmd)

#获取虚拟机的vnc端口
def getVmVNCPort(hostIP,vmID):
	pass

#VNC连接vm，并执行登录。分2步：1.发送ctrl-alt-delete(或者在ssh里面做)；2.输入认证信息并登录
#200.201.216.32:5900,https://200.201.216.44/?m=/mod-console/index&n-hfs&vmid=8118753741844&vmname=win2003_32_Sangfor123clone
#200.201.216.32:5901,https://200.201.216.44/?m=/mod-console/index&n-hfs&vmid=342406369858&vmname=redhat6.5_admin123
#设置Windows无需用户密码即可登录。(control userpasswords2)http://blog.csdn.net/sogouauto/article/details/44622099
def vncVmLogin(hostIP,vmVNCPort,execcmd,logFile):
	pass


