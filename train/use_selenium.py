from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver=webdriver.Remote(
    command_executor='http://200.200.103.5:32773/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME
)

driver.get("https://www.baidu.com")

print driver.title

#import pdb;pdb.set_trace()

driver.close()