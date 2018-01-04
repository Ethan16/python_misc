#-*- coding:utf-8 -*-
#python2
#author:rjl
import time
import random
import os
import commands
import threading
def geturl(file_dir):
    dir_list = os.listdir(file_dir)  #获取该目录下所有文件
    file = dir_list[random.randint(0,len(dir_list))]  #随机选取一个文件
    file = os.path.join(file_dir,file)    #拼接完整路径
    f = open(file,'r')
    url_list = f.readlines()    #从文件中读取所有链接
    f.close()
    if len(url_list)==0:
        pass
    url = url_list[random.randint(0,len(url_list)-1)]
    url = url.strip()  #去除路径两端的空格、换行符等
    return url

def run(url,log_name):
    cmd = 'ab -c 100 -n 1000'+url  #使用ab工具并发访问测试网站
    print cmd
    response = commands.getoutput(cmd)  #以shell执行命令
    log = log_name    #保存日志的路径
    try:
        if os.path.exists(log):
            flog = open(log,'a')   #如果文件存在以追加的方式写入
        else:
            flog = open(log,'w')   #文件不存在创建并写入     
    except IOError as err:
        print 'file open error:{0}'.format(err)
    #将执行结果写入日志
    flog.write(response+'\n')
    print url,'Done!!!!'
    flog.close()

def run_main(file_dir,log_name):
    while True:
        url = geturl(file_dir)
        run(url,log_name)
        time.sleep(2)
if __name__ == '__main__':
    file_dir1 = '/leio/URL/'  #链接存放位置
    log_name1 = '/leio/log/'  #日志存放位置
    file_dir2 = '/leio/URL/'  
    log_name2 = '/leio/log/'  
    file_dir3 = '/leio/URL/'  
    log_name3 = '/leio/log/'  
    t1 = threading.Thread(run_main,args=(file_dir1,log_name1))
    t2 = threading.Thread(run_main,args=(file_dir2,log_name2))
    t3 = threading.Thread(run_main,args=(file_dir3,log_name3))
    
    threads = []
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)

    for t in threads:
        t.setDaemon(True)
        t.start()
    
    '''
    这里是为了使程序可以使用Ctrl-c中断执行。
    在此多线程中，子线程死循环执行，永远不会退出，
    而在python线程机制中Ctrl-c只对主线程起效，但是
    设置join()后主线程阻塞，等待子线程执行完毕，
    由此造成Ctrl-c不能中断程序执行。
    ps:此方法会造成cpu资源浪费
    '''
    try:
        t = threads[0]
        while True:
            t.join(2)
            if not t.isAlive:
                break
    except KeyboardInterrupt:
        print "Ctrl-c exit...."












