from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import accounts as accounts
import docIt_Projects as projects
from selenium.webdriver.support.ui import WebDriverWait


#test_username = 'automate.docit@gmail.com'
#test_password = 'Bulgaria10$' 

# Create a new instance of Firefox driver
driver = webdriver.Firefox()

# Go to Doc It homepage
driver.get('http://www.docit.com')

# Find Menu and click on it.
#login_menu = driver.find_element_by_link_text('LOGIN')
#login_menu.click()

# Navigate to Login page
accounts.navigate_to_login(driver)

# Enter in valid login credentials
accounts.enter_email_address(driver)
accounts.enter_password(driver)

# Hit Sign In
accounts.sign_in(driver)

# Sleep a few seconds for page to load


# Assert homepage/landing page (Projects page)
projects.assert_projects_page(driver)

print accounts.email
print accounts.password


