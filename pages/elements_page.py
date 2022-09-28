import base64
import os
import random
import time

import allure
import requests
from selenium.common import TimeoutException
from generator.generator import generated_person, generated_file_for_test_elements
from locators.element_page_locators import *
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """ Элементы страницы Text Box"""
    locators = TextBoxPageLocators()

    @allure.step('Заполнить все поля и отправить')
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('Заполнение данными'):
            self.is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.is_visible(self.locators.EMAIL).send_keys(email)
            self.is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('Клик по кнопке "Отправить данные"'):
            self.is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('Проверить заполненную форму')
    def check_filled_form(self):
        full_name = self.is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    """ Элементы страницы Check Box"""
    locators = CheckBoxPageLocators()

    @allure.step('Открыть весь список чек боксов')
    def open_full_list(self):
        self.is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Рандомно кликнуть по чек боксам')
    def click_random_checkbox(self):
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

    @allure.step('Вернуть результат клика')
    def get_checked_checkboxes(self):
        checked_list = self.is_all_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('Вернуть результат вывода')
    def get_output_result(self):
        result_list = self.is_all_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    """ Элементы страницы Radio Button """
    locators = RadioButtonPageLocators()

    @allure.step('Кликнуть по кнопкам')
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}

        self.is_visible(choices[choice]).click()

    @allure.step('Вернуть результат клика')
    def get_output_result(self):
        return self.is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    """ Элементы страницы Web Table """
    locators = WebTablePageLocators()

    @allure.step('Добавление нового пользователя в форму Web Table')
    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            with allure.step('Ввести и отправить данные'):
                self.is_visible(self.locators.ADD_BUTTON).click()
                self.is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
                self.is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
                self.is_visible(self.locators.EMAIL_INPUT).send_keys(email)
                self.is_visible(self.locators.AGE_INPUT).send_keys(age)
                self.is_visible(self.locators.SALARY_INPUT).send_keys(salary)
                self.is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            with allure.step('Отправить данные'):
                self.is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_person(self):
        """ Проверка результатов добавления пользователя """
        people_list = self.is_all_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('Поиск пользователя')
    def search_come_person(self, key_word):
        self.is_present(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Проверка результатов поиска пользователя')
    def check_search_person(self):
        delete_button = self.is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Обновления информации о пользователе')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        with allure.step('Ввести данные и отправить'):
            self.is_visible(self.locators.UPDATE_BUTTON).click()
            self.is_visible(self.locators.AGE_INPUT).clear()
            self.is_visible(self.locators.AGE_INPUT).send_keys(age)
        with allure.step('Отправить данные'):
            self.is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step('Удаление пользователя')
    def delete_person(self):
        self.is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Проверка удаления пользователя')
    def check_delete(self):
        return self.is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('Выбор количества строк')
    def select_up_to_come_rows(self):
        count = [5, 10, 20, 25]
        data = []
        for x in count:
            count_row_button = self.is_visible(self.locators.COUNT_ROW_LIST)
            self.scroll_to_element(count_row_button)
            count_row_button.click()
            self.is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('Проверка количества строк')
    def check_count_rows(self):
        list_round = self.is_all_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_round)


class ButtonsPage(BasePage):
    """Элементы страницы Buttons """
    locators = ButtonsPageLocators()

    @allure.step('Проверка клика: double click, right click, dynamic click')
    def click_on_different_button(self, type_click):
        if type_click == 'double':
            self.double_click(self.is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_click_on_button(self.locators.SUCCESS_DOUBLE)

        if type_click == 'right':
            self.right_click(self.is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_click_on_button(self.locators.SUCCESS_RIGHT)

        if type_click == 'click':
            self.is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_click_on_button(self.locators.SUCCESS_CLICK_ME)

    @allure.step('Возврат результата кликов')
    def check_click_on_button(self, element):
        return self.is_present(element).text


class LinksPage(BasePage):
    """Элементы страницы Links """
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.is_visible(self.locators.HOME_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            self.click(simple_link)
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.get_current_url()
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.click(self.is_present(self.locators.BAD_REQUEST))
        else:
            return r.status_code


class UploadDownloadFilePage(BasePage):
    """ Загрузка и выгрузка файла """
    locators = UploadDownloadFileLocators()

    def upload_file(self):
        """ Выгрузка """
        file_name, path = generated_file_for_test_elements()
        self.is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.is_present(self.locators.UPLOADED_FILE).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_file(self):
        """ Загрузка """
        link = self.is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)  # декодируем
        # путь по которому мы поместим файл
        path_name_file = rf'C:\Users\zay-e\PycharmProjects\Test_ToolsQA\filetest{random.randint(0, 500)}.jpg'
        with open(path_name_file, 'wb+') as f:  # Открываем файл для записи
            offset = link_b.find(b'\xff\xd8')  # обрезаем лишнее и записываем в переменную
            f.write(link_b[offset:])  # записываем обрезанное
            check_file = os.path.exists(path_name_file)  # проверяем что файл существует
            f.close()  # закрываем файл
        os.remove(path_name_file)  # удаляем файл
        return check_file


class DynamicPropertiesPage(BasePage):
    """ Изменение цвета и видимость кнопок """
    locators = DynamicPropertiesLocators()

    def check_enable_button(self):
        """ Проверка clickable """
        try:
            self.is_clickable(self.locators.ENABLE_BUTTON, 6)
        except TimeoutException:
            return False
        return True

    def check_change_of_color(self):
        """ Проверка изменение цвета """
        color_button = self.is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_appear_of_button(self):
        """ Проверка появление через 5 секунд """
        try:
            self.is_visible(self.locators.VISIBLE_AFTER_BUTTON, 6)
        except TimeoutException:
            return False
        return True

