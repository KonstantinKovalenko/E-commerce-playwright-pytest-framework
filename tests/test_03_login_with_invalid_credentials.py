import allure

from playwright.sync_api import expect
from utils.test_data.users import INVALID_USER
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_visible, expect_text

@allure.feature("User Account")
@allure.story("Failed Login")
@allure.title("Login with invalid credentials")
@allure.description("Verify validation message is displayed after submit login with invalid credentials.")

def test_login_with_invalid_credentials(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_signup_login()
    expect_visible(app.signup.title_login_to_account, "Login to your account section")

    app.signup.login(INVALID_USER["email"], INVALID_USER["password"])
    expect_text(app.signup.login_error, "Your email or password is incorrect!")