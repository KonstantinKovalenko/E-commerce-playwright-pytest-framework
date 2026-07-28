from pages.base_page import BasePage
from utils.test_data.payment import TEST_CARD
from pages.locators.checkout.payment_locators import PaymentLocators as L

class PaymentPage(BasePage):
    def verify_loaded(self):
        self.verify_url(L.PATH)

    def click_pay_and_confirm_order(self):
        self.click(
            self.page.locator(L.BUTTON_PAY_CONFIRM_ORDER),
            "Pay and Confirm Order"
        )

    def fill_card_information(self):
        self.fill(self.page.locator(L.INPUT_NAME), TEST_CARD["name"], "Name on Card")
        self.fill(self.page.locator(L.INPUT_CARD_NUMBER), TEST_CARD["number"], "Card Number")
        self.fill(self.page.locator(L.INPUT_CVC), TEST_CARD["cvc"], "CVC")
        self.fill(self.page.locator(L.INPUT_EXPIRE_MONTH), TEST_CARD["e_month"], "Expiration month")
        self.fill(self.page.locator(L.INPUT_EXPIRE_YEAR), TEST_CARD["e_year"], "Expiration year")