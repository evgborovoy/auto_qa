from pages.elements_page import CheckBoxPage, RadioButtonPage, TextBoxPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, cur_address, per_address = text_box_page.fill_all_fields()
            filled_full_name, filled_email, filled_cur_address, filled_per_address = text_box_page.check_filled_info()
            per_address = per_address.replace("\n", " ")
            cur_address = cur_address.replace("\n", " ")
            assert filled_full_name == full_name, "full_name is not equal filled_full_name"
            assert filled_email == email, "email is not equal filled_email"
            assert filled_cur_address == cur_address, "current_address is not equal filled_current_address"
            assert filled_per_address == per_address, "permanent_address is not equal filled_permanent_address"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_on_random_checkbox()
            checked_items = check_box_page.get_checked_checkboxes()
            control_list = check_box_page.get_items_from_filed()
            assert checked_items == control_list, "Selected items not match"

    class TestRadioButton:

        def test_yes_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_radio("yes")
            result = radio_button_page.get_selected_text()
            assert result == "Yes", "Yes radio button not selected"

        def test_impressive_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_radio("impressive")
            result = radio_button_page.get_selected_text()
            assert result == "Impressive", "Impressive radio button not selected"

        def test_no_radio_button_is_disabled(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            result = radio_button_page.get_no_radio_status()
            assert result == False, "No radio button is enabled"

    class TestWebTable:

        def test_add_record(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person_info = list(web_table_page.add_record())
            rows = web_table_page.check_records_list()
            assert person_info in rows, "Record not added"

        def test_search_record(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person_info = list(web_table_page.add_record())
            web_table_page.search_record(person_info[0])
            rows = web_table_page.check_records_list()
            assert person_info in rows, f"Can't find {person_info} in table trough search field"
