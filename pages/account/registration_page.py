from pages.base_page import BasePage
from utils.test_data.users import TEST_USER

class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.title_account_information = page.get_by_role("heading", name="Enter Account Information")

        self.radio_male = page.locator('#id_gender1')
        self.input_password = page.locator('#password')

        self.select_day = page.locator('#days')
        self.select_month = page.locator('#months')
        self.select_year = page.locator('#years')

        self.checkbox_newsletter = page.locator('#newsletter')
        self.checkbox_special_offers = page.locator('#optin')

        self.input_first_name = page.locator('#first_name')
        self.input_last_name = page.locator('#last_name')
        self.input_address = page.locator('#address1')
        self.input_state = page.locator('#state')
        self.input_city = page.locator('#city')
        self.input_zipcode = page.locator('#zipcode')
        self.input_mobile_number = page.locator('#mobile_number')
        self.select_country = page.locator('#country')
     
        self.button_create_account = page.get_by_role("button", name="Create Account")

    def verify_loaded(self):
        self.verify_visible(
            self.title_account_information,
            "Enter Account Information section"
        )

    def click_create_account(self):
        self.click(
            self.button_create_account,
            "Create Account button"
        )

    def fill_account_information(self, password: str):
        self.click(self.radio_male, "Male radio button")

        self.fill(self.input_password, password, "Password")

        self.select_day.select_option("1")
        self.select_month.select_option("1")
        self.select_year.select_option("1995")

        self.click(self.checkbox_newsletter, "Newsletter checkbox")
        self.click(self.checkbox_special_offers, "Special offers checkbox")

    def fill_address_information(self):
        self.fill(self.input_first_name, TEST_USER["first_name"], "First name")
        self.fill(self.input_last_name, TEST_USER["last_name"], "Last name")
        self.fill(self.input_address, TEST_USER["address"], "Address")

        self.select_country.select_option(TEST_USER["country"])

        self.fill(self.input_state, TEST_USER["state"], "State")
        self.fill(self.input_city, TEST_USER["city"], "City")
        self.fill(self.input_zipcode, TEST_USER["zipcode"], "Zipcode")
        self.fill(self.input_mobile_number, TEST_USER["mobile"], "Mobile number")   