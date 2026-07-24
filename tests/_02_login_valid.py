import allure

from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD

@allure.feature("User Account")
@allure.story("Successful login")
@allure.title("Login with valid credentials")
@allure.description("Verify a user can login with valid username and password.")

def test_login_with_valid_credentials(home_page, signup_login_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_signup_login()

    signup_login_page.verify_login_to_account_visible()

    signup_login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    home_page.verify_loaded()
    home_page.header.verify_logged_in()