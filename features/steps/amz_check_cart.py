from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

# -------------------------------------------------------------------------
# 'Open Amazon page' step declared in "amazon_search.py"
# 'Input dress into Amazon search field' borrowed from "amazon_search.py"
# -------------------------------------------------------------------------
FIRST_ELEMENT = (By.CSS_SELECTOR, "div[data-index='3']")
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
CART_DIV = (By.XPATH, "//div[@class='a-cardui-body']//h2")
CART_CONTENT = (By.CSS_SELECTOR, "div[data-asin]")
sleep(1)


@when('Press ENTER after input')
def press_enter_in_search_bar(context):
    search_bar = context.driver.find_element(*SEARCH_FIELD)
    search_bar.send_keys(Keys.ENTER)
    sleep(1)


@when('Select first search result')
def select_first_result(context):
    first_result = context.driver.find_element(*FIRST_ELEMENT)
    first_result.click()
    sleep(1)


@when('Add the first element to cart')
def add_to_cart(context):
    add_to_cart_btn = context.driver.find_element(By.ID, 'add-to-cart-button')
    add_to_cart_btn.click()
    sleep(1)


@then('Go to cart to check content')
def go_to_cart(context):
    cart = context.driver.find_element(By.ID, 'nav-cart-count-container')
    cart.click()
    sleep(1)
    if len(context.driver.find_elements(*CART_CONTENT)) == 0:
        print(context.driver.find_element(*CART_DIV).text)
        print(f'Your car has {len(context.driver.find_elements(*CART_CONTENT))} items')
        assert "Your Amazon Cart is empty" == context.driver.find_element(*CART_DIV).text, f'Expected: "Your Amazon Cart is empty", but got: {context.driver.find_element(*CART_DIV).text}'
        sleep(1)
    else:
        print(f'Your cart has {len(context.driver.find_elements(*CART_CONTENT))} items')


