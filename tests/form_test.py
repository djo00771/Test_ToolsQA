from pages.form_page import FormPage


class TestForm:

    def test_form(self, driver):
        """ Тест формы регистрации """

        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_field_and_submit()
        result = form_page.form_result()
        assert f'{person.first_name} {person.last_name}' == result[0], 'Форма не была заполнена'
        assert person.email == result[1], 'Форма не была заполнена'
        assert person.subject == result[5], 'Форма не была заполнена'
