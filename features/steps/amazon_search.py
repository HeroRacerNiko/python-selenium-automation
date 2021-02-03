from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {query} into Amazon search field')
def input_amazon_search(context, query):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.send_keys(query)


@when('Click on Amazon search icon')
def click_search_amazon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then('Product results for {query} are shown on Amazon')
def verify_search_result(context, query):
    actual_text = context.driver.find_element(*RESULT).text
    expected_text = f'{query}'
    assert expected_text == actual_text, f'Expected: {expected_text}, but got {actual_text}'


@then('Page URL has {query} in it')
def verify_url_contains_query(context, query):
    print(f'Current URL: "{context.driver.current_url}" DOES contain "{query}"')
    assert query in context.driver.current_url, f'Watches not in {context.driver.current_url}'

