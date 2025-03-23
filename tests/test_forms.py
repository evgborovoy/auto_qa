import allure

from pages.forms_page import PracticeFormPage


@allure.suite("Forms")
class TestForms:
    @allure.feature("Practice form")
    class TestPracticeForm:

        @allure.title("Fill form")
        def test_fill_form(self, driver):
            practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
            practice_form_page.open()
            person = practice_form_page.fill_form()
            result = practice_form_page.get_info_from_table()
            print(person)
            print(result)
            assert person.first_name + " " + person.last_name == result[0], "Incorrect name"
            assert person.email == result[1], "Incorrect email"
            assert str(person.phone) == result[3]
            assert person.current_address == result[8]
