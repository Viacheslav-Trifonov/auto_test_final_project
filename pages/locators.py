

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN = (By.XPATH, "//form[@id='login_form']")
    FORM_REGISTR = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators():
    ADD_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

