

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
