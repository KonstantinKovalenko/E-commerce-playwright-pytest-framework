import allure
import re

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.assertions import expect_title, expect_visible
from utils.test_data.users import TEST_USER
from utils.test_data.titles import TITLES

@allure.feature("User Account")
@allure.story("Registration")
@allure.title("Register and delete user account")
@allure.description("Verify that a new user can register, create an account and delete the account successfully.")

def test_register_and_delete_user_account(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])
 
    app.header.click_signup_login()
    expect_visible(app.signup.title_new_user_signup, "New User Signup section")

    email = generate_email()
    app.signup.signup(TEST_USER["name"], email)
    expect_visible(app.registration.title_account_information, "Enter Account Information section")

    app.registration.fill_account_information(TEST_USER["password"])
    app.registration.fill_address_information()
    app.registration.click_create_account()
    expect_visible(app.account_created.title_account_created, "Account Created page")

    app.account_created.click_continue()
    expect_visible(app.header.logged_in_user, "Logged in user")

    app.header.click_delete_account()
    expect_visible(app.delete_account.title_account_deleted, "Account Deleted page")

    app.delete_account.click_continue()