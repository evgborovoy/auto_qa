from pages.alerts_frames_waindows_page import BrowserWindowsPage


class TestAlertsFramesWindows:
    class TestBrowserWindows:
       def test_new_tab(self, driver):
           browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
           browser_windows_page.open()
           tabs_count, text = browser_windows_page.new_tab()
           assert tabs_count > 1, "New tab not open"
           assert text == "This is a sample page", "Wrong tab was opened"
