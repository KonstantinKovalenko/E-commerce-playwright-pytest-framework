import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.users import TEST_USER
from utils.test_data.titles import TITLES
from utils.assertions import expect_contains, expect_url, expect_title, expect_visible

@allure.feature("Checkout")
@allure.story("Address verification")
@allure.title("Verify delivery and billing address")
@allure.description("Verify delivery and billing address match entered data during registration.")

def test_verify_address_details(app):
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
  
    product = app.home.get_product_info(app.home.product_cards, 12)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 12)
    
    app.home.click_modal_view_cart()
    expect_url(app.cart.page, app.cart.PATH)

    app.cart.click_proceed_to_checkout()
    expect_url(app.checkout.page, app.checkout.PATH)

    with allure.step(f"Verify address: {app.checkout.delivery_address}"):
        expect_contains(app.checkout.delivery_address, f'{TEST_USER["first_name"]} {TEST_USER["last_name"]}')
        expect_contains(app.checkout.delivery_address, TEST_USER["address"])
        expect_contains(app.checkout.delivery_address, f'{TEST_USER["city"]} {TEST_USER["state"]} {TEST_USER["zipcode"]}')
        expect_contains(app.checkout.delivery_address, TEST_USER["country"])
        expect_contains(app.checkout.delivery_address, TEST_USER["mobile"])

    with allure.step(f"Verify address: {app.checkout.billing_address}"):
        expect_contains(app.checkout.billing_address, f'{TEST_USER["first_name"]} {TEST_USER["last_name"]}')
        expect_contains(app.checkout.billing_address, TEST_USER["address"])
        expect_contains(app.checkout.billing_address, f'{TEST_USER["city"]} {TEST_USER["state"]} {TEST_USER["zipcode"]}')
        expect_contains(app.checkout.billing_address, TEST_USER["country"])
        expect_contains(app.checkout.billing_address, TEST_USER["mobile"])

    app.header.click_delete_account()
    expect_visible(app.delete_account.title_account_deleted, "Account Deleted page")

    app.delete_account.click_continue()