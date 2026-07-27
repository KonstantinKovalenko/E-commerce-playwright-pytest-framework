import allure

from pages.base_page import BasePage
from pathlib import Path

class PaymentDonePage(BasePage):
    SUCCESS_MESSAGE = '#form p'

    CONTINUE_BUTTON = '[data-qa="continue-button"]'
    DOWNLOAD_INVOICE_BUTTON = ".check_out"

    def verify_success(self):
        self.verify_text(
            self.page.locator(self.SUCCESS_MESSAGE),
            "Congratulations! Your order has been confirmed!"
        )

    def click_download_invoice(self):
        with self.page.expect_download() as download_info:
            self.click(self.page.locator(self.DOWNLOAD_INVOICE_BUTTON), "Download Invoice")
 
        download = download_info.value
        Path("downloads").mkdir(exist_ok=True)
        download.save_as("downloads/invoice.txt")

    def click_continue(self):
        self.click(self.page.locator(self.CONTINUE_BUTTON), "Continue")

    def verify_file_downloaded(self):
        with allure.step(f'Verify "invoice.txt" exists in "downloads" folder'):
            assert Path("downloads/invoice.txt").exists()