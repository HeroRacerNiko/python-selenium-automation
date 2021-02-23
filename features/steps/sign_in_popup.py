from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_POPUP = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")


@when('Click on Sign In from popup')
def sign_in_from_popup(context):
    # context.driver.find_element(*SIGN_IN_POPUP).click()
    # same thing as below, but without wait condition
    sign_in_tooltip_btn_with_wait = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP))
    sign_in_tooltip_btn_with_wait.click()


@then('Verify Sign In page opens')
def verify_sign_in_opened(context):
    # print(context.driver.current_url)
    applicant_email_form = context.driver.find_element(By.ID, "ap_email")
    # context.driver.wait.until(EC.url_contains("https://www.amazon.com/ap/signin"),
    #                           f"'Sign in keyword is not present in URL'")
    assert "https://www.amazon.com/ap/signin" in context.driver.current_url, \
        f"'Sign in' keyword is not present in the current URL"
    assert applicant_email_form, f"email form is not present"
