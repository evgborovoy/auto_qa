import pytest
from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.alerts_frames_windows_locator import BrowserWindowsPageLocators, AlertsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        tabs_count = len(self.driver.window_handles)
        self.switch_to_window(-1)
        text = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return tabs_count, text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def open_simple_alert(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT_BUTTON).click()

    def open_delayed_alert(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()

    def open_confirm_box(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()

    def get_confirm_result(self):
        return self.element_is_present(self.locators.CONFIRM_RESULT).text

    def open_prompt_box(self):
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()

    def get_prompt_box_result(self):
        return self.element_is_present(self.locators.PROMPT_RESULT).text

    def get_alert_text(self, timeout=10):
        try:
            alert = self.get_alert(timeout=timeout)
            return alert.text
        except TimeoutException:
            pytest.fail(f"Alert did not open within {timeout} seconds")

    def accept_alert(self):
        alert = self.get_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.get_alert()
        alert.dismiss()

    def send_text_to_prompt(self, text):
        alert = self.get_alert()
        alert.send_keys(text)
        alert.accept()
