from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

amazon_tc_url = "https://www.amazon.com/gp/help/customer/display.html/" \
                "ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088"
APPLICATIONS_LINK = (By.XPATH,
                     "//a[@href='https://www.amazon.com/gp/feature.html?docId=1000625601']")
TEXT_ELEMENT = (By.CSS_SELECTOR, "[class*=bxc-grid__content] h1")
DOWNLOAD_APP = (By.CSS_SELECTOR, "div[id=mgt-email-sms-left] p[id=mgt-email-sms-download-header]")
STORE_REDIRECT_LINKS = (By.XPATH, "//div[contains(@class, 'bxc-grid__image')] "
                                  "//a[contains(@href, 'redirect.html')]")


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get(amazon_tc_url)


@when('Click on Amazon applications link')
def click_on_applications_link(context):
    context.driver.find_element(*APPLICATIONS_LINK).click()


@then('Verify Amazon app page is opened')
def verify_amazon_app_page_opens(context):
    visit_app_store_ele = context.driver.find_element(*TEXT_ELEMENT)
    # context.driver.wait.until(EC.presence_of_element_located(TEXT_ELEMENT))
    assert 'Visit your app store to learn more and download the app.' \
           in visit_app_store_ele.text, f'Error'
    download_app_ele = context.driver.find_element(*DOWNLOAD_APP)
    assert 'Download the app today!' == download_app_ele.text, \
        f'Expected text not found'
    assert '?docId=1000625601' in context.driver.current_url, \
        f'docID=1000625601 not found in url'
    store_redirect_links = context.driver.find_elements(*STORE_REDIRECT_LINKS)
    assert len(store_redirect_links) == 2, f'Error...'
