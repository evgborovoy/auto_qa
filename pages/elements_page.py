import random

from generator.generator import generated_person
from locators.elements_page_locator import TextBoxPageLocators, CheckBoxLocators, RadioButtonLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person = next(generated_person())
        full_name = person.full_name
        email = person.email
        current_address = person.current_address
        permanent_address = person.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
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
        self.element_is_visible(buttons.get(button)).click()

    def get_selected_text(self):
        return self.element_is_present(self.locators.SELECTED_FIELD).text

    def get_no_radio_status(self):
        status = self.element_is_present(self.locators.NO_RADIO).is_enabled()
        return status