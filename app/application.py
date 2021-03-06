from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.amzn_misc_pages import AmazonMiscPages


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.amazon_misc_pages = AmazonMiscPages(self.driver)
