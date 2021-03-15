from behave import given, when, then


# @given('Open Amazon page') is being utilized from: amazon_search.py

@when('Click Amazon Orders link')
def click_orders_link(context):
    context.app.main_page.orders_click()


@then('Verify Sign In page is opened')
def verify_sign_in_opened(context):
    context.app.search_results_page.verify_url_contains_query('signin')
    context.app.amazon_misc_pages.verify_sign_in_opened()


@when('Click on cart icon')
def cart_click(context):
    context.app.main_page.cart_click()


@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_cart_is_empty(context):
    context.app.amazon_misc_pages.verify_cart_is_empty()
