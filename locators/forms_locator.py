import random


class PracticeFormPageLocators:
    FIRSTNAME_FIELD = ("xpath", "//input[@id='firstName']")
    LASTNAME_FIELD = ("xpath", "//input[@id='lastName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    GENDER_RADIO = ("xpath", f"//label[@for='gender-radio-{random.randint(1, 3)}']")
    MOBILE_FIELD = ("xpath", "//input[@id='userNumber']")
    DOB_FIELD = ("xpath", "//input[@id='dateOfBirthInput']")
    SUBJECT_FIELD = ("xpath", "//input[@id='subjectsInput']")
    HOBBIES_CHECKBOX = ("xpath", f"//label[@for='hobbies-checkbox-{random.randint(1, 3)}']")
    UPLOAD_PICTURE = ("xpath", "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
    STATE = ("xpath", "//input[@id='react-select-3-input']")
    STATE_SELECT = ("xpath", "//div[@id='state']")
    CITY = ("xpath", "//input[@id='react-select-4-input']")
    CITY_SELECT = ("xpath", "//div[@id='city']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

    RESULT_TABLE = ("xpath", "//div[@class='table-responsive']//td[2]")
