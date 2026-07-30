import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.users import TEST_USER
from utils.test_data.titles import TITLES

@allure.feature("User Account")
@allure.story("Registration")
@allure.title("Register and delete user account")
@allure.description("Verify that a new user can register, create an account and delete the account successfully.")

def test_register_and_delete_user_account(app):
    app.home.open()

    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_signup_login()

    with allure.step(f'Verify "New User Signup" section is visible'):
        expect(app.signup.title_new_user_signup).to_be_visible()

    email = generate_email()
  
    app.signup.signup(TEST_USER["name"], email)

    with allure.step(f'Verify "Enter Account Information" section is visible'):
        expect(app.registration.title_account_information).to_be_visible()

    app.registration.fill_account_information(TEST_USER["password"])
    app.registration.fill_address_information()
    app.registration.click_create_account()

    with allure.step(f'Verify Account Created page is visible'):
        expect(app.account_created.title_account_created).to_be_visible()

    app.account_created.click_continue()

    with allure.step(f'Verify "Logged in user" is visible'):
        expect(app.header.logged_in_user).to_be_visible()

    app.header.click_delete_account()

    with allure.step(f'Verify Account Deleted page is visible'):
        expect(app.delete_account.title_account_deleted).to_be_visible()

    app.delete_account.click_continue()