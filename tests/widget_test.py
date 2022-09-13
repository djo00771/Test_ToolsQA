from pages.widget_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


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
        """ Тест выбор даты """
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_before != value_date_after, 'the date has not been changed'

    def test_change_date_and_time(self, driver):
        """ Тест выбор даты и времени """
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        assert value_date_before != value_date_after, 'the date and time have not been changed'


class TestSliderPage:

    def test_slider(self, driver):
        """ Тест передвижение слайдера """
        slider_page = SliderPage(driver, 'https://demoqa.com/slider')
        slider_page.open()
        value_before, value_after = slider_page.check_slider()
        assert value_before != value_after, 'Вы не сдвинули слайдер'


class TestProgressBarPage:

    def test_progress_bar(self, driver):
        """ Тест прогресс загрузки """
        progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        progress_bar_page.open()
        before, after = progress_bar_page.check_progress_bar()
        assert before != after, 'Прогресса нет'

    def test_full_progress_bar(self, driver):
        """ Тест полный прогресс загрузки """
        full_progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        full_progress_bar_page.open()
        full_progress = full_progress_bar_page.check_full_progress_bar()
        assert full_progress == '100', 'Прогресс не завершен'


class TestTabsPage:

    def test_tabs(self, driver):
        """ Тест вкладок """
        tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs_page.open()
        what_button, what_content = tabs_page.check_tabs('what')
        origin_button, origin_content = tabs_page.check_tabs('origin')
        use_button, use_content = tabs_page.check_tabs('use')
        assert what_button == 'What' and what_content > 0, 'Текст отсутствует, или название не верно'
        assert origin_button == 'Origin' and origin_content > 0, 'Текст отсутствует, или название не верно'
        assert use_button == 'Use' and origin_content > 0, 'Текст отсутствует, или название не верно'


class TestToolTipsPage:

    def test_tool_tips(self, driver):
        """ Тест подсказок """
        tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
        assert button_text == 'You hovered over the Button', 'Hover missing or incorrect content'
        assert field_text == 'You hovered over the text field', 'Hover missing or incorrect content'
        assert contrary_text == 'You hovered over the Contrary', 'Hover missing or incorrect content'
        assert section_text == 'You hovered over the 1.10.32', 'Hover missing or incorrect content'


class TestMenuPage:

    def test_menu(self, driver):
        """ Тест меню """
        menu_page = MenuPage(driver, 'https://demoqa.com/menu')
        menu_page.open()
        data = menu_page.check_menu()
        assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                        'Sub Sub Item 2', 'Main Item 3']


class TestSelectMenuPage:

    def test_select_menu(self, driver):
        select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
        select_menu_page.open()
        result_text = select_menu_page.check_select_menu()
        assert result_text[0] == 'Group 2, option 1'
        assert result_text[1] == 'Mrs.'

    def test_multiselect_menu(self, driver):
        multiselect_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
        multiselect_menu_page.open()
        result_text = multiselect_menu_page.check_multiselect_menu()
        assert result_text == ['Green', 'Blue', 'Black', 'Red']
