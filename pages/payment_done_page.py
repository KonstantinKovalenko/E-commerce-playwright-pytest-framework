from pages.base_page import BasePage

class PaymentDonePage(BasePage):
    SUCCESS_MESSAGE = '#form p'

    def verify_success(self):
        self.verify_text(
            self.page.locator(self.SUCCESS_MESSAGE),
            "Congratulations! Your order has been confirmed!"
        )