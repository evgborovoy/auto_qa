from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver: WebDriver = driver
        self.url: str = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator: (str, str), timeout: float = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: (str, str), timeout: float = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator: (str, str), timeout: float = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator: (str, str), timeout: float = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator: (str, str), timeout: float = 10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator: (str, str), timeout: float = 10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_event(self, event, timeout=5):
        return WebDriverWait(self.driver, timeout).until(event)

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, locator):
        element = self.element_is_visible(locator)
        self.go_to_element(element)
        actions = ActionChains(self.driver)
        actions.double_click(element)
        actions.perform()

    def action_right_click(self, locator):
        element = self.element_is_visible(locator)
        self.go_to_element(element)
        actions = ActionChains(self.driver)
        actions.context_click(element)
        actions.perform()

    def switch_to_window(self, tab):
        """tab: input window index (-1 for last opened tab)"""
        tabs = self.driver.window_handles
        # Usually new tab is last tab
        if 0 <= abs(tab) < len(tabs):
            self.driver.switch_to.window(tabs[tab])
        else:
            raise IndexError("No such tab index")

    def get_alert(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    def switch_to_frame(self, element):
        return self.driver.switch_to.frame(element)

    def element_drag_and_drop(self, element, x_coordinate, y_coordinate):
        action = ActionChains(self.driver)
        action.click_and_hold()
        action.pause(0.2)
        action.drag_and_drop_by_offset(element, x_coordinate, y_coordinate)
        action.pause(0.2)
        action.release()
        action.perform()
