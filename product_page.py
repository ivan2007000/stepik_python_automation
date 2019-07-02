from .base_page import BasePage
import math
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_promo_url()

    def should_be_promo_url(self):
        assert "?promo=" in self.browser.current_url, "Некорректный URL"

    def click_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Login form is not presented"
        add_button = self.browser.find_element_by_class_name("btn-add-to-basket")
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"