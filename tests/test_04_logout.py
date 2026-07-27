import allure

from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD

@allure.feature("User Account")
@allure.story("Successful logout")
@allure.title("Login and then logout")
@allure.description("Verify that a user can log in with valid credentials and then log out successfully.")

def test_logout_after_successful_login(home_page, signup_login_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_signup_login()

    signup_login_page.verify_login_to_account_visible()

    signup_login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    home_page.header.verify_logged_in()

    home_page.header.click_logout()

    signup_login_page.verify_loaded()