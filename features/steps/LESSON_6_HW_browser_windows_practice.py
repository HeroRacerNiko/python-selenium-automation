from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

DOG_BLOG = (By.XPATH, "//img[@id='d'] [@alt='Dogs of Amazon']")
# DOG_BLOG = (By.CSS_SELECTOR, "a[href='/dogsofamazon'] img")
# DOG_BLOG = (By.ID, 'g')
BESTSELLER_LINKS = (By.XPATH, "//div[@id='zg_tabs'] //a[contains(@href, 'ref=zg')]")
TITLE = (By.XPATH, "//div[@id='zg_banner_text_wrapper']")
bestseller_expected_titles = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on 404 blog')
def click_on_404(context):
    assert context.driver.find_element(*DOG_BLOG), f'Dog image element not found'
    context.driver.find_element(*DOG_BLOG).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then('User can close new window and switch back to the original')
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)


@then('Iterate over bestseller links, verify changes in title')
def iterate_over_bestseller_links(context):
    # index = 0
    # while index < len(context.driver.find_elements(*BESTSELLER_LINKS)):
    #     best_sellers_tab = context.driver.find_elements(*BESTSELLER_LINKS)
    #     best_sellers_tab[index].click()
    #     best_sellers_tab = context.driver.find_elements(*BESTSELLER_LINKS)
    #     page_title = context.driver.find_element(*TITLE)
    #     assert bestseller_expected_titles[index] in page_title.text, \
    #         f'{bestseller_expected_titles[index]} not in {page_title.text}'
    #     assert best_sellers_tab[index].text in page_title.text, \
    #         f'Error: web element text not in page title'
    #     index += 1
    link_tab = context.driver.find_elements(*BESTSELLER_LINKS)
    for index in range(len(link_tab)):
        link = context.driver.find_elements(*BESTSELLER_LINKS)[index]
        link_text = link.text
        link.click()
        header_text = context.driver.find_element(*TITLE).text
        assert link_text in header_text, f'Error...' \
                                         f'{link_text} is not in {header_text}'
