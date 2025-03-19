class TextBoxPageLocators:
    FULL_NAME = ("xpath", "//input[@id='userName']")
    EMAIL = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = ("xpath", "//textarea[@id='permanentAddress']")
    SUBMIT = ("xpath", "//button[@id='submit']")

    # control panel
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


class WebTableLocators:
    ADD_BUTTON = ("xpath", "//button[@id='addNewRecordButton']")
    SEARCH_FIELD = ("xpath", "//input[@id='searchBox']")

    # row
    DELETE_ROW_BUTTON = ("xpath", "//span[@title='Delete']")
    EDIT_ROW_BUTTON = ("xpath", "//span[@title='Edit']")

    # Add new record form
    FIRSTNAME_FIELD = ("xpath", "//input[@id='firstName']")
    LASTNAME_FIELD = ("xpath", "//input[@id='lastName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    AGE_FIELD = ("xpath", "//input[@id='age']")
    SALARY_FIELD = ("xpath", "//input[@id='salary']")
    DEPARTMENT_FIELD = ("xpath", "//input[@id='department']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

    RECORD_ROWS = ("xpath", "//div[@class='rt-tr-group']")
    ROWS_AMOUNT = ("xpath", "//select[@aria-label='rows per page']")


class ButtonsLocators:
    # buttons
    DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
    DYNAMIC_BUTTON = ("xpath", "//button[text()='Click Me']")

    # control panel
    CONTROL_DOUBLE_CLICK_BUTTON = ("xpath", "//p[@id='doubleClickMessage']")
    CONTROL_RIGHT_CLICK_BUTTON = ("xpath", "//p[@id='rightClickMessage']")
    CONTROL_DYNAMIC_BUTTON = ("xpath", "//p[@id='dynamicClickMessage']")

