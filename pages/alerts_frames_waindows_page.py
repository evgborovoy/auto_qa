from pages.base_page import BasePage
from locators.alerts_frames_windows_locator import BrowserWindowsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        tabs_count = len(self.driver.window_handles)
        self.switch_to_window(-1)
        text = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return tabs_count, text
