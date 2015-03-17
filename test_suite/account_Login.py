# Test logging into user account on docit.com

import sys
sys.path.append('/Users/madeleine/docIt_selenium/')
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import methods.accounts as accounts
import methods.docIt_Projects as projects


# Create a new instance of Firefox driver
driver = webdriver.Firefox()

# Go to Doc It homepage
driver.get('http://www.docit.com')

# Navigate to Login page
accounts.navigate_to_login(driver)

# Enter in valid login credentials
accounts.enter_email_address(driver)
accounts.enter_password(driver)

# Hit Sign In
accounts.sign_in(driver)

#try:
#  wait = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('sidebar'))
#  print 'found sidebar!!!!'
#except NoSuchElementException:
#  assert 0, 'can not find sidebar'
#  browser.close()
# Sleep a few seconds for page to load
#driver.implicitly_wait(10)
#wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID,'sidebar-inner'))


# Assert homepage/landing page (Projects page)
projects.assert_projects_page(driver)

# Test is Done
print 'Test is Done!'

# Close the browser
driver.quit()

