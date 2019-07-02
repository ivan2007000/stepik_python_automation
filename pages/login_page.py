from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password_field2.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        register_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """проверка на корректный url адрес"""
        assert ('login' in self.browser.current_url), "Login URL does not contains 'login' word."
        # assert ('login' in self.url), "Login URL does not contains 'login' word."

    def should_be_login_form(self):
        """проверка, что есть форма логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found."

    def should_be_register_form(self):
        """проверка, что есть форма регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found."