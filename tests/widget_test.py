from pages.widget_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage


class TestAccordianPage:

    def test_widget(self, driver):
        """ Тест раскрывающихся сообщений """
        accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian('first')
        second_title, second_content = accordian_page.check_accordian('second')
        third_title, third_content = accordian_page.check_accordian('third')
        assert first_title == 'What is Lorem Ipsum?' and first_content > 0
        assert second_title == 'Where does it come from?' and second_content > 0
        assert third_title == 'Why do we use it?' and third_content > 0


class TestAutoCompletePage:

    def test_fill_multi_autocomplete(self, driver):
        """ Тест добавление цветов, в строку много цветов """
        autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplete_page.open()
        colors = autocomplete_page.fill_input_multi()
        colors_result = autocomplete_page.check_color_in_multi()
        assert colors == colors_result, 'добавленные цвета отсутствуют во входных данных'

    def test_remove_value_from_multi(self, driver):
        """ Тест удаления цвета из строки много цветов """
        autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
        assert count_value_before != count_value_after, "значение не было удалено"

    def test_fill_single_autocomplete(self, driver):
        """ Тест добавления цвета в строку один цвет """
        autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplete_page.open()
        color = autocomplete_page.fill_input_single()
        color_result = autocomplete_page.check_color_in_single()
        assert color == color_result, 'добавленные цвета отсутствуют во входных данных'


class TestDatePickerPage:

    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_before != value_date_after, 'the date has not been changed'

    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        assert value_date_before != value_date_after, 'the date and time have not been changed'


class TestSliderPage:

    def test_slider(self, driver):
        slider_page = SliderPage(driver, 'https://demoqa.com/slider')
        slider_page.open()
        value_before, value_after = slider_page.check_slider()
        assert value_before != value_after, 'Вы не сдвинули слайдер'


class TestProgressBarPage:

    def test_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        progress_bar_page.open()
        before, after = progress_bar_page.check_progress_bar()
        assert before != after, 'Прогресса нет'

    def test_full_progress_bar(self, driver):
        full_progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        full_progress_bar_page.open()
        full_progress = full_progress_bar_page.check_full_progress_bar()
        assert full_progress == '100', 'Прогресс не завершен'


class TestTabsPage:

    def test_tabs(self, driver):
        tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs_page.open()
        what_button, what_content = tabs_page.check_tabs('what')
        origin_button, origin_content = tabs_page.check_tabs('origin')
        use_button, use_content = tabs_page.check_tabs('use')
        assert what_button == 'What' and what_content > 0, 'Текст отсутствует, или название не верно'
        assert origin_button == 'Origin' and origin_content > 0, 'Текст отсутствует, или название не верно'
        assert use_button == 'Use' and origin_content > 0, 'Текст отсутствует, или название не верно'
