# Functions to find elements by css, xpath, etc on docit.com

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('/Users/madeleine/docit_selenium')

def try_finding_xpath(browser,locator):
  browser = browser
  locator = locator
  for i in range(10):
    try:
      browser.find_element_by_xpath(locator)
      print '+++++ Found %s +++++' %locator
      return None 
    except NoSuchElementException:
      assert 0, "can't find xpath %s" %locator
      browser.close()
  
def find_css_selector(browser, locator):
  browser = browser
  locator = locator
  try:
    element = WebDriverWait(browser, 10).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    )
    print '+++++ Found %s +++++' %locator
  except NoSuchElementException:
    browser.quit()


def try_finding_url(browser, url):
    browser = browser
    url = url
    browser.implicitly_wait(10)
    for i in range(30):
      browser_url = browser.current_url
      if browser_url != url:
	print 'browser url does not match expected. trying again'
    
