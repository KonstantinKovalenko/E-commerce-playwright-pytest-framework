from pages.base_page import BasePage

class SignupLoginPage(BasePage):
    PATH = "/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.title_new_user_signup = page.get_by_role("heading", name="New User Signup!")
        self.title_login_to_account = page.get_by_role("heading", name="Login to your account")

        self.input_signup_name = page.locator('[data-qa="signup-name"]')
        self.input_signup_email = page.locator('[data-qa="signup-email"]')
        self.button_signup = page.locator('[data-qa="signup-button"]')

        self.input_login_email = page.locator('[data-qa="login-email"]')
        self.input_login_password = page.locator('[data-qa="login-password"]')
        self.button_login = page.locator('[data-qa="login-button"]')

        self.login_error = page.get_by_text("Your email or password is incorrect!")
        self.signup_error = page.get_by_text("Email Address already exist!")

    def verify_loaded(self):
        self.verify_title("Automation Exercise - Signup / Login")

    def verify_new_user_signup_visible(self):
        self.verify_visible(
            self.title_new_user_signup,
            "New User Signup section"
        )

    def verify_login_to_account_visible(self):
        self.verify_visible(
            self.title_login_to_account,
            "Login to your account section"
        )

    def verify_login_validation_error(self):
        self.verify_text(
            self.login_error,
            "Your email or password is incorrect!"
        )

    def verify_email_already_exists_error(self):
        self.verify_text(
            self.signup_error,
            "Email Address already exist!"
        )

    def signup(self, name: str, email: str):
        self.fill(self.input_signup_name, name, "Name")
        self.fill(self.input_signup_email, email, "Email")
        self.click(self.button_signup, "Signup button")

    def login(self, email: str, password: str):
        self.fill(self.input_login_email, email, "Email")
        self.fill(self.input_login_password, password, "Password")
        self.click(self.button_login, "Login button")