from locators.alerts_frame_windows_locators import BrowserWindowsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsLocators()

    def check_opened_new_tab(self):
        self.is_visible(self.locators.NEW_TAB).click()
        self.switch_new_tab(1)
        text_title = self.is_present(self.locators.TITLE_NEW_TAB).text
        return text_title

    def check_opened_new_window(self):
        self.is_visible(self.locators.NEW_WINDOW).click()
        self.switch_new_tab(1)
        text_title = self.is_present(self.locators.TITLE_NEW_TAB).text
        return text_title
