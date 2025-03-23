import pytest

from pages.alerts_frames_waindows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage


class TestAlertsFramesWindows:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            expected_text = "This is a sample page"
            tabs_count, text = browser_windows_page.new_tab()
            assert tabs_count > 1, "New tab not open"
            assert text == expected_text, "Wrong tab was opened"

    class TestAlertsPage:

        def test_simple_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_page.open_simple_alert()
            alert_text = alert_page.get_alert_text()
            assert alert_text == "You clicked a button", "Text in alert does not match"

        def test_delayed_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_page.open_delayed_alert()
            alert_text = alert_page.get_alert_text(timeout=10)
            assert alert_text == "This alert appeared after 5 seconds", "Text in alert does not match"

        def test_confirm_alert_accept(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_page.open_confirm_box()
            alert_text = alert_page.get_alert_text()
            assert alert_text == "Do you confirm action?", "Text in alert does not match"

            alert_page.accept_alert()
            result_text = alert_page.get_confirm_result()
            assert result_text == "You selected Ok", "Wrong action in alert"

        def test_confirm_alert_dismiss(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_page.open_confirm_box()
            alert_text = alert_page.get_alert_text()
            assert alert_text == "Do you confirm action?", "Text in alert does not match"

            alert_page.dismiss_alert()
            result_text = alert_page.get_confirm_result()
            assert result_text == "You selected Cancel", "Wrong action in alert"

        def test_prompt_box(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_page.open_prompt_box()
            alert_text = alert_page.get_alert_text()
            assert alert_text == "Please enter your name", "Text in alert does not match"

            text = "John Doe"
            alert_page.send_text_to_prompt(text)
            result_text = alert_page.get_prompt_box_result().split(" ")[2:]  # Убираем лишние слова
            result_text = " ".join(result_text)
            assert result_text == text, "Entered text does not match"

    class TestFramesPage:

        def test_check_frame(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            result_1 = frames_page.check_frame("frame1")
            result_2 = frames_page.check_frame("frame2")
            assert result_1 == ('This is a sample page', '500px', '350px'), "Wrong frame"
            assert result_2 == ('This is a sample page', '100px', '100px'), "Wrong frame"

    class TestNestedFramesPage:

        def test_(self, driver):
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()
            p_text, c_text = nested_frames_page.get_nested_frames_text()
            assert p_text == "Parent frame", "Text in parent frame does not match"
            assert c_text == "Child Iframe", "Text in child frame does not match"