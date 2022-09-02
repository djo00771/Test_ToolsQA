from pages.widget_page import AccordianPage, AutoCompletePage


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

    def test_auto_complete(self, driver):
        auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
        auto_complete_page.open()