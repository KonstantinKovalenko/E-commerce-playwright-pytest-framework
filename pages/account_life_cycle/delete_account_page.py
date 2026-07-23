from pages.base_page import BasePage

class DeleteAccountPage(BasePage):

    ACCOUNT_DELETED_TITLE = '[data-qa="account-deleted"]'
    CONTINUE_BUTTON = '[data-qa="continue-button"]'

    def verify_loaded(self):
        self.verify_visible(
            self.page.locator(self.ACCOUNT_DELETED_TITLE),
            "Account Deleted page"
        )

    def click_continue(self):
        self.click(
            self.page.locator(self.CONTINUE_BUTTON),
            "Continue button"
        )