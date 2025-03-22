class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = ("xpath", "//button[@id='tabButton']")
    NEW_TAB_TEXT = ("xpath", "//h1[@id='sampleHeading']")


class AlertsPageLocators:
    SIMPLE_ALERT_BUTTON = ("xpath", "//button[@id='alertButton']")
    TIMER_ALERT_BUTTON = ("xpath", "//button[@id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = ("xpath", "//button[@id='confirmButton']")
    CONFIRM_RESULT = ("xpath", "//span[@id='confirmResult']")
    PROMPT_ALERT_BUTTON = ("xpath", "//button[@id='promtButton']")
    PROMPT_RESULT = ("xpath", "//span[@id='promptResult']")

class FramesPageLocators:
    BIG_FRAME = ("xpath", "//iframe[@id='frame1']")
    SMALL_FRAME = ("xpath", "//iframe[@id='frame2']")
    FRAME_TEXT = ("xpath", "//h1[@id='sampleHeading']")
