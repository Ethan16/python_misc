#!C:\python27
#-*-coding:utf8-*-

"""
客户端用ab工具访问，服务端"系统概况>节点状态>节点状态"，新建连接数接近即可
"""

from selenium import webdriver
#from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#import wait
import time

HCI_IP='200.201.136.116'
HCI_USER_NAME='admin'
HCI_USER_PWD='sangfor123'
#AD_VMID=3590808821638
#AD_VMID=445801565642
AD_VMID=430801565642
AD_USER_NAME='admin'
AD_USER_PWD='admin'

#TODO 方法至少用2个参数，hciip和advmid，先用1个参数调试。
def is_ad_balance(hciip):
	dr=webdriver.Firefox()
	#dr=webdriver.Chrome()
	hci_url='https://%s/login'%hciip
	ad_url='https://%s/?m=/mod-vnet/dev/web/index&n-hfs&id=%s'%(hciip,AD_VMID)

	#全局隐性等待，45秒超时。
	dr.implicitly_wait(45)
	dr.get(hci_url)
	#TODO:登录有时候会失败，需要做重试处理。
	dr.find_element_by_css_selector("#user_name").send_keys(HCI_USER_NAME)	
	dr.find_element_by_css_selector("#password").send_keys(HCI_USER_PWD)	
	dr.find_element_by_css_selector("#login").click()
		
	#try:
	dr.get(ad_url)
		
	dr.switch_to_frame("mainFrame")
	dr.switch_to_alert()
	dr.find_element_by_css_selector("#msg_qd").click()
	#dr.switch_to_alert().accept()

	dr.switch_to_default_content()

	locator = (By.CSS_SELECTOR, '#id_left > iframe')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
	dr.switch_to_frame("leftFrame")

	#1.系统概况：#left_menu_0 > a > b		
	locator = (By.CSS_SELECTOR, '#left_menu_0 > a > b')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
	element_tmp.click()

	#2.节点状态：#left_menu_0_9 > a    #left_menu_0_9 > a:nth-child(1)
	#try:
	locator = (By.CSS_SELECTOR, '#left_menu_0_9 > a:nth-child(1)')
	WebDriverWait(dr,45,0.5).until(EC.visibility_of_element_located(locator))
	#element_tmp.click()
	dr.find_element_by_css_selector("#left_menu_0_9 > a:nth-child(1)").click()
	#import pdb;pdb.set_trace()
	
	#except ElementNotInteractableException:
	#	print u'左侧“节点状态”按钮点击无响应，运行失败！浏览器退出，请重试！'
	#	dr.quit()
	#http://blog.csdn.net/huilan_same/article/details/52338073	

	#3.节点状态：#title_tag > ul:nth-child(2) > a
	dr.switch_to_default_content()
	dr.switch_to_frame("mainFrame")

	locator = (By.CSS_SELECTOR, '#title_tag > ul:nth-child(2) > a')
	element_tmp=WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))	
	element_tmp.click()

	#4.并发连接数1：#node_state_list > tr.color1 > td:nth-child(2)
	#TODO 2个服务器，下述代码够用。多节点，可以用字典存储名字和并发数
	node1_established=int(dr.find_element_by_css_selector("#node_state_list > tr.color1 > td:nth-child(2)").text)
	node1_name=dr.find_element_by_css_selector("#node_state_list > tr.color1 > td:nth-child(1)").text

	#5.并发连接数2：#node_state_list > tr.color2 > td:nth-child(2)
	##node_state_list > tr.color2 > td:nth-child(1)
	node2_established=int(dr.find_element_by_css_selector("#node_state_list > tr.color2 > td:nth-child(2)").text)
	node2_name=dr.find_element_by_css_selector("#node_state_list > tr.color2 > td:nth-child(1)").text

	if (node1_established == 0) or (node2_established == 0):
		print u'至少1个节点的并发连接数为0，负载均衡不成功，请检查配置是否正确。'
		print u'节点: %s ,并发连接数: %d 。'%(node1_name,node1_established)
		print u'节点: %s ,并发连接数: %d 。'%(node2_name,node2_established)
		dr.quit()
	else:
		established_decrease=abs(node1_established-node2_established)
		if established_decrease <= 3:
			print u'[success]负载均衡测试成功。节点: %s ,并发连接数: %d 。节点: %s ,并发连接数: %d 。'%(node1_name,	node1_established,node2_name,node2_established)	
		else:
			print u'[Verify]负载不够均衡。节点: %s ,并发连接数: %d 。节点: %s ,并发连接数: %d 。'%(node1_name,	node1_established,node2_name,node2_established)	
		dr.quit()

is_ad_balance(HCI_IP)
