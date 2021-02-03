from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
passkey = 'randomSh*t'

driver = webdriver.Chrome(executable_path=r'C:\Users\nurdi\Downloads\REPOS\JE\python-selenium-automation\chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://amazon.com/')

nav_link = driver.find_element(By.ID, "nav-link-accountList")
nav_link.click()
sleep(0.5)

create_btn = driver.find_element(By.ID, 'createAccountSubmit')
create_btn.click()
sleep(0.5)

your_name = driver.find_element(By.ID, 'ap_customer_name')
your_name.click()
your_name.send_keys('Rafael Solano')
sleep(0.5)

your_email = driver.find_element(By.ID, 'ap_email')
your_email.click()
your_email.send_keys('nonexistent.impossible@gmail.com')
sleep(0.5)

password = driver.find_element(By.ID, 'ap_password')
password.click()
password.send_keys(passkey)
sleep(1)

password_check = driver.find_element(By.ID, 'ap_password_check')
password_check.click()
password_check.send_keys(passkey)
sleep(1)
continue_btn = driver.find_element(By.CSS_SELECTOR, "input[id='continue']")
amazon_top_logo = driver.find_element(By.CSS_SELECTOR, "i[role='img']")
condition_of_use = driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")
privacy_notice = driver.find_element(By.CSS_SELECTOR, "a[href*='privacy_notice']")
sign_in_bottom = driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")


driver.quit()
