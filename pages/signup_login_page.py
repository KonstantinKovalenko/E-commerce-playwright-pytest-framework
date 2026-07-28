from pages.base_page import BasePage
from pages.locators.signup_login_locators import SignupLoginLocators as L

class SignupLoginPage(BasePage):
    def verify_loaded(self):
        self.verify_title("Automation Exercise - Signup / Login")

    def verify_new_user_signup_visible(self):
        self.verify_visible(
            self.page.locator(L.TITLE_NEW_USER_SIGNUP),
            "New User Signup section"
        )

    def verify_login_to_account_visible(self):
        self.verify_visible(
            self.page.locator(L.TITLE_LOGIN_TO_ACCOUNT),
            "Login to your account section"
        )

    def verify_login_validation_error(self):
        self.verify_text(
            self.page.locator(L.LOGIN_ERROR),
            "Your email or password is incorrect!"
        )

    def verify_email_already_exists_error(self):
        self.verify_text(
            self.page.locator(L.SIGNUP_ERROR),
            "Email Address already exist!"
        )

    def signup(self, name: str, email: str):
        self.fill(self.page.locator(L.INPUT_SIGNUP_NAME), name, "Name")
        self.fill(self.page.locator(L.INPUT_SIGNUP_EMAIL), email, "Email")
        self.click(self.page.locator(L.BUTTON_SIGNUP), "Signup button")

    def login(self, email: str, password: str):
        self.fill(self.page.locator(L.INPUT_LOGIN_EMAIL), email, "Email")
        self.fill(self.page.locator(L.INPUT_LOGIN_PASSWORD), password, "Password")
        self.click(self.page.locator(L.BUTTON_LOGIN), "Login button")