import random
import time
from selenium.common import UnexpectedAlertPresentException
from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsLocators
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
        """ Проверка открытия сообщения в браузере """
        self.is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.switch_new_alert()
        return alert_window.text

    def check_alert_apper_5_second(self):
        """ Проверка открытия сообщения в браузере через 5 сек. """
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
        self.is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.switch_new_alert()
        alert_window.accept()
        text_result = self.is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f'test-autotest {random.randint(0, 900)}'
        self.is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.switch_new_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.is_present(self.locators.PROMPT_RESULT).text
        return text, text_result

