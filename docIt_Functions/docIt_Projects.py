# Functions related to Projects page

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import docIt_Functions as functions


#Trying this out. Instantiating browser here. 
#browser = webdriver.Firefox()

def assert_projects_page(browser):
  browser = browser

  functions.try_finding_xpath(browser, "//div[@id='header']")
  project_url = browser.current_url
  assert "https://www.docit.com/project/list" in project_url 
