# -*- coding:utf8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, InvalidElementStateException

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
HCI_USER_NAME = 'admin'
HCI_USER_PWD = 'sangfor123'
VAD_ID = 7458706160170
BAK_FILE = r"\\200.200.164.111\vtt_share\12-NFV\NFV_HCI5.3\vAD\adconf_1_2017-11-07.bcf"


class Ad(object):
    def __init__(self, hci_ip, hci_user_name, hci_user_pwd, vad_id):
        self.hci_ip = hci_ip
        self.hci_user_name = hci_user_name
        self.hci_user_pwd = hci_user_pwd
        self.vad_id = vad_id
        self.hci_url = 'https://%s/login' % self.hci_ip
        self.vad_url = 'https://%s/?m=/mod-vnet/dev/web/index&n-hfs&id=%s' % (
            self.hci_ip, self.vad_id)
        self.dr = webdriver.Firefox()

    def login_hci(self):
        try:
            self.dr.find_element_by_css_selector(
                "#user_name").send_keys(self.hci_user_name)
            self.dr.find_element_by_css_selector(
                "#password").send_keys(self.hci_user_pwd)
            self.dr.find_element_by_css_selector("#login").click()
            if expected_conditions.title_contains("SANGFOR"):
                print 'HCI login success.'
            elif expected_conditions.title_contains("Login"):
                print 'HCI login fail.Try again.'
            else:
                print 'Something unknown.Try again.'
        except InvalidElementStateException as e:
            print 'Catch InvalidElementStateException : ', e
            print 'Quit driver.Pls try again.'

    def do_not_change_password(self):
        self.dr.switch_to.frame("mainFrame")
        if expected_conditions.alert_is_present():
            self.dr.find_element_by_css_selector("#msg_qd").click()
            print 'Current password is default.'
        self.dr.switch_to.default_content()

    def switch_to_left(self):
        locator = (By.CSS_SELECTOR, '#id_left > iframe')
        WebDriverWait(self.dr, 45, 0.5).until(
            expected_conditions.presence_of_element_located(locator))
        self.dr.switch_to.frame("leftFrame")

    def recover_backup_from_file(self):
        # 1.系统配置
        locator = (By.CSS_SELECTOR, '#left_menu_8 > a > b')
        element_tmp = WebDriverWait(self.dr, 45, 0.5).until(
            expected_conditions.presence_of_element_located(locator))
        element_tmp.click()
        self.dr.find_element_by_css_selector("#left_menu_8 > a > b").click()

        # 2.设备管理
        locator = (By.CSS_SELECTOR, '#left_menu_8_0 > a')
        element_tmp = WebDriverWait(self.dr, 45, 0.5).until(
            expected_conditions.presence_of_element_located(locator))
        element_tmp.click()

        self.dr.switch_to.default_content()
        self.dr.switch_to.frame("mainFrame")

        # 3.配置备份与恢复
        locator = (By.CSS_SELECTOR, 'ul.tag_gray:nth-child(3) > a:nth-child(1)')
        element_tmp = WebDriverWait(self.dr, 45, 0.5).until(
            expected_conditions.presence_of_element_located(locator))
        element_tmp.click()

        # 4.从文件恢复
        self.dr.find_element_by_css_selector(".import_tag").click()

        # 5.浏览
        self.dr.find_element_by_css_selector("#file_addr").send_keys(BAK_FILE)

        # 6.恢复
        self.dr.find_element_by_css_selector(
            "button.large_but:nth-child(2)").click()

        # 7.确认
        if expected_conditions.alert_is_present():
            self.dr.find_element_by_css_selector("#msg_qd").click()

    def wait_recover_finish(self):
        try:
            self.dr.get(self.vad_url)
            WebDriverWait(self.dr, 90).until(
                expected_conditions.title_contains('AD'))
        except TimeoutException as e:
            print 'Catch TimeoutException.', e
        finally:
            self.dr.get(self.vad_url)
            if expected_conditions.title_contains("AD"):
                print 'Access AD success.'
            else:
                print 'Access AD fail.Pls try again.'
                self.dr.quit()

    def check_recover_result(self):
        # 0.切换到leftFrame
        locator = (By.CSS_SELECTOR, '#id_left > iframe')
        WebDriverWait(self.dr, 45, 0.5).until(
            expected_conditions.presence_of_element_located(locator))
        self.dr.switch_to.frame("leftFrame")
        # 1.系统概况
        locator = (By.CSS_SELECTOR, '#left_menu_0 > a > b')
        element_tmp = WebDriverWait(self.dr, 45, 0.5).until(
            expected_conditions.presence_of_element_located(locator))
        element_tmp.click()

        # 2.日志查看
        locator = (By.CSS_SELECTOR, '#left_menu_0_14 > a:nth-child(1)')
        WebDriverWait(self.dr, 45, 0.5).until(
            expected_conditions.visibility_of_element_located(locator))
        self.dr.find_element_by_css_selector(
            "#left_menu_0_14 > a:nth-child(1)").click()

        # 3.管理日志
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame("mainFrame")

        locator = (By.CSS_SELECTOR, '#audit_label')
        element_tmp = WebDriverWait(self.dr, 45, 0.5).until(
            expected_conditions.presence_of_element_located(locator))
        element_tmp.click()

        # 4.检查第二条日志内容
        operate_processing = self.dr.find_element_by_css_selector(
            "tr.color2:nth-child(2) > td:nth-child(7)").text
        operate_result = self.dr.find_element_by_css_selector(
            "tr.color2:nth-child(2) > td:nth-child(6)").text

        cmp_result = (operate_processing ==
                      u'\u6062\u590d\u5907\u4efd\u914d\u7f6e' and operate_result == u'\u5b8c\u6210')

        if cmp_result:
            print '[success]recovery success'
        else:
            print '[fail]recovery fail.Pls try again.'

    def recovery_ad_back(self):

        # 全局隐性等待，90秒超时。
        self.dr.implicitly_wait(90)

        self.dr.get(self.hci_url)

        self.login_hci()

        self.dr.get(self.vad_url)

        self.do_not_change_password()

        self.switch_to_left()

        self.recover_backup_from_file()

        self.wait_recover_finish()

        self.do_not_change_password()

        self.check_recover_result()

        self.dr.quit()


vad_test = Ad(HCI_IP, HCI_USER_NAME, HCI_USER_PWD, VAD_ID)

vad_test.recovery_ad_back()
