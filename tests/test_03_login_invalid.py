import allure

from utils.test_data import INVALID_USER

@allure.feature("User Account")
@allure.story("Unsuccessful login")
@allure.title("Login with invalid credentials")
@allure.description("Verify validation message is displayed after submit login with invalid credentials.")

def test_login_with_invalid_credentials(home_page, signup_login_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_signup_login()

    signup_login_page.verify_login_to_account_visible()

    signup_login_page.login(INVALID_USER["email"], INVALID_USER["password"])

    signup_login_page.verify_login_validation_error()