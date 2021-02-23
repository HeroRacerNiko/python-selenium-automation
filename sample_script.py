from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
# external executable_path note the 'r' for raw text (\U unicode conflict):
# driver = webdriver.Chrome(executable_path=r"C:\Users\nurdi\Downloads\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="C:\\Users\\nurdi\\Downloads\\chromedriver.exe")

# internal executable_path:
# absolute path, note the 'r' as a raw text > https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file
# driver = webdriver.Chrome(executable_path=r'C:\Users\nurdi\Downloads\REPOS\JE\python-selenium-automation\chromedriver.exe')
# or just by name, as long as the file is in the same directory
# driver = webdriver.Chrome('chromedriver.exe')

# if chromedriver is in same directory as python file there is no need to specify the executable_path
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.minimize_window()
driver.maximize_window()
# driver.wait = WebDriverWait(driver, wait)


# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec - hard coded - not preferred
# sleep(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text
print("test completed, and successful")
driver.quit()
