from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_LINK = (By.ID, 'nav-orders')
    CART_LINK = (By.ID, 'nav-cart')

    def open_main_page(self):
        self.open_url('https://www.amazon.com')

    def input_amazon_search(self, query):
        self.input_text(query, *self.SEARCH_FIELD)

    def click_search_amazon(self):
        self.click(*self.SEARCH_ICON)

    def orders_click(self):
        self.click(*self.ORDERS_LINK)

    def cart_click(self):
        self.click(*self.CART_LINK)

    def press_key(self):
        search_field = self.driver.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(Keys.ENTER)

