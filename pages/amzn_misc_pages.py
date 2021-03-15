from pages.base_page import Page
from selenium.webdriver.common.by import By


class AmazonMiscPages(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, ".a-box-inner h1")
    SIGN_IN_EMAIL = (By.ID, 'ap_email')
    EMPTY_CART_TEXT_LOC = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")
    CART_COUNTER_LOC = (By.ID, 'nav-cart-count')
    CART_CONTENT = (By.CSS_SELECTOR, "div[data-asin]")

    def verify_sign_in_opened(self):
        # print(self.driver.find_element(*self.SIGN_IN_TEXT).text)
        assert "Sign-In" in self.driver.find_element(*self.SIGN_IN_TEXT).text
        self.driver.find_element(*self.SIGN_IN_EMAIL)

    def verify_cart_is_empty(self):
        empty_cart_text_element = self.driver.find_element(*self.EMPTY_CART_TEXT_LOC)
        expected_text = "Your Amazon Cart is empty"
        actual_text = empty_cart_text_element.text

        cart_counter_el = self.driver.find_element(*self.CART_COUNTER_LOC)
        print(actual_text)
        print(cart_counter_el.text)
        assert expected_text in actual_text, f'Expected: {expected_text}, got {actual_text}'
        assert int(cart_counter_el.text) == 0

    def verify_cart_content(self, quantity):
        cart = self.driver.find_element(By.ID, 'nav-cart-count-container')
        cart.click()
        if int(self.driver.find_element(*self.CART_COUNTER_LOC).text) == 0:
            # if len(self.driver.find_elements(*CART_CONTENT)) == 0:
            print(f'Your cart has {len(self.driver.find_elements(*self.CART_CONTENT))} items')
            assert "Your Amazon Cart is empty" == self.driver.find_element(*self.EMPTY_CART_TEXT_LOC).text, \
                f'Expected: "Your Amazon Cart is empty", ' \
                f'but got: {self.driver.find_element(*self.EMPTY_CART_TEXT_LOC).text}'
        else:
            print(f'Your cart has {self.driver.find_element(*self.CART_COUNTER_LOC).text} item(s)')
            assert int(self.driver.find_element(*self.CART_COUNTER_LOC).text) == int(quantity), f'cart items doesn\'t match test quntity\
                Cart has {int(self.driver.find_element(*self.CART_COUNTER_LOC).text)} items, \
                expected: {int(quantity)}'

    def verify_cart_product_quantity_matches_single_order(self, quantity):
        current_counter = int(self.driver.find_element(*self.CART_COUNTER_LOC).text)
        assert current_counter == int(quantity), f'Cart has {current_counter} items, quantity of product was added was: {quantity}'
