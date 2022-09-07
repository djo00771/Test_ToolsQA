import os
import time
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file_for_test_form
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_field_and_submit(self):
        """ Заполнить поля и отправить """
        person = next(generated_person())
        path = generated_file_for_test_form()
        self.remove_element()
        self.is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.is_visible(self.locators.EMAIL).send_keys(person.email)
        self.is_visible(self.locators.GENDER).click()
        self.is_visible(self.locators.MOBILE).send_keys(person.mobile)
        subject = self.is_visible(self.locators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.is_visible(self.locators.HOBBIES).click()
        self.is_visible(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.is_all_visible(self.locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]

        return result_text

