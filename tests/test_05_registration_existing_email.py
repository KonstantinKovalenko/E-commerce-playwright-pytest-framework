import allure

from config.settings import TEST_USER_EMAIL

@allure.feature("User Account")
@allure.story("User registration")
@allure.title("Register user with an existing email")
@allure.description("Verify that a new user can not be registered using existing email.")

def test_register_user_with_existing_email(home_page, signup_login_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_signup_login()

    signup_login_page.verify_new_user_signup_visible()

    signup_login_page.signup("randomUser", TEST_USER_EMAIL)

    signup_login_page.verify_email_already_exists_error()