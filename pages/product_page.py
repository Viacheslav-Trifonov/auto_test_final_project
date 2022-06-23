from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators, ProductPageLocators




class ProductPage(BasePage):
    def should_be_basket_page(self):
        self.add_to_basket()
        self.compare_product()
        self.should_not_be_success_message()
        self.should_disappeared()
        self.disappeared_after_adding()

    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        basket_link.click()

    def compare_product(self):
        name_product1 = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product2 = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BASKET)
        assert name_product1.text == name_product2.text, 'Товар неверно добавлен в корзину'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение появилось, верно"


    def should_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение не появилось, верно"


    def disappeared_after_adding(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение не исчезло, верно"

