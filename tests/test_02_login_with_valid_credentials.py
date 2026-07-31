import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_visible

@allure.feature("User Account")
@allure.story("Login")
@allure.title("Login with valid credentials")
@allure.description("Verify a user can login with valid username and password.")

def test_login_with_valid_credentials(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_signup_login()
    expect_visible(app.signup.title_login_to_account, "Login to your account section")

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    expect_title(app.home.page, TITLES["home"])
    expect_visible(app.header.logged_in_user, "Logged in user")