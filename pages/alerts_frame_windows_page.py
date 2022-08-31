import random
import time
from selenium.common import UnexpectedAlertPresentException
from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsLocators, FrameLocators, \
    NestedFrameLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsLocators()

    def check_opened_new_tab(self):
        """ Проверка открытия новой вкладки """
        self.is_visible(self.locators.NEW_TAB).click()
        self.switch_new_tab(1)
        text_title = self.is_present(self.locators.TITLE_NEW_TAB).text
        return text_title

    def check_opened_new_window(self):
        """ Проверка открытия нового окна """
        self.is_visible(self.locators.NEW_WINDOW).click()
        self.switch_new_tab(1)
        text_title = self.is_present(self.locators.TITLE_NEW_TAB).text
        return text_title


class AlertsPage(BasePage):

    locators = AlertsLocators()

    def check_alert_button(self):
        """ Проверка открытия оповещения """
        self.is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.switch_new_alert()
        return alert_window.text

    def check_alert_apper_5_second(self):
        """ Проверка открытия оповещения через 5 сек. """
        self.is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        time.sleep(5)
        # при низкой скорости интернета возникает исключение, в остальном блок try можно исключить
        try:
            alert_window = self.switch_new_alert()
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.switch_new_alert()
            return alert_window.text

    def check_confirm_alert(self):
        """ Проверка подтверждения действия в окне оповещения """
        self.is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.switch_new_alert()
        alert_window.accept()
        text_result = self.is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        """ Проверка ввода текста в окне оповещения """
        text = f'test-autotest {random.randint(0, 900)}'
        self.is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.switch_new_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramePage(BasePage):
    """ Фреймы """
    locators = FrameLocators()

    def check_frame(self, frame_num):
        """ Проверка двух фреймов на странице """
        if frame_num == 'frame1':
            frame = self.is_present(self.locators.FRAME1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_iframe(frame)
            text = self.is_present(self.locators.TEXT_FRAME).text
            self.switch_out_iframe()
            return [text, width, height]

        if frame_num == 'frame2':
            frame = self.is_present(self.locators.FRAME2)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_iframe(frame)
            text = self.is_present(self.locators.TEXT_FRAME).text
            self.switch_out_iframe()
            return [text, width, height]


class NestedFramePage(BasePage):
    """ Вложенные фреймы """
    locators = NestedFrameLocators()

    def check_nested_frame(self):
        """ Проверка двух вложенных фреймов на странице"""
        parent_frame = self.is_present(self.locators.PARENT_FRAME)
        self.switch_to_iframe(parent_frame)
        parent_text = self.is_present(self.locators.PARENT_TEXT).text
        child_frame = self.is_present(self.locators.CHILD_FRAME)
        self.switch_to_iframe(child_frame)
        child_text = self.is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    """ Модальные окна """
    locators = ModalDialogsPageLocators()

    def check_modal_dialogs(self):
        """ Проверка модальных окон с разным количеством текста """
        self.is_visible(self.locators.SMALL_MODAL).click()
        small_body_text = self.is_visible(self.locators.SMALL_MODAL_TEXT).text
        small_body_title = self.is_visible(self.locators.SMALL_MODAL_BODY).text
        self.is_visible(self.locators.SMALL_MODAL_CLOSE).click()
        self.is_visible(self.locators.LARGE_MODAL).click()
        large_body_text = self.is_visible(self.locators.LARGE_MODAL_TEXT).text
        large_body_title = self.is_visible(self.locators.LARGE_MODAL_BODY).text
        self.is_visible(self.locators.LARGE_MODAL_CLOSE).click()
        return [small_body_title, len(small_body_text)], [large_body_title, len(large_body_text)]


