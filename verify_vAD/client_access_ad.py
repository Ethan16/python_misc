#!C:\python27
#-*-coding:utf8-*-

#from selenium import webdriver

import urllib2

"""
作者：zyc
日期：2017-11-7
功能：PC本地拉起Firefox，访问AD
"""

AD_WAN_URL="http://80.80.80.10/"
TEST="http://www.sahitest.com/demo/php/fileUpload.htm"
FREQUENCY=3

def access_web(weburl):
	fail_count,L=0,range(1,FREQUENCY+1)
	#TODO 需要校验下weburl是否合法
	for i in L:
		try:
			url_access=urllib2.urlopen(weburl).read()
			print u"\n\n这是第%d次读取网页。\n\n"%i,url_access
		except urllib2.HTTPError,e:
			print u'这是一个HTTPError错误，错误信息：',e.code
			fail_count=fail_count+1
		except urllib2.URLError,e:
			print u'这是一个URLError错误，错误信息：',str(e)
			fail_count=fail_count+1
		
	if fail_count>0:
		print u'\n\n总共访问%d次，访问失败%d次，访问地址为：%s，请检查网络情况！'%(len(L),fail_count,weburl)
	else:
		print u'\n\n%d次访问都成功了，访问地址为：%s，干得好！'%(len(L),weburl)

access_web(TEST)
#access_web(AD_WAN_URL)
