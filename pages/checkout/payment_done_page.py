import allure

from pages.base_page import BasePage
from pathlib import Path
from pages.locators.checkout.payment_done_locators import PaymentDoneLocators as L

class PaymentDonePage(BasePage):
    def verify_success(self):
        self.verify_text(
            self.page.locator(L.SUCCESS_MESSAGE),
            "Congratulations! Your order has been confirmed!"
        )

    def click_continue(self):
        self.click(
            self.page.locator(L.BUTTON_CONTINUE),
            "Continue"
        )

    def click_download_invoice(self):
        with self.page.expect_download() as download_info:
            self.click(self.page.locator(L.BUTTON_DOWNLOAD_INVOICE), "Download Invoice")
 
        download = download_info.value
        Path("assets/downloads").mkdir(exist_ok=True)
        download.save_as("assets/downloads/invoice.txt")

    def verify_file_downloaded(self):
        with allure.step(f'Verify "invoice.txt" exists in "assets/downloads" folder'):
            assert Path("assets/downloads/invoice.txt").exists()