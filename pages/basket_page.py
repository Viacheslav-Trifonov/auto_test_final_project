from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.net_tovarov()
        self.net_texta()

    def net_tovarov(self):
        assert self.is_not_element_present(*BasketPageLocators.FULL_BASKET), \
            "В корзине есть товары"

    def net_texta(self):
        assert not self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "В корзине пусто"
