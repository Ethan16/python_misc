#!C:\python27
#-*-coding:utf8-*-

from selenium import webdriver
#from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#import wait
import time
import re

HCI_IP='200.201.188.106'
#HCI_IP='200.201.136.116'
HCI_USER_NAME='admin'
HCI_USER_PWD='sangfor123'
#AD_VMID=3590808821638
#AD_VMID=445801565642
#AD_VMID=430801565642
AD_VMID=7458706160170
AD_USER_NAME='admin'
AD_USER_PWD='admin'
BAK_FILE=r"\\200.200.164.111\vtt_share\12-NFV\NFV_HCI5.3\vAD\adconf_1_2017-11-07.bcf"

def ad_resume_back(hciip):
	dr=webdriver.Firefox()
	#dr=webdriver.Chrome()
	hci_url='https://%s/login'%hciip
	ad_url='https://%s/?m=/mod-vnet/dev/web/index&n-hfs&id=%s'%(hciip,AD_VMID)

	print u'HCI login page is : ',hci_url
	#全局隐性等待，45秒超时。
	dr.implicitly_wait(45)
	dr.get(hci_url)
	
	dr.find_element_by_css_selector("#user_name").send_keys(HCI_USER_NAME)	
	dr.find_element_by_css_selector("#password").send_keys(HCI_USER_PWD)	
	dr.find_element_by_css_selector("#login").click()
	#如果没有登录成功，重试一遍
	#longin_hci_js=javascript:seajs.require('jquery')('#user_name').val('admin').next().val('sangfor123').next().next().next().click();
	if not WebDriverWait(dr,10).until(EC.title_contains('SANGFOR')):
		dr.find_element_by_css_selector("#user_name").send_keys(HCI_USER_NAME)	
		dr.find_element_by_css_selector("#password").send_keys(HCI_USER_PWD)	
		dr.find_element_by_css_selector("#login").click()
			
	#https://200.201.188.106/?m=/mod-vnet/dev/web/index&n-hfs&id=3590808821638
	dr.get(ad_url)
	print u'AD console page is : ',ad_url

	#WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
	dr.switch_to_frame("mainFrame")	
	
	if EC.alert_is_present():
		dr.find_element_by_css_selector("#msg_qd").click()
		print 'Current password is default.'
	dr.switch_to_default_content()

	#selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: //*[@id="left_menu_8"]/a/b
	#NoSuchFrameException: Message: leftFrame	

	locator = (By.CSS_SELECTOR, '#id_left > iframe')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
	dr.switch_to_frame("leftFrame")

	#1.系统配置：#left_menu_8 > a > b
	#dr.find_element_by_css_selector("#left_menu_8 > a > b")
	
	locator = (By.CSS_SELECTOR, '#left_menu_8 > a > b')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
	element_tmp.click()
	#time.sleep(5)

	#2.设备管理：#left_menu_8_0 > a
	locator = (By.CSS_SELECTOR, '#left_menu_8_0 > a')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
	element_tmp.click()
	#http://blog.csdn.net/huilan_same/article/details/52338073
	dr.find_element_by_css_selector("#left_menu_8_0 > a").click()
		
	dr.switch_to_default_content()
	dr.switch_to_frame("mainFrame")
	#3.配置备份与恢复：ul.tag_gray:nth-child(3) > a:nth-child(1)
	locator = (By.CSS_SELECTOR, 'ul.tag_gray:nth-child(3) > a:nth-child(1)')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))	
	element_tmp.click()

	#4.从文件恢复：.import_tag
	dr.find_element_by_css_selector(".import_tag").click()

	#5.浏览：#file_addr
	dr.find_element_by_css_selector("#file_addr").send_keys(BAK_FILE)

	#6.恢复：button.large_but:nth-child(2)
	dr.find_element_by_css_selector("button.large_but:nth-child(2)").click()

	#7.确认：#msg_qd
	dr.switch_to_alert()
	dr.find_element_by_css_selector("#msg_qd").click()
	#8:reload AD url

	
	#raise TimeoutException(message, screen, stacktrace)
	#dr.get(ad_url)
	try:
		dr.get(ad_url)
		WebDriverWait(dr,90).until(EC.title_contains('AD'))
	except TimeoutException as e:
		print 'Catch TimeoutException.',e
		#dr.quit()
	finally:
		#dr=webdriver.Firefox()
		dr.get(ad_url)
		print 'Access AD again in exception.'

	#import pdb; pdb.set_trace()
	dr.switch_to_frame("mainFrame")

	#
	if EC.alert_is_present():
		dr.find_element_by_css_selector("#msg_qd").click()
		print 'Current password is default.'
	dr.switch_to_default_content()

	locator = (By.CSS_SELECTOR, '#id_left > iframe')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
	dr.switch_to_frame("leftFrame")

	#1.系统概况：#left_menu_0 > a > b	
	locator = (By.CSS_SELECTOR, '#left_menu_0 > a > b')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
	element_tmp.click()

	#2.日志查看:#left_menu_0_14 > a:nth-child(1)
	locator = (By.CSS_SELECTOR, '#left_menu_0_14 > a:nth-child(1)')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.visibility_of_element_located(locator))
	dr.find_element_by_css_selector("#left_menu_0_14 > a:nth-child(1)").click()
	#dr.find_element_by_css_selector("#left_menu_0_14 > a:nth-child(1)").click()

	#3.管理日志：#audit_label
	dr.switch_to_default_content()
	dr.switch_to_frame("mainFrame")
	
	locator = (By.CSS_SELECTOR, '#audit_label')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))	
	element_tmp.click()

	#4.第一条日志内容:#table2 > tbody > tr:nth-child(1) > td:nth-child(7)	恢复备份配置	tr.color2:nth-child(2) > td:nth-child(7)
	#结果:#table2 > tbody > tr:nth-child(1) > td:nth-child(6)	完成	tr.color2:nth-child(2) > td:nth-child(6)
	#TODO:1122判断有问题，待调试
	operate_processing=dr.find_element_by_css_selector("tr.color2:nth-child(2) > td:nth-child(7)").text
	operate_result=dr.find_element_by_css_selector("tr.color2:nth-child(2) > td:nth-child(6)").text

	#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-5: ordinal not in range(128)
	#TypeError: descriptor 'decode' requires a 'str' object but received a 'unicode'
	#cmp_result = (operate_processing == '恢复备份配置' and operate_result == '完成')
	#cmp_result = (re.match('恢复备份配置',operate_processing) and re.match('完成',operate_result))
	cmp_result = (operate_processing == u'\u6062\u590d\u5907\u4efd\u914d\u7f6e' and operate_result == u'\u5b8c\u6210')

	if cmp_result:
		print '[success]recovery success'
	else:
		print '[fail]recovery fail.Pls try again.'

	dr.quit()

ad_resume_back(HCI_IP)