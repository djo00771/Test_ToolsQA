import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            """ Переключение на новую вкладку """
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "Вкладка не открыта"

        def test_new_window(self, driver):
            """ Переключение на новое окно """
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "Окно не открыто"

    class TestAlerts:

        def test_see_alert(self, driver):
            """ Переключение на окно сообщения """
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_button()
            assert alert_text == 'You clicked a button', "Сообщение не выведено"

        def test_alert_apper_5_second(self, driver):
            """ Переключение на окно сообщения через 5 сек. """
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_apper_5_second()
            assert alert_text == 'This alert appeared after 5 seconds', "Сообщение не выведено"

        def test_confirm_alert(self, driver):
            """ Выполнить действие в окне сообщения """
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', "Сообщение не выведено"

        def test_prompt_alert(self, driver):
            """ Выполнить действие в окне сообщения """
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            # assert на выбор
            assert text in alert_text, "Текст не совпадает"
            assert alert_text == f'You entered {text}', "Текст не совпадает"
