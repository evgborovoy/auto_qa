import allure

from pages.widgets_page import SliderPage, ProgressBarPage


@allure.suite("Widgets Page")
class TestWidgets:
    @allure.feature("Slider")
    class TestSliderPage:
        @allure.title("Change slider value")
        def test_change_slider_value_drag_and_drop(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, "Value does not change"

    @allure.feature("Progress Bar")
    class TestProgressBar:
        @allure.title("Start progress bar")
        def test_start_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            before, after = progress_bar_page.progress_bar_action()
            assert before != after, "Progress bar not start"

        @allure.title("Complete full progress bar")
        def test_fill_complete(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            is_complete = progress_bar_page.complete_progress_bar()
            assert is_complete, "Progress bar not complete"
