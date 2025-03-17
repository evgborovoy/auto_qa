from pages.elements_page import TextBoxPage


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
