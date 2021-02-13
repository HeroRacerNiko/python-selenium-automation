from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

# -------------------------------------------------------------------------
# 'Open Amazon page' step declared in "amazon_search.py"
# 'Input dress into Amazon search field' borrowed from "amazon_search.py"
# -------------------------------------------------------------------------
FIRST_ELEMENT = (By.CSS_SELECTOR, "div[data-index='2']")
FIRST_ELEMENT_PREFERRED = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART_DIV = (By.XPATH, "//div[@class='a-cardui-body']//h2")
CART_CONTENT = (By.CSS_SELECTOR, "div[data-asin]")
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_DROPDOWN = (By.ID, 'dropdown_selected_size_name')
DEFAULT_SIZE = (By.ID, 'size_name_0')
CART_COUNTER = (By.XPATH, "//span[@id='nav-cart-count']")
QTY_DROPDOWN = (By.XPATH, "//span[@class='a-button a-button-dropdown a-button-small']")
# QTY_OPTIONS = (By.XPATH, "//li[@class='a-dropdown-item']/a[@data-value='{\"stringVal\":\"10\"}']")
sleep(1)


@when('Press ENTER after input')
def press_enter_in_search_bar(context):
    search_bar = context.driver.find_element(*SEARCH_FIELD)
    search_bar.send_keys(Keys.ENTER)
    sleep(1)


@when('Select first search result')
def select_first_result(context):
    first_result = context.driver.find_elements(*FIRST_ELEMENT_PREFERRED)
    # first_result = context.driver.find_element(*FIRST_ELEMENT)
    first_result[0].click()
    sleep(1)


@when('Add the first element to cart with default size and {quantity} quantity')
def add_to_cart(context, quantity):
    print(len(context.driver.find_elements(By.ID, "quantity")))
    if len(context.driver.find_elements(By.ID, "quantity")):
        context.driver.find_element(*QTY_DROPDOWN).click()
        sleep(0.5)
        context.driver.find_element(By.XPATH,
                                    "//li[@class='a-dropdown-item']/a[@data-value='{\"stringVal\":\"" + quantity + "\"}']").click()
        sleep(0.5)
        context.driver.find_element(*ADD_TO_CART_BTN).click()
    else:
        context.driver.find_element(*ADD_TO_CART_BTN).click()
        if len(context.driver.find_elements(*SIZE_TOOLTIP)) == 1:
            context.driver.find_element(*SIZE_DROPDOWN).click()
            context.driver.find_element(*DEFAULT_SIZE).click()
            sleep(2)
            context.driver.find_element(*QTY_DROPDOWN).click()
            sleep(0.5)
            context.driver.find_element(By.XPATH, "//li[@class='a-dropdown-item']/a[@data-value='{\"stringVal\":\"" + quantity + "\"}']").click()
            sleep(0.5)
            context.driver.find_element(*ADD_TO_CART_BTN).click()
        else:
            context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(1)


@then('Go to cart to check content')
def go_to_cart(context):
    cart = context.driver.find_element(By.ID, 'nav-cart-count-container')
    cart.click()
    sleep(1)
    if int(context.driver.find_element(*CART_COUNTER).text) == 0:
        # if len(context.driver.find_elements(*CART_CONTENT)) == 0:
        print(context.driver.find_element(*CART_DIV).text)
        print(f'Your cart has {len(context.driver.find_elements(*CART_CONTENT))} items')
        assert "Your Amazon Cart is empty" == context.driver.find_element(*CART_DIV).text, f'Expected: "Your Amazon Cart is empty", but got: {context.driver.find_element(*CART_DIV).text}'
        sleep(1)
    else:
        print(f'Your cart has {context.driver.find_element(*CART_COUNTER).text} item(s)')


