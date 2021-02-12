from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\nurdi\Downloads\chromedriver_win32\chromedriver.exe")

driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
driver.implicitly_wait(4)

driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')]")












