from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path=r"C:\Users\nurdi\Downloads\REPOS\JE\python-selenium-automation\chromedriver.exe")
# driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 10)


# driver.get('https://www.amazon.com')
# driver.find_element_by_id("nav-signin-tooltip").click()


driver.get('https://www.google.com')
driver.find_element(By.XPATH, "//input[@name='q']").send_keys('Hello world')
search_el = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='btnK'] [@value='Google Search'] [@class='gNO89b']")))
search_el.click()
# driver.find_element(By.XPATH, "//input[@name='btnK'] [@value='Google Search'] [@class='gNO89b']").click()
driver.quit()
