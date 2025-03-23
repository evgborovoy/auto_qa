import os
import random

import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select

from generator.generator import generated_person, generate_file
from locators.elements_page_locator import *
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person = next(generated_person())
        full_name = person.full_name
        email = person.email
        current_address = person.current_address
        permanent_address = person.permanent_address
        with allure.step(f"Input {full_name}"):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        with allure.step(f"Input {email}"):
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
        with allure.step(f"Input {current_address}"):
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        with allure.step(f"Input {permanent_address}"):
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step("Click Submit button"):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_info(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxLocators()

    @allure.step("Open full list")
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_on_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = random.randint(7, 10)
        while count != 0:
            item = item_list[random.randint(1, 16)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for item in checked_list:
            item_title = item.find_element("xpath", ".//ancestor::span[@class='rct-text']")
            data.append(item_title.text.split(".")[0].replace(" ", "").lower())
        return data

    def get_items_from_filed(self):
        items = self.elements_are_present(self.locators.SELECTED_ITEMS_FIELD)
        res = []
        for item in items:
            res.append(item.text.lower())
        return res


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_on_radio(self, button):
        buttons = {
            "yes": self.locators.YES_RADIO,
            "impressive": self.locators.IMPRESSIVE_RADIO,
        }
        with allure.step(f"Click on {button}"):
            self.element_is_visible(buttons.get(button)).click()

    def get_selected_text(self):
        return self.element_is_present(self.locators.SELECTED_FIELD).text

    def get_no_radio_status(self):
        status = self.element_is_present(self.locators.NO_RADIO).is_enabled()
        return status


class WebTablePage(BasePage):
    locators = WebTableLocators()

    def add_record(self):
        person_data = next(generated_person())
        first_name = person_data.first_name
        last_name = person_data.last_name
        email = person_data.email
        age = person_data.age
        salary = person_data.salary
        department = person_data.department
        with allure.step(f"Click on Add button"):
            self.element_is_visible(self.locators.ADD_BUTTON).click()
        with allure.step(f"Input {first_name}"):
            self.element_is_visible(self.locators.FIRSTNAME_FIELD).send_keys(first_name)
        with allure.step(f"Input {last_name}"):
            self.element_is_visible(self.locators.LASTNAME_FIELD).send_keys(last_name)
        with allure.step(f"Input {email}"):
            self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        with allure.step(f"Input {age}"):
            self.element_is_visible(self.locators.AGE_FIELD).send_keys(age)
        with allure.step(f"Input {salary}"):
            self.element_is_visible(self.locators.SALARY_FIELD).send_keys(salary)
        with allure.step(f"Input {department}"):
            self.element_is_visible(self.locators.DEPARTMENT_FIELD).send_keys(department)
        with allure.step(f"Click on Submit button"):
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return first_name, last_name, str(age), email, str(salary), department

    def check_records_list(self):
        records_list = self.elements_are_present(self.locators.RECORD_ROWS)
        data = []
        for item in records_list:
            data.append(item.text.split("\n"))
        return data

    def search_record(self, search_arg):
        self.element_is_present(self.locators.SEARCH_FIELD).send_keys(search_arg)

    def edit_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        with allure.step("Click on edit button"):
            self.element_is_visible(self.locators.EDIT_ROW_BUTTON).click()
        self.element_is_visible(self.locators.AGE_FIELD).clear()
        with allure.step(f"Input {age}"):
            self.element_is_visible(self.locators.AGE_FIELD).send_keys(age)
        with allure.step("Click on Submit button"):
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step("Click on Delete button")
    def delete_row(self):
        self.element_is_visible(self.locators.DELETE_ROW_BUTTON).click()

    def change_rows_amount(self):
        options = [5, 10, 20, 25, 50, 100]
        data = []
        row_amount_field = self.element_is_present(self.locators.ROWS_AMOUNT)
        self.go_to_element(row_amount_field)
        dropdown = Select(row_amount_field)
        for option in options:
            dropdown.select_by_value(str(option))
            self.go_to_element(row_amount_field)
            data.append(len(self.check_records_list()))
        return data


class ButtonsPage(BasePage):
    locators = ButtonsLocators()

    def double_click(self):
        self.action_double_click(self.locators.DOUBLE_CLICK_BUTTON)

    def right_click(self):
        self.action_right_click(self.locators.RIGHT_CLICK_BUTTON)

    def dynamic_click(self):
        self.element_is_visible(self.locators.DYNAMIC_BUTTON).click()

    def check_status(self, action="right"):
        actions = {
            "double": self.locators.CONTROL_DOUBLE_CLICK_BUTTON,
            "right": self.locators.CONTROL_RIGHT_CLICK_BUTTON,
            "dynamic": self.locators.CONTROL_DYNAMIC_BUTTON,
        }
        return self.element_is_present(actions.get(action))


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def open_new_tab_link(self):
        self.element_is_visible(self.locators.LINK).click()
        self.switch_to_window(-1)
        url = self.driver.current_url
        return url


class UploadDownloadPage(BasePage):
    locators = UploadDownloadLocators()

    def upload_file(self):
        file_name, path = generate_file()
        self.element_is_visible(self.locators.UPLOAD).send_keys(path)
        uploaded_path = self.element_is_visible(self.locators.UPLOADED_PATH).text
        os.remove(path)
        return file_name.split("/")[-1], uploaded_path.split("\\")[-1]


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True

    def get_button_text_color(self):
        button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        return button.value_of_css_property("color")

    def wait_for_color_change(self):
        initial_color = self.get_button_text_color()

        def color_changed(driver):
            current_color = self.get_button_text_color()
            return current_color != initial_color

        self.wait_event(color_changed)
        return self.get_button_text_color()

    def visible_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True
