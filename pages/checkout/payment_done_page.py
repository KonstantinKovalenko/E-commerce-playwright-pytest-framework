import allure

from pages.base_page import BasePage
from pathlib import Path

class PaymentDonePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.success_message = page.locator('#form p')
        self.button_continue = page.locator('[data-qa="continue-button"]')
        self.button_download_invoice = page.locator('.check_out')

    def verify_success(self):
        self.verify_text(
            self.success_message,
            "Congratulations! Your order has been confirmed!"
        )

    def click_continue(self):
        self.click(
            self.button_continue,
            "Continue"
        )

    def click_download_invoice(self):
        with self.page.expect_download() as download_info:
            self.click(self.button_download_invoice, "Download Invoice")
 
        download = download_info.value
        Path("assets/downloads").mkdir(exist_ok=True)
        download.save_as("assets/downloads/invoice.txt")

    def verify_file_downloaded(self):
        with allure.step(f'Verify "invoice.txt" exists in "assets/downloads" folder'):
            assert Path("assets/downloads/invoice.txt").exists()