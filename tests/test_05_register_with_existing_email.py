import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_visible, expect_text

@allure.feature("User Account")
@allure.story("Failed registration")
@allure.title("Register user with an existing email")
@allure.description("Verify that a new user can not be registered using existing email.")

def test_register_user_with_existing_email(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_signup_login()
    expect_visible(app.signup.title_new_user_signup, "New User Signup section")

    app.signup.signup("randomUser", TEST_USER_EMAIL)
    expect_text(app.signup.signup_error, "Email Address already exist!")