

class Page:

    def __init__(self, driver):
        self.driver = driver
        # self.base_url = 'https://www.amazon.com'

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(text)

    def open_url(self, url):
        self.driver.get(url)

