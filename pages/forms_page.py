from selenium.webdriver.common.keys import Keys

from generator.generator import generated_person, generate_file
from locators.forms_locator import PracticeFormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()

    def fill_form(self):
        person = next(generated_person())
        file_name, path = generate_file()
        self.element_is_visible(self.locators.FIRSTNAME_FIELD).send_keys(person.first_name)
        self.element_is_visible(self.locators.LASTNAME_FIELD).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_RADIO).click()
        self.element_is_visible(self.locators.MOBILE_FIELD).send_keys(person.phone)
        self.element_is_visible(self.locators.SUBJECT_FIELD).send_keys("bio")
        self.element_is_visible(self.locators.SUBJECT_FIELD).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX).click()
        self.element_is_present(self.locators.UPLOAD_PICTURE).send_keys(path)
        current_address = self.element_is_visible(self.locators.CURRENT_ADDRESS)
        self.go_to_element(current_address)
        current_address.send_keys(person.current_address)
        self.go_to_element(self.element_is_present(self.locators.STATE_SELECT))
        self.element_is_visible(self.locators.STATE_SELECT).click()
        self.element_is_visible(self.locators.STATE).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CITY_SELECT).click()
        self.element_is_visible(self.locators.CITY).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person

    def get_info_from_table(self):
        result = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result:
            data.append(item.text)
        return data
