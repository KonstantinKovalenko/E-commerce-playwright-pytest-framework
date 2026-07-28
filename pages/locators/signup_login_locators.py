class SignupLoginLocators:
    PATH = "/login"

    TITLE_NEW_USER_SIGNUP = ".signup-form h2"
    TITLE_LOGIN_TO_ACCOUNT = ".login-form h2"

    INPUT_SIGNUP_NAME = '[data-qa="signup-name"]'
    INPUT_SIGNUP_EMAIL = '[data-qa="signup-email"]'
    BUTTON_SIGNUP = '[data-qa="signup-button"]'

    INPUT_LOGIN_EMAIL = '[data-qa="login-email"]'
    INPUT_LOGIN_PASSWORD = '[data-qa="login-password"]'
    BUTTON_LOGIN = '[data-qa="login-button"]'

    LOGIN_ERROR = 'p:has-text("Your email or password is incorrect!")'
    SIGNUP_ERROR = 'p:has-text("Email Address already exist!")'