import allure

from playwright.sync_api import expect
from utils.test_data.users import INVALID_USER
from utils.test_data.titles import TITLES

@allure.feature("User Account")
@allure.story("Failed Login")
@allure.title("Login with invalid credentials")
@allure.description("Verify validation message is displayed after submit login with invalid credentials.")

def test_login_with_invalid_credentials(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_signup_login()

    with allure.step(f'Verify "Login to your account" section is visible'):
        expect(app.signup.title_login_to_account).to_be_visible()

    app.signup.login(INVALID_USER["email"], INVALID_USER["password"])

    app.signup.verify_login_validation_error()