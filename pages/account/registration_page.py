from pages.base_page import BasePage
from utils.test_data.users import TEST_USER
from pages.locators.account.registration_locators import RegistrationLocators as L

class RegistrationPage(BasePage):
    def verify_loaded(self):
        self.verify_visible(
            self.page.locator(L.TITLE_ACCOUNT_INFORMATION),
            "Enter Account Information section"
        )

    def click_create_account(self):
        self.click(
            self.page.locator(L.BUTTON_CREATE_ACCOUNT),
            "Create Account button"
        )

    def fill_account_information(self, password: str):
        self.click(self.page.locator(L.RADIO_MALE), "Male radio button")

        self.fill(self.page.locator(L.INPUT_PASSWORD), password, "Password")

        self.page.locator(L.SELECT_DAY).select_option("1")
        self.page.locator(L.SELECT_MONTH).select_option("1")
        self.page.locator(L.SELECT_YEAR).select_option("1995")

        self.click(self.page.locator(L.CHECKBOX_NEWSLETTER), "Newsletter checkbox")
        self.click(self.page.locator(L.CHECKBOX_SPECIAL_OFFERS), "Special offers checkbox")

    def fill_address_information(self):
        self.fill(self.page.locator(L.INPUT_FIRST_NAME), TEST_USER["first_name"], "First name")
        self.fill(self.page.locator(L.INPUT_LAST_NAME), TEST_USER["last_name"], "Last name")
        self.fill(self.page.locator(L.INPUT_ADDRESS), TEST_USER["address"], "Address")

        self.page.locator(L.SELECT_COUNTRY).select_option(TEST_USER["country"])

        self.fill(self.page.locator(L.INPUT_STATE), TEST_USER["state"], "State")
        self.fill(self.page.locator(L.INPUT_CITY), TEST_USER["city"], "City")
        self.fill(self.page.locator(L.INPUT_ZIPCODE), TEST_USER["zipcode"], "Zipcode")
        self.fill(self.page.locator(L.INPUT_MOBILE_NUMBER), TEST_USER["mobile"], "Mobile number")   