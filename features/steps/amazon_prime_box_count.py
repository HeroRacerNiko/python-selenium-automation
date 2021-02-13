from selenium.webdriver.common.by import By
from behave import given, when, then

PRIME_BOXES_LOC = (By.CSS_SELECTOR, '.benefit-box')
BESTSELLER_LINKS = (By.XPATH, "//div[@id='zg_tabs']//a[contains(@href, 'ref=zg_bs_tab')]")


@given("Open Amazon Prime page")
def open_amazon_page(context):
    context.driver.get("https://www.amazon.com/amazonprime")


@given("Open Amazon Prime BestSellers page")
def open_best_sellers(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then("Verify page has {number} links")
def verify_links_count(context, number):
    best_sellers_tab = context.driver.find_elements(*BESTSELLER_LINKS)
    print(len(best_sellers_tab))
    assert len(best_sellers_tab) == int(number), f'Expected: {number} links, got: {len(best_sellers_tab)}.'


@then("Verify page has {number} boxes")
def verify_count(context, number):
    benefit_boxes = context.driver.find_elements(*PRIME_BOXES_LOC)
    actual_count = (len(benefit_boxes))
    print(len(benefit_boxes))
    assert actual_count == int(number), f'Expected: {number}, got: {actual_count}'
