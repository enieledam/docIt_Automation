# Functions related to Accounts, e.g. Log In

import sys
sys.path.append('/Users/madeleine/docit_selenium')
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import methods.find as functions

# Test account email address and password
email = 'automate.docit@gmail.com'
password = 'Bulgaria10$'

def try_finding_link(browser,locator):
  browser = browser 
  locator = locator
  try:
    browser.find_element_by_link_text(locator)
  except NoSuchElementException:
    assert 0, "----- can't find %s link -----" %locator
    browser.close()

#def try_finding_xpath(browser,locator):
#  browser = browser
#  locator = locator
#  try:
#    browser.find_element_by_xpath(locator)
#    print '+++++ Found %s +++++' %locator
#  except NoSuchElementException:
#    assert 0, "----- can't find xpath %s -----" %locator
#    browser.close()

def navigate_to_login(browser):
  browser = browser
  try_finding_link(browser, 'LOGIN')
  login_menu = browser.find_element_by_link_text('LOGIN')
  # Click on Login Menu
  login_menu.click()

  # Assert login page is shown
  try:
    browser.find_element_by_xpath("//h4[@class='form-heading'][contains(text(), 'Login')]")
    print "+++++ Found login header +++++"
  except NoSuchElementException:
    #TODO Add a try
    assert 0, "can't find Login header"
    browser.close()

def enter_email_address(browser, username=email):
  browser = browser
  username = username
  try:
    browser.find_element_by_css_selector("input[name='UserName']")
    print '+++++ Found email field +++++'
  except NoSuchElementException:
    assert 0, "Can't find email field to input email address"
    browser.close()

  email_field = browser.find_element_by_css_selector("input[name='UserName']")
  email_field.send_keys(username)

def enter_password(browser, pw=password):
  browser = browser
  pw = pw

  try:
    browser.find_element_by_css_selector("input[name='inputPassword']")
    print '+++++ Found password field +++++'
  except NoSuchElementException:
    assert 0, "Can't find password field"
    browser.close()

  password_field = browser.find_element_by_css_selector("input[name='inputPassword']")
  password_field.send_keys(pw)

def sign_in(browser):
  functions.try_finding_xpath(browser, "//button[contains(text(), 'Sign In')]")
  sign_in_button = browser.find_element_by_xpath("//button[contains(text(), 'Sign In')]")
  sign_in_button.click()
