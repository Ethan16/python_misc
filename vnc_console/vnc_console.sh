#!/bin/bash
#需求描述:在HCI上的虚拟机控制台上，通过输入用户名密码，完成登录。研究下vnc的自动化
qm monitor ${vmid}
qm monitor 8118753741844

qm> sendkey ctrl-alt-delete

#yw:QemuServer.pm里面有方法直接调用。

ps auxf | grep kv

/sf/etc/init.d/fw.sh stop  #ljb关闭防火墙，才能vnc虚拟机

/usr/bin/kvm -id 8118753741844 -chardev socket,id=qmp,path=/var/run/qemu-server/8118753741844.qmp,server,nowait -mon chardev=qmp,mode=control -vnc 0.0.0.0:0,websocket=6101,to=6200

-vnc 0.0.0.0:0 -> 5900
#问题：现在所有的虚拟机的端口都是0，是怎么映射的？

qm> info vnc
Server:
     address: 0.0.0.0:5900
        auth: none
Client:
     address: 200.201.216.32:40213
  x509_dname: none
    username: none