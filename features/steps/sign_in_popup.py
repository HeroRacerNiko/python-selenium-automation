from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SIGN_IN_POPUP = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
MAIN_SEARCH = (By.ID, 'twotabsearchtextbox')


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
# ############################ScenarioOutlineWithWait##############################################


@when('Verify tooltip popup appears and clickable')
def check_for_tooltip(context):
    # either one of following verification should work
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP))
    assert context.driver.find_element(*SIGN_IN_POPUP), f"Tooltip did not load..."


@when('Wait for {sec} seconds')
def hard_sleep(context, sec):
    # context.driver.refresh()
    sleep(int(sec))


@then('Verify tooltip disappears in {sec} seconds')
def verify_tooltip_hidden(context, sec):
    # tooltip doesn't disappear after 4 seconds but implicit wait
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP))
    context.driver.wait.until(EC.presence_of_element_located(MAIN_SEARCH))
    # context.driver.find_element(*MAIN_SEARCH) # does same thing as above

