import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_visible

@allure.feature("User Account")
@allure.story("Logout")
@allure.title("Login and then logout")
@allure.description("Verify that a user can log in with valid credentials and then log out successfully.")

def test_logout_after_successful_login(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_signup_login()
    expect_visible(app.signup.title_login_to_account, "Login to your account section")

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    expect_visible(app.header.logged_in_user, "Logged in user")

    app.header.click_logout()
    expect_title(app.signup.page, TITLES["signup"])