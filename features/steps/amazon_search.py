from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input Watches into Amazon search field')
def input_amazon_search(context):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')