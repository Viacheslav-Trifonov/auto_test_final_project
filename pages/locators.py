from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    FORM_LOGIN = (By.XPATH, "//form[@id='login_form']")
    FORM_REGISTR = (By.XPATH, "//form[@id='register_form']")
    EMAIL_FORM = (By.XPATH, "//input[@name='registration-email']")
    PASS_FORM1 = (By.XPATH, "//input[@name='registration-password1']")
    PASS_FORM2 = (By.XPATH, "//input[@name='registration-password2']")
    BUTTON_REGISTR = (By.XPATH, "//button[@value='Register']")


class ProductPageLocators:
    ADD_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    FULL_BASKET = (By.XPATH, "//p[@class='col-sm-3 h3']")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
