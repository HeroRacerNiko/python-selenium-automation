from selenium.webdriver.common.by import By
from behave import given, when, then

PRIME_BOXES_LOC = (By.CSS_SELECTOR, '.benefit-box')


@given("Open Amazon Prime page")
def open_amazon_prime(context):
    context.driver.get("https://amazon.com/amazonprime")


@then("Verify page has {box_count} boxes")
def verify_count(context, box_count):
    benefit_boxes = context.driver.find_elements(*PRIME_BOXES_LOC)
    actual_count = (len(benefit_boxes))
    print(len(benefit_boxes))
    assert actual_count == int(box_count), f'Expected: {box_count}, got: {actual_count}'
