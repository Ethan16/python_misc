#!C:\python27
#-*-coding:utf8-*-

from selenium import webdriver
#from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.select import Select
#import wait
# import time

"""
需求：HCI上已经打开vAD的配置页面的情况下，对vAD进行一个基本配置，然后验证vAD的业务
分析：1.打开vAD的配置页面，填写配置信息，可以使用Selenium实现。
	2.重点是验证业务生效。需要熟悉vAD的业务。
NFV模块测试人：石龙奇，用例：464821
1.1台访问主机是否可以实现负载均衡？slq：轮询的方式，可以。
2.是否可以通过导入配置实现一键配置？nyz：配置(网络配置、负载均衡配置)都在，通过文件恢复即可。
最终需求：
1. 实现vADer导入配置，用selenium。
2. 在client端验证vAD有负载均衡功能。客户端连续2次访问到的是不同的内容即可。
-----------------------------------------------------------
作者：zyc
日期：2017-11-7
功能：vAD导入配置恢复备份
"""

HCI_IP = '200.201.188.106'
# HCI_IP='200.201.136.116'
HCI_USER_NAME = 'admin'
HCI_USER_PWD = 'sangfor123'
# AD_VMID=3590808821638
# AD_VMID=445801565642
AD_VMID = 7458706160170
AD_USER_NAME = 'admin'
AD_USER_PWD = 'admin'
BAK_FILE = r"\\200.200.164.111\vtt_share\12-NFV\NFV_HCI5.3\vAD\adconf_1_2017-11-07.bcf"


