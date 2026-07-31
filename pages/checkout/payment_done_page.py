import allure

from pages.base_page import BasePage
from playwright.sync_api import Page
from pathlib import Path

class PaymentDonePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.success_message = page.locator('#form p')
        self.button_continue = page.locator('[data-qa="continue-button"]')
        self.button_download_invoice = page.locator('.check_out')

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

    def invoice_file(self):
        return Path("assets/downloads/invoice.txt")