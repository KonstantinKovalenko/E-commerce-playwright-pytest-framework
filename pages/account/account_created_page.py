from pages.base_page import BasePage
from pages.locators.account.account_created_locators import AccountCreatedLocators as L

class AccountCreatedPage(BasePage):
    def verify_loaded(self):
        self.verify_visible(
            self.page.locator(L.TITLE_ACCOUNT_CREATED),
            "Account Created page"
        )

    def click_continue(self):
        self.click(
            self.page.locator(L.BUTTON_CONTINUE),
            "Continue button"
        )