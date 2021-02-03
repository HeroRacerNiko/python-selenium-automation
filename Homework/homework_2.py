from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

sign_in_btn = driver.find_element(By.ID, 'nav-link-accountList-nav-line-1')
sign_in_btn.click()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# sign in logo:
# sign_in_logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# sign_in_logo.click()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# email input field:
email_field = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
email_field.send_keys("testing@gmail.com")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# continue button:
# sign_in_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
sign_in_continue = driver.find_element(By.CSS_SELECTOR, "input#continue")
sign_in_continue.click()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# need help link:
# need_help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# need_help_link = driver.find_element(By.CSS_SELECTOR, "span.a-expander-prompt")
# need_help_link.click()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# forgot password link:
# forgot_password_link = driver.find_element(By.CSS_SELECTOR, "a#auth-fpp-link-bottom")
# forgot_password_link.click()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Other Sign in issues link:
# other_issues_link = driver.find_element(By.CSS_SELECTOR, "a#ap-other-signin-issues-link")
# other_issues_link = driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Create your Amazon account button:
# create_account_btn = driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
# create_account_btn.click()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Privacy Notice link:
privacy_notice_link = driver.find_element(By.XPATH, "//a[contains(@href, 'footer_privacy_notice')]")
# privacy-notice_link = driver.find_element(By.XPATH, "//a[contains(@href, 'ap_desktop_footer_privacy_notice)]")
# privacy-notice_link = driver.find_element(By.CSS_SELECTOR, "a[href*='ap_desktop_foo']")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Conditions of Use link:
cou_x = "//a[contains(text(), 'Conditions of Use') and contains(@href, 'cou?')]"
# privacy_notice_link = driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')
cou_link = driver.find_element(By.XPATH, cou_x)


# CSS_SELECTOR Doesnt support .text