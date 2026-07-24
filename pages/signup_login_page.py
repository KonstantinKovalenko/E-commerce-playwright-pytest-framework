from pages.base_page import BasePage

class SignupLoginPage(BasePage):
    PATH = "/login"

    NEW_USER_SIGNUP_TITLE = ".signup-form h2"
    LOGIN_TO_ACCOUNT_TITLE = ".login-form h2"

    SIGNUP_NAME_INPUT = '[data-qa="signup-name"]'
    SIGNUP_EMAIL_INPUT = '[data-qa="signup-email"]'
    SIGNUP_BUTTON = '[data-qa="signup-button"]'

    LOGIN_EMAIL_INPUT = '[data-qa="login-email"]'
    LOGIN_PASSWORD_INPUT = '[data-qa="login-password"]'
    LOGIN_BUTTON = '[data-qa="login-button"]'

    LOGIN_ERROR = 'p:has-text("Your email or password is incorrect!")'
    SIGNUP_ERROR = 'p:has-text("Email Address already exist!")'

    def verify_loaded(self):
        self.verify_title("Automation Exercise - Signup / Login")

    def verify_new_user_signup_visible(self):
        self.verify_visible(
            self.page.locator(self.NEW_USER_SIGNUP_TITLE),
            "New User Signup section"
        )

    def verify_login_to_account_visible(self):
        self.verify_visible(
            self.page.locator(self.LOGIN_TO_ACCOUNT_TITLE),
            "Login to your account section"
        )

    def verify_login_validation_error(self):
        self.verify_text(
            self.page.locator(self.LOGIN_ERROR),
            "Your email or password is incorrect!"
        )

    def verify_email_already_exists_error(self):
        self.verify_text(
            self.page.locator(self.SIGNUP_ERROR),
            "Email Address already exist!"
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

    def login(self, email: str, password: str):
        self.fill(
            self.page.locator(self.LOGIN_EMAIL_INPUT),
            email,
            "Email"
        )

        self.fill(
            self.page.locator(self.LOGIN_PASSWORD_INPUT),
            password,
            "Password"
        )

        self.click(
            self.page.locator(self.LOGIN_BUTTON),
            "Login button"
        )