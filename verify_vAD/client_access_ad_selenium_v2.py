# -*- coding:utf8 -*-

from selenium import webdriver


"""
作者：zyc
日期：2018-1-4
功能：PC本地拉起Firefox，访问AD。使用Selenium来判断标题
"""

AD_WAN_URL = "http://80.80.80.10/"


def is_ad_load_balance(ad_wan_url):
    dr = webdriver.Firefox()
    dr.get(ad_wan_url)

    title_once = dr.title
    print title_once

    dr.delete_all_cookies()

    dr.refresh()

    title_twice = dr.title
    print title_twice

    if title_once != title_twice:
        print '[success]AD load balance.'
    else:
        print '[fail]AD load balance fail.Pls check network configuration.'

    dr.quit()


is_ad_load_balance(AD_WAN_URL)
