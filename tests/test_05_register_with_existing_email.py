import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL
from utils.test_data.titles import TITLES

@allure.feature("User Account")
@allure.story("Failed registration")
@allure.title("Register user with an existing email")
@allure.description("Verify that a new user can not be registered using existing email.")

def test_register_user_with_existing_email(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_signup_login()

    with allure.step(f'Verify "New User Signup" section is visible'):
        expect(app.signup.title_new_user_signup).to_be_visible()

    app.signup.signup("randomUser", TEST_USER_EMAIL)

    app.signup.verify_email_already_exists_error()