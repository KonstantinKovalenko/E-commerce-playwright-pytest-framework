import allure

from utils.test_data.users import INVALID_USER

@allure.feature("User Account")
@allure.story("Failed Login")
@allure.title("Login with invalid credentials")
@allure.description("Verify validation message is displayed after submit login with invalid credentials.")

def test_login_with_invalid_credentials(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_signup_login()

    app.signup.verify_login_to_account_visible()

    app.signup.login(INVALID_USER["email"], INVALID_USER["password"])

    app.signup.verify_login_validation_error()