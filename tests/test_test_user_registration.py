import allure

from utils.data_generator import generate_email
from utils.test_data import TEST_USER


@allure.feature("User Account")
@allure.story("Register User")
@allure.title("Register and delete user account")
@allure.description(
    "Verify that a new user can register, "
    "create an account, and delete the account successfully."
)

def test_register_and_delete_user_account(home_page, signup_login_page, registration_page, account_created_page, delete_account_page):

    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_signup_login()

    signup_login_page.verify_new_user_signup_visible()

    email = generate_email()
    allure.dynamic.parameter("email", email)

    signup_login_page.signup(TEST_USER["name"], email)

    registration_page.verify_loaded()

    registration_page.fill_account_information(TEST_USER["password"])
    registration_page.fill_address_information()
    registration_page.click_create_account()

    account_created_page.verify_loaded()
    account_created_page.click_continue()

    home_page.header.verify_logged_in()

    home_page.header.click_delete_account()

    delete_account_page.verify_loaded()
    delete_account_page.click_continue()