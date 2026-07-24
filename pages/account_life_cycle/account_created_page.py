from pages.base_page import BasePage

class AccountCreatedPage(BasePage):
    ACCOUNT_CREATED_TITLE = '[data-qa="account-created"]'
    CONTINUE_BUTTON = '[data-qa="continue-button"]'

    def verify_loaded(self):
        self.verify_visible(
            self.page.locator(self.ACCOUNT_CREATED_TITLE),
            "Account Created page"
        )

    def click_continue(self):
        self.click(
            self.page.locator(self.CONTINUE_BUTTON),
            "Continue button"
        )