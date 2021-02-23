from behave import when, then, given
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC


COLORS_ELS = (By.XPATH, "//ul[contains(@class, 'a-unordered-list a-nostyle a-button-list')] "
                        "/li[contains(@id, 'color_name')]")
COLORS_NAMES = (By.CSS_SELECTOR, "div.a-row span.selection")


@given('Open amazon url with product {product_id}')
def open_url_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then('Iterate over list of colors, assert, print')
def capture_and_iterate(context):
    colors_box = context.driver.find_elements(*COLORS_ELS)
    colors_list = []

    for i in range(len(colors_box)):
        colors_box[i].click()
        colors_text = context.driver.find_element(*COLORS_NAMES).text
        colors_list.append(colors_text)
        # We can verify each color selection if we know the color list, for now, since it is a big
        # list I decided to report number and list of colors for particular product.
        # assert colors_text == expected_colors[i], f'{colors_text} not == {expected_colors[i]}'
    print(f'This product has {len(colors_box)} colors: {*colors_list,}')
    # return ???
    return colors_list


RESULTS_LIST = (By.XPATH, "//ul[@class='s-result-list s-col-3 wfm-desktop-list-font-unset s-height-equalized'] //li")
RESULTS_LIST_PR_NAME = (By.XPATH, "//ul[@class='s-result-list s-col-3 wfm-desktop-list-font-unset s-height-equalized'] "
                                  "//li//span[@class='a-size-medium wfm-sales-item-card__product-name a-text-bold']")


@given('Open amazon Whole Foods page')
def whole_foods_open(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@when('Iterate and verify product name in each element')
def product_name_ver(context):
    results_list_pr_name = context.driver.find_elements(*RESULTS_LIST_PR_NAME)
    for index in range(len(results_list_pr_name)):
        print(f'#{index+1}: {results_list_pr_name[index].text}')
        assert results_list_pr_name[index].text, f'Element at index {index} is missing a product name'


@then('Iterate and verify keyword "Regular"')
def key_word_ver(context):
    results_list = context.driver.find_elements(*RESULTS_LIST)
    print(f'Deals page features {len(results_list)} items')
    for index in range(len(results_list)):
        if "Regular" in results_list[index].text:
            print(f'"Regular" is in element #{index + 1}')
        assert 'Regular' in results_list[index].text, f'Couldn\'t find "Regular" in element # {index + 1}'
