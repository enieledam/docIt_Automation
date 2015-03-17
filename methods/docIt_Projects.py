# Functions related to Projects page
import sys
sys.path.append('/Users/madeleine/docit_selenium')
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import methods.find  as functions

def assert_projects_page(browser):
  browser = browser
  functions.find_css_selector(browser, "ul[ng-model=\'projects\']")
  project_url = browser.current_url
  functions.try_finding_url(browser, project_url)
  if project_url != 'https://www.docit.com/project/list':
    for i in range(20):
      print 'Current url is %s' %project_url
      try:
	assert "https://www.docit.com/project/list" in project_url
	if True:
	  print 'project url == ' + project_url
	  return None
      except NoSuchElementException:
	assert 0, '----- can not find project list url -----'
