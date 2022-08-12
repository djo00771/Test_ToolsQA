import random
import time
import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            """ Тест формы Text Box"""

            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'full_name не совпадает'
            assert email == output_email, 'email не совпадает'
            assert current_address == output_current, 'current_address не совпадает'
            assert permanent_address == output_per_addr, 'permanent_address не совпадает'

    class TestCheckBox:

        def test_check_box(self, driver):
            """ Тест формы с чек боксами """

            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'Флажки небыли выбраны'

    class TestRadioButton:

        @pytest.mark.xfail(reason="bug report")
        def test_radio_button(self, driver):
            """ Тест кнопок """

            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' небыли выбраны"
            assert output_impressive == 'Impressive', "'Impressive' небыли выбраны"
            assert output_no == 'No', "'No' небыли выбраны"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            """ Тест добавления нового пользователя """

            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_added_person()
            assert new_person in table_result, 'Данные пользователя не совпадают'

        def test_web_table_search_person(self, driver):
            """ Тест поиска пользователя """

            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_come_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'Пользователь не найден'

        def test_web_table_update_person_info(self, driver):
            """ Тест обновления информации о пользователе """

            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_come_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'Пользователя нет в таблице'

        def test_web_table_delete_person_info(self, driver):
            """ Тест обновления информации о пользователе """

            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_come_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_delete()
            assert text == 'No rows found'

        def test_web_table_change_count_rows(self, driver):
            """ Тест проверки количества строк """

            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_come_rows()
            assert count == [5, 10, 20, 25]

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            """ Тест проверки клика по кнопкам """

            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_on_different_button('double')
            right = buttons_page.click_on_different_button('right')
            click_me = buttons_page.click_on_different_button('click')
            assert double == 'You have done a double click', 'Кнопка double click не нажата'
            assert right == 'You have done a right click', 'Кнопка right click не нажата'
            assert click_me == 'You have done a dynamic click', 'Кнопка dynamic click не нажата'

    class TestLinksPage:

        def test_check_link(self, driver):
            """ Тест проверки рабочей ссылки """

            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "Не корректный url либо битая ссылка"

        def test_broken_link(self, driver):
            """ Тест ссылки отправляющей api запрос с кодом 400 """

            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "Не корректный url либо битая ссылка"
