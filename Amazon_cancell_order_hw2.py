from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/gp/help/customer/display.html ')
driver.implicitly_wait(4)

# help_search_x = "//input[@id='helpsearch']"
help_search = driver.find_element(By.ID, "helpsearch")
help_search.click()
help_search.send_keys("Cancel order")
help_search.send_keys(Keys.ENTER)


hcs_field = driver.find_element(By.CSS_SELECTOR, ".help-content")


actual_text = driver.find_element(By.CSS_SELECTOR, ".help-content").text
expected_text = 'Cancel Items or Orders'
assert expected_text in actual_text, f'Expected {expected_text}, but got {actual_text}'
# assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()
