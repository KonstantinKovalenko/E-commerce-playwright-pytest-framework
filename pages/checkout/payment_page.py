from pages.base_page import BasePage
from utils.test_data.payment import TEST_CARD

class PaymentPage(BasePage):
    PATH = "/payment"

    def __init__(self, page: Page):
        super().__init__(page)

        self.input_name = page.locator('[data-qa="name-on-card"]')
        self.input_card_number = page.locator('[data-qa="card-number"]')
        self.input_cvc = page.locator('[data-qa="cvc"]')
        self.input_expire_month = page.locator('[data-qa="expiry-month"]')
        self.input_expire_year = page.locator('[data-qa="expiry-year"]')

        self.button_pay_confirm_order = page.locator('[data-qa="pay-button"]')

    def verify_loaded(self):
        self.verify_url(self.PATH)

    def click_pay_and_confirm_order(self):
        self.click(
            self.button_pay_confirm_order,
            "Pay and Confirm Order"
        )

    def fill_card_information(self):
        self.fill(self.input_name, TEST_CARD["name"], "Name on Card")
        self.fill(self.input_card_number, TEST_CARD["number"], "Card Number")
        self.fill(self.input_cvc, TEST_CARD["cvc"], "CVC")
        self.fill(self.input_expire_month, TEST_CARD["e_month"], "Expiration month")
        self.fill(self.input_expire_year, TEST_CARD["e_year"], "Expiration year")