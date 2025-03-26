import random
import time

from pages.base_page import BasePage
from locators.widgets_page_locators import SliderPageLocators, ProgressBarLocators


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def _get_slider_value(self):
        value = self.element_is_present(self.locators.SLIDER).get_attribute("value")
        return value

    def _change_slider_value_by_drag_and_drop(self):
        slider = self.element_is_visible(self.locators.SLIDER)
        self.element_drag_and_drop(slider, random.randint(20, 50), 0)

    def change_slider_value(self):
        before = self._get_slider_value()
        self._change_slider_value_by_drag_and_drop()
        after = self._get_slider_value()
        return before, after



class ProgressBarPage(BasePage):
    locators = ProgressBarLocators()

    def _start_progress_bar(self):
        self.element_is_clickable(self.locators.START_BUTTON).click()

    def _get_progress_info(self):
        return self.element_is_present(self.locators.PROGRESS_INDICATOR).text

    def progress_bar_action(self):
        self._start_progress_bar()
        time.sleep(random.randint(1, 5))
        value = self._get_progress_info()
        return value

    def complete_progress_bar(self):
        self._start_progress_bar()
        time.sleep(11)
        after = self._get_progress_info()
        if after == "100%":
            return True
        return False
