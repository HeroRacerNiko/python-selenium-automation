from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

HELP_SEARCH_BAR = (By.ID, "helpsearch")
URL = 'https://www.amazon.com/gp/help/customer/display.html'
# INFO_PAGE = (By.CSS_SELECTOR, ".help-content > h1 or .help-content > h2")
INFO_PAGE = (By.CSS_SELECTOR, ".help-content")


@given('Open Amazon customer help page')
def open_help_page(context):
    context.driver.get(URL)
    sleep(0.5)

# unnecessary step: no need to click on search bar, it gets selected and keys entered in following step


@when('Click on search bar')
def click_search_bar(context):
    search_bar = context.driver.find_element(*HELP_SEARCH_BAR)
    search_bar.click()
    sleep(0.5)


@when('Enter {command} into search bar')
def enter_cancel_text(context, command):
    search_bar = context.driver.find_element(*HELP_SEARCH_BAR)
    search_bar.send_keys(command)
    sleep(0.5)


@when('Press Enter in search bar after input')
def press_enter(context):
    search_bar = context.driver.find_element(*HELP_SEARCH_BAR)
    search_bar.send_keys(Keys.ENTER)
    sleep(0.5)


@then('{result} should be visible')
def assert_result(context, result):
    actual_text = context.driver.find_element(*INFO_PAGE).text
    print(actual_text)
    expected_text = result
    # assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    assert expected_text in actual_text, f'Expected {expected_text}, but got {actual_text}'
