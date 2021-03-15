from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    FIRST_ELEMENT_PREFERRED = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    QTY_DROPDOWN = (By.XPATH, "//span[@class='a-button a-button-dropdown a-button-small']")
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SIDE_PANE = (By.ID, 'attach-accessory-pane')
    SIDE_PANE_CART = (By.XPATH, "//span[@id='attach-sidesheet-view-cart-button'] //input[@class='a-button-input']")
    SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
    SIZE_DROPDOWN = (By.ID, 'dropdown_selected_size_name')
    DEFAULT_SIZE = (By.ID, 'size_name_0')

    def verify_text(self, query):
        actual_text = self.driver.find_element(*self.RESULT).text
        expected_text = f'{query}'
        assert expected_text == actual_text, f'Expected {query}, but got {actual_text}'

    def verify_url_contains_query(self, query):
        print(f'Current URL: "{self.driver.current_url}" DOES contain "{query}"')
        assert query in self.driver.current_url, f'Watches not in {self.driver.current_url}'

    def select_first_result(self):
        result_list = self.driver.find_elements(*self.FIRST_ELEMENT_PREFERRED)
        result_list[0].click()

    def add_to_cart(self, quantity):
        if len(self.driver.find_elements(By.ID, "quantity")):
            self.driver.find_element(*self.QTY_DROPDOWN).click()
            self.driver.find_element(By.XPATH, "//li[@class='a-dropdown-item']/a[@data-value='{\"stringVal\":\"" + quantity + "\"}']").click()
            # self.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()
            self.driver.find_element(*self.ADD_TO_CART_BTN).click()
            if self.driver.wait.until(EC.visibility_of_element_located(*self.SIDE_PANE)):
                print("Side panel kicked in")
                self.driver.find_element(*self.SIDE_PANE_CART).click()
            else:
                self.driver.find_element(*self.ADD_TO_CART_BTN).click()
        else:
            self.driver.find_element(*self.ADD_TO_CART_BTN).click()
            if len(self.driver.find_elements(*self.SIZE_TOOLTIP)) == 1:
                self.driver.find_element(*self.SIZE_DROPDOWN).click()
                self.driver.find_element(*self.DEFAULT_SIZE).click()
                self.driver.find_element(*self.QTY_DROPDOWN).click()
                self.driver.find_element(By.XPATH, "//li[@class='a-dropdown-item']/a[@data-value='{\"stringVal\":\"" + quantity + "\"}']").click()
                self.driver.find_element(*self.ADD_TO_CART_BTN).click()
            else:
                self.driver.find_element(*self.ADD_TO_CART_BTN).click()
