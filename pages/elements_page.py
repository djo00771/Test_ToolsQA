import random
import time

import locators.element_page_locators
from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """ Элементы страницы Text Box"""
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


class CheckBoxPage(BasePage):
    """ Элементы страницы Check Box"""
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        """ Открыть все чек боксы """
        self.is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        """ Кликнуть по чек боксам рандомно """
        item_list = self.is_all_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.scroll_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        """ Вернуть результат клика """
        checked_list = self.is_all_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        """ Вернуть результат вывода """
        result_list = self.is_all_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()
