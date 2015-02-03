# General functions for DocIt

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def try_finding_xpath(browser,locator):
  browser = browser
  locator = locator
  for i in range(60):
    try:
      browser.find_element_by_xpath(locator)
      print 'Found %s' %locator
    except NoSuchElementException:
      assert 0, "can't find xpath %s" %locator
      browser.close()
  else: browser.fail("time out")
