from pages.base_page import BasePage
from utils.test_data import TEST_USER

class RegistrationPage(BasePage):
    ACCOUNT_INFORMATION_TITLE = 'h2:has-text("Enter Account Information")'

    MALE_RADIO = "#id_gender1"
    PASSWORD_INPUT = "#password"

    DAY_SELECT = "#days"
    MONTH_SELECT = "#months"
    YEAR_SELECT = "#years"

    NEWSLETTER_CHECKBOX = "#newsletter"
    SPECIAL_OFFERS_CHECKBOX = "#optin"

    FIRST_NAME_INPUT = "#first_name"
    LAST_NAME_INPUT = "#last_name"
    ADDRESS_INPUT = "#address1"
    COUNTRY_SELECT = "#country"
    STATE_INPUT = "#state"
    CITY_INPUT = "#city"
    ZIPCODE_INPUT = "#zipcode"
    MOBILE_NUMBER_INPUT = "#mobile_number"

    CREATE_ACCOUNT_BUTTON = '[data-qa="create-account"]'

    def verify_loaded(self):
        self.verify_visible(
            self.page.locator(self.ACCOUNT_INFORMATION_TITLE),
            "Enter Account Information section"
        )

    def fill_account_information(self, password: str):
        self.click(self.page.locator(self.MALE_RADIO), "Male radio button")

        self.fill(self.page.locator(self.PASSWORD_INPUT), password, "Password")

        self.page.locator(self.DAY_SELECT).select_option("1")
        self.page.locator(self.MONTH_SELECT).select_option("1")
        self.page.locator(self.YEAR_SELECT).select_option("1995")

        self.click(self.page.locator(self.NEWSLETTER_CHECKBOX), "Newsletter checkbox")
        self.click(self.page.locator(self.SPECIAL_OFFERS_CHECKBOX), "Special offers checkbox")

    def fill_address_information(self):
        self.fill(self.page.locator(self.FIRST_NAME_INPUT), TEST_USER["first_name"], "First name")
        self.fill(self.page.locator(self.LAST_NAME_INPUT), TEST_USER["last_name"], "Last name")
        self.fill(self.page.locator(self.ADDRESS_INPUT), TEST_USER["address"], "Address")

        self.page.locator(self.COUNTRY_SELECT).select_option(TEST_USER["country"])

        self.fill(self.page.locator(self.STATE_INPUT), TEST_USER["state"], "State")
        self.fill(self.page.locator(self.CITY_INPUT), TEST_USER["city"], "City")
        self.fill(self.page.locator(self.ZIPCODE_INPUT), TEST_USER["zipcode"], "Zipcode")
        self.fill(self.page.locator(self.MOBILE_NUMBER_INPUT), TEST_USER["mobile"], "Mobile number")

    def click_create_account(self):
        self.click(
            self.page.locator(self.CREATE_ACCOUNT_BUTTON),
            "Create Account button"
        )

    def wait_for_timeout(self, timeout: int):
        self.page.wait_for_timeout(5000)