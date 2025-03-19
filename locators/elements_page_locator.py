class TextBoxPageLocators:
    FULL_NAME = ("xpath", "//input[@id='userName']")
    EMAIL = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = ("xpath", "//textarea[@id='permanentAddress']")
    SUBMIT = ("xpath", "//button[@id='submit']")

    CREATED_FULL_NAME = ("xpath", "//p[@id='name']")
    CREATED_EMAIL = ("xpath", "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = ("xpath", "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = ("xpath", "//p[@id='permanentAddress']")


class CheckBoxLocators:
    EXPAND_ALL_BUTTON = ("xpath", "//button[@title='Expand all']")
    ITEM_LIST = ("xpath", "//span[@class='rct-title']")
    SELECTED_ITEMS_FIELD = ("xpath", "//span[@class='text-success']")
    CHECKED_ITEMS = ("css selector", "svg[class='rct-icon rct-icon-check']")


class RadioButtonLocators:
   YES_RADIO = ("xpath", "//label[@for='yesRadio']")
   IMPRESSIVE_RADIO = ("xpath", "//label[@for='impressiveRadio']")
   NO_RADIO = ("xpath", "//input[@id='noRadio']")
   SELECTED_FIELD = ("xpath", "//span[@class='text-success']")

