from pages.base_page import BasePage


class SignupLoginPage(BasePage):

    PATH = "/login"

    NEW_USER_SIGNUP_TITLE = ".signup-form h2"
    SIGNUP_NAME_INPUT = '[data-qa="signup-name"]'
    SIGNUP_EMAIL_INPUT = '[data-qa="signup-email"]'
    SIGNUP_BUTTON = '[data-qa="signup-button"]'

    def verify_new_user_signup_visible(self):
        self.verify_visible(
            self.page.locator(self.NEW_USER_SIGNUP_TITLE),
            "New User Signup section"
        )

    def signup(self, name: str, email: str):
        self.fill(
            self.page.locator(self.SIGNUP_NAME_INPUT),
            name,
            "Name"
        )

        self.fill(
            self.page.locator(self.SIGNUP_EMAIL_INPUT),
            email,
            "Email"
        )

        self.click(
            self.page.locator(self.SIGNUP_BUTTON),
            "Signup button"
        )