from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

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
SIDE_PANE = (By.ID, 'attach-accessory-pane')
SIDE_PANE_CART = (By.XPATH, "//span[@id='attach-sidesheet-view-cart-button'] //input[@class='a-button-input']")


@when('Press ENTER after input')
def press_enter_in_search_bar(context):
    context.app.main_page.press_key()

    # search_bar = context.driver.find_element(*SEARCH_FIELD)
    # search_bar.send_keys(Keys.ENTER)


@when('Select first search result')
def select_first_result(context):
    context.app.search_results_page.select_first_result()

    # first_result = context.driver.find_elements(*FIRST_ELEMENT_PREFERRED)
    # # first_result = context.driver.find_element(*FIRST_ELEMENT)
    # first_result[0].click()


@when('Add the first element to cart with default size and {quantity} quantity')
def add_to_cart(context, quantity):
    context.app.search_results_page.add_to_cart(quantity)

    # if len(context.driver.find_elements(By.ID, "quantity")):
    #     context.driver.find_element(*QTY_DROPDOWN).click()
    #     context.driver.find_element(By.XPATH,
    #                                 "//li[@class='a-dropdown-item']/a[@data-value='{\"stringVal\":\"" + quantity + "\"}']").click()
    #     # context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()
    #     context.driver.find_element(*ADD_TO_CART_BTN).click()
    #     if context.driver.wait.until(EC.visibility_of_element_located(SIDE_PANE)):
    #         print("Side panel kicked in")
    #         context.driver.find_element(*SIDE_PANE_CART).click()
    #     else:
    #         context.driver.find_element(*ADD_TO_CART_BTN).click()
    # else:
    #     context.driver.find_element(*ADD_TO_CART_BTN).click()
    #     if len(context.driver.find_elements(*SIZE_TOOLTIP)) == 1:
    #         context.driver.find_element(*SIZE_DROPDOWN).click()
    #         context.driver.find_element(*DEFAULT_SIZE).click()
    #         context.driver.find_element(*QTY_DROPDOWN).click()
    #         context.driver.find_element(By.XPATH, "//li[@class='a-dropdown-item']/a[@data-value='{\"stringVal\":\"" + quantity + "\"}']").click()
    #         context.driver.find_element(*ADD_TO_CART_BTN).click()
    #     else:
    #         context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Go to cart to check content & {quantity}')
def go_to_cart(context, quantity):
    context.app.amazon_misc_pages.verify_cart_content(quantity)

    # cart = context.driver.find_element(By.ID, 'nav-cart-count-container')
    # cart.click()
    # if int(context.driver.find_element(*CART_COUNTER).text) == 0:
    #     # if len(context.driver.find_elements(*CART_CONTENT)) == 0:
    #     print(f'Your cart has {len(context.driver.find_elements(*CART_CONTENT))} items')
    #     assert "Your Amazon Cart is empty" == context.driver.find_element(*CART_DIV).text, \
    #         f'Expected: "Your Amazon Cart is empty", ' \
    #         f'but got: {context.driver.find_element(*CART_DIV).text}'
    # else:
    #     print(f'Your cart has {context.driver.find_element(*CART_COUNTER).text} item(s)')
    #     assert int(context.driver.find_element(*CART_COUNTER).text) == int(quantity), f'cart items doesn\'t matcch test quntity\
    #     Cart has {int(context.driver.find_element(*CART_COUNTER).text)} items, \
    #     expected: {int(quantity)}'


@then('Verify cart quantity matches {quantity} that was put in cart')
def verify_amounts_cart(context, quantity):
    context.app.amazon_misc_pages.verify_cart_product_quantity_matches_single_order(quantity)