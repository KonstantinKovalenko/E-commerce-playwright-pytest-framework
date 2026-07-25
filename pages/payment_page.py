from pages.base_page import BasePage
from utils.test_data import TEST_CARD

class PaymentPage(BasePage):
    PATH = "/payment"

    NAME_INPUT = '[data-qa="name-on-card"]'
    CARD_NUMBER_INPUT = '[data-qa="card-number"]'
    CVC_INPUT = '[data-qa="cvc"]'
    EXPIRE_MONTH_INPUT = '[data-qa="expiry-month"]'
    EXPIRE_YEAR_INPUT = '[data-qa="expiry-year"]'

    PAY_CONFIRM_ORDER_BUTTON = '[data-qa="pay-button"]'

    SUCCESS_MESSAGE = "#success_message"

    def verify_loaded(self):
        self.verify_url(self.PATH)

    def click_pay_and_confirm_order(self):
        self.click(
            self.page.locator(self.PAY_CONFIRM_ORDER_BUTTON),
            "Pay and Confirm Order"
        )

    def fill_card_information(self):
        self.fill(self.page.locator(self.NAME_INPUT), TEST_CARD["name"], "Name on Card")
        self.fill(self.page.locator(self.CARD_NUMBER_INPUT), TEST_CARD["number"], "Card Number")
        self.fill(self.page.locator(self.CVC_INPUT), TEST_CARD["cvc"], "CVC")
        self.fill(self.page.locator(self.EXPIRE_MONTH_INPUT), TEST_CARD["e_month"], "Expiration month")
        self.fill(self.page.locator(self.EXPIRE_YEAR_INPUT), TEST_CARD["e_year"], "Expiration year")