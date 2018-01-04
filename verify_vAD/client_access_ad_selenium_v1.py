#!C:\python27
#-*-coding:utf8-*-

from selenium import webdriver

# import urllib2

"""
作者：zyc
日期：2017-11-7
功能：PC本地拉起Firefox，访问AD
"""

AD_WAN_URL="http://80.80.80.10/"
TEST="https://200.201.188.106/"
#FREQUENCY=10

def constantly_access_ad(adurl):
	#L=range(1,FREQUENCY+1)
	dr=webdriver.Firefox()
	
	#for i in L:		
	while True:
		dr.get(adurl)
		print '\nAccess times:%d'%i
	dr.quit()

constantly_access_ad(TEST)
