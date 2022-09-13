import time
import random
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from pages.base_page import BasePage
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        """ Проверка раскрытия сообщения """
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_FIRST_TEXT},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_SECOND_TEXT},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_THIRD_TEXT}
                     }
        section_title = self.is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        """ Ввод данных в строку много цветов """
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        """ Удаление данных из строки много цветов """
        count_value_before = len(self.is_all_present(self.locators.MULTI_VALUE))
        remove_button_list = self.is_all_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.is_all_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        """ Проверка данных в строке много цветов """
        color_list = self.is_all_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        """ Ввод данных в строку один цвет """
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        """ Проверка ввода в строку один цвет """
        color = self.is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        """ Выбор даты """
        date = next(generated_date())
        input_date = self.is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        """ Выбор даты и времени """
        date = next(generated_date())
        input_date = self.is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        """ Установить дату по тексту """
        select = Select(self.is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        """ Установить дату из элементов списка """
        item_list = self.is_all_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def check_slider(self):
        """ Проверка передвижения слайдера """
        value_before = self.is_visible(self.locators.VALUE_INPUT).get_attribute('value')
        slider_input = self.is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        value_after = self.is_visible(self.locators.VALUE_INPUT).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def check_progress_bar(self):
        """ Проверка прогресса загрузки """
        value_before = self.is_present(self.locators.PROGRESS_VALUE).text
        progress_bar_button = self.is_clickable(self.locators.PROGRESS_INPUT)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.is_present(self.locators.PROGRESS_VALUE).text
        return value_before, value_after

    def check_full_progress_bar(self):
        """ Проверка полного прогресса загрузки """
        self.is_visible(self.locators.PROGRESS_INPUT).click()
        time.sleep(12)
        full_progress = self.is_visible(self.locators.FULL_PROGRESS_VALUE).get_attribute('aria-valuenow')
        self.is_visible(self.locators.PROGRESS_RESSET).click()
        return full_progress


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tabs_name):
        """ Проверка переключения между вкладками """
        tabs = {'what':
                    {'title': self.locators.WHAT_TITLE,
                     'content': self.locators.WHAT_CONTENT},
                'origin':
                    {'title': self.locators.ORIGIN_TITLE,
                     'content': self.locators.ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.USE_TITLE,
                     'content': self.locators.USE_CONTENT}
                }
        button = self.is_visible(tabs[tabs_name]['title'])
        button.click()
        what_content = self.is_visible(tabs[tabs_name]['content']).text
        return button.text, len(what_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        """ Возврат текста из всплывающих подсказок """
        element = self.is_present(hover_elem)
        self.action_move_to_element(element)
        self.is_visible(wait_elem)
        time.sleep(1)
        tool_tip_text = self.is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        """ Проверка всплывающих подсказок """
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK,
                                                              self.locators.TOOL_TIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK,
                                                             self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        """ Проверка пунктов меню """
        menu_list = self.is_all_present(self.locators.MENU)
        data = []
        for item in menu_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def check_select_menu(self):
        self.is_visible(self.locators.SELECT_VALUE_INPUT).click()
        self.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
        self.is_visible(self.locators.SELECT_ONE_INPUT).click()
        self.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
        result_list = self.is_all_present(self.locators.SELECT_RESULT_LIST)
        data = []
        for item in result_list:
            data.append(item.text)
        return data

    def check_multiselect_menu(self):
        self.is_visible(self.locators.MULTISELECT_INPUT).click()
        self.send_keys(Keys.RETURN, Keys.RETURN, Keys.RETURN, Keys.RETURN)
        result_list = self.is_all_present(self.locators.MULTISELECT_RESULT_LIST)
        data = []
        for i in result_list:
            data.append(i.text)
        return data
