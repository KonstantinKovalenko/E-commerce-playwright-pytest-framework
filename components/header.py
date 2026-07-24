from playwright.sync_api import Page
from pages.base_page import BasePage

class Header(BasePage):
    SIGNUP_LOGIN_BUTTON = 'a[href="/login"]'
    LOGOUT_BUTTON = 'a[href="/logout"]'
    DELETE_ACCOUNT_BUTTON = 'a[href="/delete_account"]'
    LOGGED_IN_USER = 'a:has-text("Logged in as")'

    def __init__(self, page: Page):
        super().__init__(page)

    def click_signup_login(self):
        self.click(
            self.page.locator(self.SIGNUP_LOGIN_BUTTON),
            "Signup / Login button"
        )

    def verify_logged_in(self):
        self.verify_visible(
            self.page.locator(self.LOGGED_IN_USER),
            "Logged in user"
        )

    def click_delete_account(self):
        self.click(
            self.page.locator(self.DELETE_ACCOUNT_BUTTON),
            "Delete Account button"
        )

    def click_logout(self):
        self.click(
            self.page.locator(self.LOGOUT_BUTTON),
            "Logout button"
        )