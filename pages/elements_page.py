import time

from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """ Заполнить и отправить """
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.is_visible(self.locators.EMAIL).send_keys(email)
        self.is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """ Проверка из ответа """
        full_name = self.is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
    