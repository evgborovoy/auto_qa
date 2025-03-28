from pages.elements_page import *
import allure


@allure.suite("Elements")
class TestElements:
    @allure.feature("Text Box page")
    class TestTextBox:

        @allure.title("Check text box")
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

    @allure.feature("Check Box page")
    class TestCheckBox:

        @allure.title("Test Check box")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_on_random_checkbox()
            checked_items = check_box_page.get_checked_checkboxes()
            control_list = check_box_page.get_items_from_filed()
            assert checked_items == control_list, "Selected items not match"

    @allure.feature("Radio button page")
    class TestRadioButton:

        @allure.title("Check 'Yes' radio button ")
        def test_yes_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_radio("yes")
            result = radio_button_page.get_selected_text()
            assert result == "Yes", "Yes radio button not selected"

        @allure.title("Check 'Impressive' radio button ")
        def test_impressive_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_radio("impressive")
            result = radio_button_page.get_selected_text()
            assert result == "Impressive", "Impressive radio button not selected"

        @allure.title("Check disabled radio button")
        def test_no_radio_button_is_disabled(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            result = radio_button_page.get_no_radio_status()
            assert result == False, "No radio button is enabled"

    @allure.feature("Web Table page")
    class TestWebTable:

        @allure.title("Add record in table")
        def test_add_record(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person_info = list(web_table_page.add_record())
            rows = web_table_page.check_records_list()
            assert person_info in rows, "Record not added"

        @allure.title("Test find record in using search field")
        def test_search_record(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person_info = list(web_table_page.add_record())
            web_table_page.search_record(person_info[0])
            rows = web_table_page.check_records_list()
            assert person_info in rows, f"Can't find {person_info} in table trough search field"

        @allure.title("Edit record")
        def test_edit_record(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person = web_table_page.add_record()[1]
            web_table_page.search_record(person)
            changes = web_table_page.edit_person_info()
            rows = web_table_page.check_records_list()
            print(person, changes, rows, sep="\n")
            assert changes in rows[0], "Record does not changed"

        @allure.title("Delete record in table")
        def test_delete_record(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person = web_table_page.add_record()
            web_table_page.search_record(person[3])  # find by email
            web_table_page.delete_row()
            rows = web_table_page.check_records_list()
            assert person not in rows, "Record was not deleted"

        @allure.title("Change rows amount at page")
        def test_change_rows_amount(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            data = web_table_page.change_rows_amount()
            assert [5, 10, 20, 25, 50, 100] == data, "Rows amount not changed"

    @allure.feature("Buttons page")
    class TestButtons:

        @allure.title("Double click")
        def test_double_click(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button_page.double_click()
            result = button_page.check_status("double")
            assert result is not None, "Double click not worked"

        @allure.title("Right click")
        def test_right_click(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button_page.right_click()
            result = button_page.check_status("right")
            assert result is not None, "Right click not worked"

        @allure.title("Click on dynamic button")
        def test_dynamic_click(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button_page.dynamic_click()
            result = button_page.check_status("dynamic")
            assert result is not None, "Click on dynamic button not worked"

    @allure.feature("Links page")
    class TestLinksPage:

        @allure.title("Open link")
        def test_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            link = links_page.open_new_tab_link()
            assert link == "https://demoqa.com/", "Redirect to wrong links or not open"

    @allure.feature("Upload")
    class TestUploadDownloadPage:

        @allure.title("Upload file")
        def test_upload(self, driver):
            upload_download_page = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            file_name, uploaded_file_name = upload_download_page.upload_file()
            assert file_name == uploaded_file_name, "File was not uploaded"

    @allure.feature("Dynamic properties page")
    class TestDynamicPropertiesPage:

        @allure.title("Enable after 5 seconds button click")
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            is_enable = dynamic_properties_page.enable_button()
            assert is_enable == True, "Button is disabled"

        @allure.title("Text on button change color")
        def test_color_change_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            initial_color = dynamic_properties_page.get_button_text_color()
            color = dynamic_properties_page.wait_for_color_change()
            assert color == 'rgba(220, 53, 69, 1)', "Color not red"
            assert initial_color != color, "Button not change color"

        @allure.title("Wait 5 sec for appear button and click")
        def test_visible_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            is_appear = dynamic_properties_page.visible_button()
            assert is_appear == True, "Button is not appear"