class Ad(object):

    def __init__(self, hciip, advmid):
        self.hciip = hciip
        self.advmid = advmid
        # self.username=username
        # self.pwd=pwd
        # self.backfile=backfile

    # 登录进入AD控制台
    # https://200.201.188.106/?m=/mod-vnet/dev/web/index&n-hfs&id=3590808821638
    def ad_resume_back(self):
        dr = webdriver.Firefox()
        # dr=webdriver.Chrome()
        hci_url = 'https://%s/login' % self.hciip
        ad_url = 'https://%s/?m=/mod-vnet/dev/web/index&n-hfs&id=%s' % (
            self.hciip, self.advmid)

        print u'HCI login page is : ', hci_url
        # 全局隐性等待，90秒超时。
        dr.implicitly_wait(90)
        dr.get(hci_url)

        dr.find_element_by_css_selector("#user_name").send_keys(HCI_USER_NAME)
        dr.find_element_by_css_selector("#password").send_keys(HCI_USER_PWD)
        dr.find_element_by_css_selector("#login").click()
        # 如果没有登录成功，重试一遍
        # longin_hci_js=javascript:seajs.require('jquery')('#user_name').val('admin').next().val('sangfor123').next().next().next().click();
        #import pdb; pdb.set_trace()
        # if not re.match('SANGFOr',dr.title):
        if dr.title == u'Login':
            dr.find_element_by_css_selector(
                "#user_name").send_keys(HCI_USER_NAME)
            dr.find_element_by_css_selector(
                "#password").send_keys(HCI_USER_PWD)
            dr.find_element_by_css_selector("#login").click()

        # https://200.201.188.106/?m=/mod-vnet/dev/web/index&n-hfs&id=3590808821638
        dr.get(ad_url)
        print 'AD console page is : ', ad_url

        # WebDriverWait(dr,45,0.5).until(EC.presence_of_element_located(locator))
        dr.switch_to_frame("mainFrame")

        if EC.alert_is_present():
            dr.find_element_by_css_selector("#msg_qd").click()
            print 'Current password is default.'
        dr.switch_to_default_content()

        # selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: //*[@id="left_menu_8"]/a/b
        # NoSuchFrameException: Message: leftFrame

        locator = (By.CSS_SELECTOR, '#id_left > iframe')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        dr.switch_to_frame("leftFrame")

        # 1.系统配置：#left_menu_8 > a > b
        # dr.find_element_by_css_selector("#left_menu_8 > a > b")

        locator = (By.CSS_SELECTOR, '#left_menu_8 > a > b')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        element_tmp.click()
        # time.sleep(5)

        # 2.设备管理：#left_menu_8_0 > a
        locator = (By.CSS_SELECTOR, '#left_menu_8_0 > a')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        element_tmp.click()
        # http://blog.csdn.net/huilan_same/article/details/52338073
        dr.find_element_by_css_selector("#left_menu_8_0 > a").click()

        dr.switch_to_default_content()
        dr.switch_to_frame("mainFrame")
        # 3.配置备份与恢复：ul.tag_gray:nth-child(3) > a:nth-child(1)
        locator = (By.CSS_SELECTOR, 'ul.tag_gray:nth-child(3) > a:nth-child(1)')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        element_tmp.click()

        # 4.从文件恢复：.import_tag
        dr.find_element_by_css_selector(".import_tag").click()

        # 5.浏览：#file_addr
        dr.find_element_by_css_selector("#file_addr").send_keys(BAK_FILE)

        # 6.恢复：button.large_but:nth-child(2)
        dr.find_element_by_css_selector(
            "button.large_but:nth-child(2)").click()

        # 7.确认：#msg_qd
        dr.switch_to_alert()
        dr.find_element_by_css_selector("#msg_qd").click()

        #raise TimeoutException(message, screen, stacktrace)
        # dr.get(ad_url)
        try:
            dr.get(ad_url)
            WebDriverWait(dr, 90).until(EC.title_contains('AD'))
        except TimeoutException as e:
            print 'Catch TimeoutException.', e
            # dr.quit()
        finally:
            # dr=webdriver.Firefox()
            dr.get(ad_url)
            if EC.title_contains("AD"):
                print 'Access AD success.'
            else:
                print 'Access AD fail.Pls try again.'
                dr.quit()

        #
        dr.switch_to_frame("mainFrame")

        #
        if EC.alert_is_present():
            dr.find_element_by_css_selector("#msg_qd").click()
            # print 'Current password is default.'
        dr.switch_to_default_content()

        locator = (By.CSS_SELECTOR, '#id_left > iframe')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        dr.switch_to_frame("leftFrame")

        # 1.系统概况：#left_menu_0 > a > b
        locator = (By.CSS_SELECTOR, '#left_menu_0 > a > b')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        element_tmp.click()

        # 2.日志查看:#left_menu_0_14 > a:nth-child(1)
        locator = (By.CSS_SELECTOR, '#left_menu_0_14 > a:nth-child(1)')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.visibility_of_element_located(locator))
        dr.find_element_by_css_selector(
            "#left_menu_0_14 > a:nth-child(1)").click()
        # dr.find_element_by_css_selector("#left_menu_0_14 >
        # a:nth-child(1)").click()

        # 3.管理日志：#audit_label
        dr.switch_to_default_content()
        dr.switch_to_frame("mainFrame")

        locator = (By.CSS_SELECTOR, '#audit_label')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        element_tmp.click()

        # 4.第一条日志内容:#table2 > tbody > tr:nth-child(1) > td:nth-child(7)	恢复备份配置	tr.color2:nth-child(2) > td:nth-child(7)
        # 结果:#table2 > tbody > tr:nth-child(1) > td:nth-child(6)	完成	tr.color2:nth-child(2) > td:nth-child(6)
        # TODO:1122判断有问题，待调试 ->1123:done
        operate_processing = dr.find_element_by_css_selector(
            "tr.color2:nth-child(2) > td:nth-child(7)").text
        operate_result = dr.find_element_by_css_selector(
            "tr.color2:nth-child(2) > td:nth-child(6)").text

        # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-5: ordinal not in range(128)
        # TypeError: descriptor 'decode' requires a 'str' object but received a 'unicode'
        #cmp_result = (operate_processing == '恢复备份配置' and operate_result == '完成')
        #cmp_result = (re.match('恢复备份配置',operate_processing) and re.match('完成',operate_result))
        cmp_result = (operate_processing ==
                      u'\u6062\u590d\u5907\u4efd\u914d\u7f6e' and operate_result == u'\u5b8c\u6210')

        if cmp_result:
            print '[success]recovery success'
        else:
            print '[fail]recovery fail.Pls try again.'

        dr.quit()

    # 使用客户端的方法来判断，此方法废弃掉。
    def is_ad_balance(self):
        dr = webdriver.Firefox()
        # dr=webdriver.Chrome()
        hci_url = 'https://%s/login' % self.hciip
        ad_url = 'https://%s/?m=/mod-vnet/dev/web/index&n-hfs&id=%s' % (
            self.hciip, self.advmid)

        # 全局隐性等待，45秒超时。
        dr.implicitly_wait(45)
        dr.get(hci_url)
        dr.find_element_by_css_selector("#user_name").send_keys(HCI_USER_NAME)
        dr.find_element_by_css_selector("#password").send_keys(HCI_USER_PWD)
        dr.find_element_by_css_selector("#login").click()
        if not WebDriverWait(dr, 10).until(EC.title_contains('SANGFOR')):
            dr.find_element_by_css_selector(
                "#user_name").send_keys(HCI_USER_NAME)
            dr.find_element_by_css_selector(
                "#password").send_keys(HCI_USER_PWD)
            dr.find_element_by_css_selector("#login").click()

        # try:
        dr.get(ad_url)

        dr.switch_to_frame("mainFrame")
        #
        if EC.alert_is_present():
            # dr.switch_to_alert()
            dr.find_element_by_css_selector("#msg_qd").click()
            print 'Current password is default.'
        dr.switch_to_default_content()
        # dr.switch_to_alert().accept()

        locator = (By.CSS_SELECTOR, '#id_left > iframe')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        dr.switch_to_frame("leftFrame")

        # 1.系统概况：#left_menu_0 > a > b
        locator = (By.CSS_SELECTOR, '#left_menu_0 > a > b')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        element_tmp.click()

        # 2.节点状态：#left_menu_0_9 > a    #left_menu_0_9 > a:nth-child(1)
        # try:
        locator = (By.CSS_SELECTOR, '#left_menu_0_9 > a:nth-child(1)')
        WebDriverWait(dr, 45, 0.5).until(
            EC.visibility_of_element_located(locator))
        # element_tmp.click()
        dr.find_element_by_css_selector(
            "#left_menu_0_9 > a:nth-child(1)").click()
        #

        # except ElementNotInteractableException:
        #	print u'左侧“节点状态”按钮点击无响应，运行失败！浏览器退出，请重试！'
        #	dr.quit()
        # http://blog.csdn.net/huilan_same/article/details/52338073

        # 3.节点状态：#title_tag > ul:nth-child(2) > a
        dr.switch_to_default_content()
        dr.switch_to_frame("mainFrame")

        locator = (By.CSS_SELECTOR, '#title_tag > ul:nth-child(2) > a')
        element_tmp = WebDriverWait(dr, 45, 0.5).until(
            EC.presence_of_element_located(locator))
        element_tmp.click()

        # 4.#showColumn__node_name -> #filterList__total_conn_num
        import pdb
        pdb.set_trace()
        dr.find_element_by_css_selector('#showColumn__node_name').click()
        dr.find_element_by_css_selector('#filterList__total_conn_num').click()

        # 5.并发连接数1：#node_state_list > tr.color1 > td:nth-child(2)	.color1 > td:nth-child(3)
        # node1_established_start=int(dr.find_element_by_css_selector("#node_state_list
        # > tr.color1 > td:nth-child(2)").text)
        node1_established_start = int(
            dr.find_element_by_css_selector(".color1 > td:nth-child(3)").text)
        # node1_name=dr.find_element_by_css_selector("#node_state_list >
        # tr.color1 > td:nth-child(1)").text

        # 6.并发连接数2：#node_state_list > tr.color2 > td:nth-child(2)	.color2 > td:nth-child(3)
        # node_state_list > tr.color2 > td:nth-child(1)
        # node2_established_start=int(dr.find_element_by_css_selector("#node_state_list
        # > tr.color2 > td:nth-child(2)").text)
        node2_established_start = int(
            dr.find_element_by_css_selector(".color2 > td:nth-child(3)").text)
        # node2_name=dr.find_element_by_css_selector("#node_state_list >
        # tr.color2 > td:nth-child(1)").text

        # TODO:5分钟后再取一次值，此期间，客户端在持续访问。需要考虑客户端与AD的配合问题->1123:让客户端持续不断地访问AD
        # time.sleep(300)
        WebDriverWait(dr, 30)

        #import pdb; pdb.set_trace()
        node1_established_end = int(dr.find_element_by_css_selector(
            "#node_state_list > tr.color1 > td:nth-child(2)").text)
        node2_established_end = int(dr.find_element_by_css_selector(
            "#node_state_list > tr.color2 > td:nth-child(2)").text)

        node1_established = abs(node1_established_end-node1_established_start)
        node2_established = abs(node2_established_end-node2_established_start)

        if (node1_established == 0) or (node2_established == 0):
            print '[fail]One node link is 0.Pls check configuration!'
            # print 'node: %s ,link num: %d 。'%(node1_name,node1_established)
            # print 'node: %s ,link num: %d 。'%(node2_name,node2_established)
            dr.quit()
        else:
            established_decrease = abs(node1_established-node2_established)
            if established_decrease <= 2:
                # node: %s ,link num: %d .node: %s ,link num: %d
                # 。'%(node1_name,node1_established,node2_name,node2_established)
                print '[success]Load balance test success.'
            else:
                # node: %s ,link num: %d .node: %s ,link num: %d
                # 。'%(node1_name,node1_established,node2_name,node2_established)
                print '[fail]Load balance test fail.'
            dr.quit()

ad_test = Ad(HCI_IP, AD_VMID)
ad_test.ad_resume_back()
# ad_test.is_ad_balance()
