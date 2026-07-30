import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.titles import TITLES

@allure.feature("User Account")
@allure.story("Login")
@allure.title("Login with valid credentials")
@allure.description("Verify a user can login with valid username and password.")

def test_login_with_valid_credentials(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_signup_login()

    with allure.step(f'Verify "Login to your account" section is visible'):
        expect(app.signup.title_login_to_account).to_be_visible()

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    with allure.step(f'Verify "Logged in user" is visible'):
        expect(app.header.logged_in_user).to_be_visible()