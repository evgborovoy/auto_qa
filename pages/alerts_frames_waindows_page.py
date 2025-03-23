import pytest
from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.alerts_frames_windows_locator import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators


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


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def get_frame_info(self, locator):
        frame = self.element_is_present(locator)
        height = frame.get_attribute("height")
        width = frame.get_attribute("width")
        self.switch_to_frame(frame)
        text = self.element_is_present(self.locators.FRAME_TEXT).text
        self.driver.switch_to.default_content()
        return text, width, height

    def check_frame(self, frame_num):
        if frame_num == "frame1":
            return self.get_frame_info(self.locators.BIG_FRAME)
        elif frame_num == "frame2":
            return self.get_frame_info(self.locators.SMALL_FRAME)
        else:
            pytest.fail(f"The frame does not exist")


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def get_frame_text(self, frame_locator, text_locator):
        frame = self.element_is_present(frame_locator)
        self.switch_to_frame(frame)
        text = self.element_is_present(text_locator).text
        return text

    def get_nested_frames_text(self):
        parent_text = self.get_frame_text(self.locators.PARENT_FRAME, self.locators.PARENT_FRAME_TEXT)
        child_text = self.get_frame_text(self.locators.CHILD_FRAME, self.locators.CHILD_FRAME_TEXT)
        self.driver.switch_to.default_content()
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def get_modal_title(self, button_locator, title_locator):
        self.element_is_clickable(button_locator).click()
        title = self.element_is_visible(title_locator).text
        return title

    def get_small_modal_title(self):
        button = self.locators.SMALL_MODAL_BUTTON
        title = self.locators.SMALL_MODAL_TITLE
        return self.get_modal_title(button, title)

    def get_large_modal_title(self):
        button = self.locators.LARGE_MODAL_BUTTON
        title = self.locators.LARGE_MODAL_TITLE
        return self.get_modal_title(button, title)
