import allure

from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD

@allure.feature("User Account")
@allure.story("Logout")
@allure.title("Login and then logout")
@allure.description("Verify that a user can log in with valid credentials and then log out successfully.")

def test_logout_after_successful_login(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_signup_login()

    app.signup.verify_login_to_account_visible()

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    app.header.verify_logged_in()

    app.header.click_logout()

    app.signup.verify_loaded()