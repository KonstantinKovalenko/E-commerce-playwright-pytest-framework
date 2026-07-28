from pages.base_page import BasePage
from pages.locators.account.delete_account_locators import DeleteAccountLocators as L

class DeleteAccountPage(BasePage):
    def verify_loaded(self):
        self.verify_visible(
            self.page.locator(L.TITLE_ACCOUNT_DELETED),
            "Account Deleted page"
        )

    def click_continue(self):
        self.click(
            self.page.locator(L.BUTTON_CONTINUE),
            "Continue button"
        )