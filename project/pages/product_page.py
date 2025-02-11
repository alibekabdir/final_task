from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.add_to_basket_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
        self.product_name = (By.CSS_SELECTOR, ".product_main h1")
        self.product_price = (By.CSS_SELECTOR, ".product_main .price_color")
        self.basket_message = (By.CSS_SELECTOR, ".alert-success strong")
        self.basket_total = (By.CSS_SELECTOR, ".alert-info strong")

    def add_to_basket(self):
        self.browser.find_element(*self.add_to_basket_button).click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*self.product_name).text

    def get_product_price(self):
        return self.browser.find_element(*self.product_price).text

    def get_basket_message(self):
        return self.browser.find_element(*self.basket_message).text

    def get_basket_total(self):
        return self.browser.find_element(*self.basket_total).text