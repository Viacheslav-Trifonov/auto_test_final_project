from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        login_url = self.browser.current_url
        assert login_url == 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/', f'{login_url}'

    def should_be_login_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is not presented"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTR), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.email = email
        self.password = password

        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        input_email.send_keys(self.email)

        input_pass1 = self.browser.find_element(*LoginPageLocators.PASS_FORM1)
        input_pass1.send_keys(self.password)

        input_pass2 = self.browser.find_element(*LoginPageLocators.PASS_FORM2)
        input_pass2.send_keys(self.password)

        button_registr = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTR)
        button_registr.click()
