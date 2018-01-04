#!C:\python27
#-*-coding:utf8-*-

from selenium import webdriver
import unittest

class BaiduTest(unittest.TestCase):
	def setUp(self):
		self.browser=webdriver.Firefox()
		self.addCleanup(self.browser.quit)

	def testPageTitle(self):
		self.browser.get("http://www.baidu.com")
		self.assertIn(u'百度',self.browser.title)

if __name__ == '__main__':
	unittest.main(verbosity=2)