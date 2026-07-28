import allure

from config.settings import TEST_USER_EMAIL

@allure.feature("User Account")
@allure.story("Failed registration")
@allure.title("Register user with an existing email")
@allure.description("Verify that a new user can not be registered using existing email.")

def test_register_user_with_existing_email(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_signup_login()

    app.signup.verify_new_user_signup_visible()

    app.signup.signup("randomUser", TEST_USER_EMAIL)

    app.signup.verify_email_already_exists_error()