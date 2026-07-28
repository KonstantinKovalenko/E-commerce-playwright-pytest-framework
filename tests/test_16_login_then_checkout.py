import allure

from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.users import EXISTING_USER
from pages.locators.home_locators import HomeLocators as h_L
from pages.locators.checkout.checkout_locators import CheckoutLocators as c_L
@allure.feature("Checkout")
@allure.story("Payment")
@allure.title("Login and then checkout")
@allure.description("Verify user can login and then successfully complete checkout.")

def test_login_then_checkout(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_signup_login()

    app.signup.verify_login_to_account_visible()
    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    app.home.verify_loaded()
    app.header.verify_logged_in()

    product_1 = app.home.get_product_info(h_L.PRODUCT_CARDS, 5)
    app.home.add_product_to_cart(h_L.BUTTON_ADD_TO_CART, 5)

    app.home.click_modal_continue_shopping()

    product_2 = app.home.get_product_info(h_L.PRODUCT_CARDS, 6)
    app.home.add_product_to_cart(h_L.BUTTON_ADD_TO_CART, 6)

    app.home.click_modal_view_cart()
    app.cart.verify_loaded()

    app.cart.click_proceed_to_checkout()
    app.checkout.verify_loaded()

    app.checkout.verify_address(c_L.DELIVERY_ADDRESS, EXISTING_USER)
    app.checkout.verify_product(0, product_1)
    app.checkout.verify_product(1, product_2)
    app.checkout.verify_total_amount()

    app.checkout.add_comment()
    app.checkout.click_place_order()
    app.payment.verify_loaded()

    app.payment.fill_card_information()
    app.payment.click_pay_and_confirm_order()

    app.payment_done.verify_success()

    app.header.click_logout()

    app.signup.verify_loaded()