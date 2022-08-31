from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramePage, ModalDialogsPage


class TestAlertsFrameWindow:

    class TestBrowserWindowsPage:

        def test_new_tab(self, driver):
            """ Тест переключение на новую вкладку """
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "Вкладка не открыта"

        def test_new_window(self, driver):
            """ Тест переключение на новое окно """
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "Окно не открыто"

    class TestAlertsPage:

        def test_see_alert(self, driver):
            """ Тест окна оповещения """
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_button()
            assert alert_text == 'You clicked a button', "Сообщение не выведено"

        def test_alert_apper_5_second(self, driver):
            """ Тест окна оповещения с задержкой 5 сек. """
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_apper_5_second()
            assert alert_text == 'This alert appeared after 5 seconds', "Сообщение не выведено"

        def test_confirm_alert(self, driver):
            """ Тест подтверждения действия в окне оповещения """
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', "Сообщение не выведено"

        def test_prompt_alert(self, driver):
            """ Тест ввода текста в окно оповещения """
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            # assert на выбор
            assert text in alert_text, "Текст не совпадает"
            assert alert_text == f'You entered {text}', "Текст не совпадает"

    class TestFramePage:

        def test_frame(self, driver):
            """ Тест двух фреймов """
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'the frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'the frame does not exist'

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            """ Тест двух вложенных фреймов """
            nested_frames_page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_result, child_result = nested_frames_page.check_nested_frame()
            assert 'Parent frame' in parent_result, "вы не переключились на фрейм"
            assert 'Child Iframe' in child_result, "вы не переключились на фрейм"

    class TestModalDialogsPage:

        def test_modal_dialog(self, driver):
            """ Тест модальных окон с разным количеством текста """
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            small, large = modal_dialog_page.check_modal_dialogs()
            assert small[1] < large[1]
            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'
