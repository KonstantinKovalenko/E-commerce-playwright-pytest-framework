from pages.base_page import BasePage
from playwright.sync_api import Page

class AccountCreatedPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.title_account_created = page.get_by_role("heading", name="Account Created!")
        self.button_continue = page.locator('[data-qa="continue-button"]')

    def click_continue(self):
        self.click(
            self.button_continue,
            "Continue button"
        )