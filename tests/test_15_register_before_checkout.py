import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.users import TEST_USER
from utils.test_data.titles import TITLES
from utils.assertions import expect_contains, expect_url, expect_title, expect_visible, expect_product, expect_text

@allure.feature("Checkout")
@allure.story("Registered checkout")
@allure.title("Register user before checkout")
@allure.description("Verify user can register an account and then complete checkout.")

def test_register_before_checkout(app):
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
  
    added_product = app.home.get_product_info(app.home.product_cards, 9)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 9)
    
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

    checkout_product = app.checkout.get_product(0)
    expect_product(checkout_product, added_product)

    calculated_total_amount = app.checkout.calculate_total_amount()
    expect_text(app.checkout.total_amount(), calculated_total_amount)

    app.checkout.add_comment()
    app.checkout.click_place_order()
    expect_url(app.payment.page, app.payment.PATH)

    app.payment.fill_card_information()
    app.payment.click_pay_and_confirm_order()
    expect_text(app.payment_done.success_message, "Congratulations! Your order has been confirmed!")

    app.header.click_delete_account()
    expect_visible(app.delete_account.title_account_deleted, "Account Deleted page")

    app.delete_account.click_continue()