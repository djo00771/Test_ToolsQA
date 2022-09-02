import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators


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

    def check_auto_complete(self):
        pass