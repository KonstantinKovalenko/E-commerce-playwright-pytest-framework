from pages.base_page import BasePage

class DeleteAccountPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.title_account_deleted = page.get_by_role("heading", name="Account Deleted!")
        self.button_continue = page.locator('[data-qa="continue-button"]')

    def verify_loaded(self):
        self.verify_visible(
            self.title_account_deleted,
            "Account Deleted page"
        )

    def click_continue(self):
        self.click(
            self.button_continue,
            "Continue button"
        )