import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.users import EXISTING_USER
from utils.test_data.titles import TITLES
from utils.assertions import expect_contains, expect_url, expect_title, expect_visible, expect_product, expect_text

@allure.feature("Checkout")
@allure.story("Payment")
@allure.title("Login and then checkout")
@allure.description("Verify user can login and then successfully complete checkout.")

def test_login_then_checkout(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_signup_login()
    expect_visible(app.signup.title_login_to_account, "Login to your account section")

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    expect_title(app.home.page, TITLES["home"])
    expect_visible(app.header.logged_in_user, "Logged in user")

    added_product_1 = app.home.get_product_info(app.home.product_cards, 5)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 5)

    app.home.click_modal_continue_shopping()

    added_product_2 = app.home.get_product_info(app.home.product_cards, 6)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 6)

    app.home.click_modal_view_cart()
    expect_url(app.cart.page, app.cart.PATH)

    app.cart.click_proceed_to_checkout()
    expect_url(app.checkout.page, app.checkout.PATH)

    with allure.step(f"Verify address: {app.checkout.delivery_address}"):
        expect_contains(app.checkout.delivery_address, f'{EXISTING_USER["first_name"]} {EXISTING_USER["last_name"]}')
        expect_contains(app.checkout.delivery_address, EXISTING_USER["address"])
        expect_contains(app.checkout.delivery_address, f'{EXISTING_USER["city"]} {EXISTING_USER["state"]} {EXISTING_USER["zipcode"]}')
        expect_contains(app.checkout.delivery_address, EXISTING_USER["country"])
        expect_contains(app.checkout.delivery_address, EXISTING_USER["mobile"])
            
    checkout_product_1 = app.checkout.get_product(0)
    checkout_product_2 = app.checkout.get_product(1)
    expect_product(checkout_product_1, added_product_1)
    expect_product(checkout_product_2, added_product_2)
    
    calculated_total_amount = app.checkout.calculate_total_amount()
    expect_text(app.checkout.total_amount(), calculated_total_amount)

    app.checkout.add_comment()
    app.checkout.click_place_order()
    expect_url(app.payment.page, app.payment.PATH)

    app.payment.fill_card_information()
    app.payment.click_pay_and_confirm_order()
    expect_text(app.payment_done.success_message, "Congratulations! Your order has been confirmed!")

    app.header.click_logout()
    expect_title(app.signup.page, TITLES["signup"])