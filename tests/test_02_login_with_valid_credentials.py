import allure

from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD

@allure.feature("User Account")
@allure.story("Login")
@allure.title("Login with valid credentials")
@allure.description("Verify a user can login with valid username and password.")

def test_login_with_valid_credentials(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_signup_login()

    app.signup.verify_login_to_account_visible()

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    app.home.verify_loaded()
    app.header.verify_logged_in()