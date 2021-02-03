from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

#driver.find_element(By.ID, 'twotabsearchtextbox').send_key('Watches')
search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_field.send_keys("Watches")

search_icon = driver.find_element(By.ID, 'nav-search-submit-button')
search_icon.click()

actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_text = '"Watches"'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()