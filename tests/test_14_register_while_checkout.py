import allure

from utils.data_generator import generate_email
from utils.test_data.users import TEST_USER
from pages.locators.checkout.checkout_locators import CheckoutLocators as c_L

@allure.feature("Checkout")
@allure.story("Guest checkout")
@allure.title("Register user while checkout")
@allure.description("Verify user can register an account while try to checkout and then complete checkout.")

def test_register_while_checkout(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_products()
    app.products.verify_loaded()
    
    product = app.products.get_product_info(3)
    app.products.hover_over_product(3)
    app.products.add_product_to_cart(3)
    
    app.products.click_modal_view_cart()
    app.cart.verify_loaded()

    app.cart.click_proceed_to_checkout()
    app.cart.click_modal_register_login()

    app.signup.verify_new_user_signup_visible()

    email = generate_email()
    app.signup.signup(TEST_USER["name"], email)

    app.registration.verify_loaded()

    app.registration.fill_account_information(TEST_USER["password"])
    app.registration.fill_address_information()
    app.registration.click_create_account()

    app.account_created.verify_loaded()
    app.account_created.click_continue()

    app.header.verify_logged_in()

    app.header.click_cart()

    app.cart.click_proceed_to_checkout()
    app.checkout.verify_loaded()

    app.checkout.verify_address(c_L.DELIVERY_ADDRESS, TEST_USER)
    app.checkout.verify_product(0, product)
    app.checkout.verify_total_amount()

    app.checkout.add_comment()
    app.checkout.click_place_order()
    app.payment.verify_loaded()

    app.payment.fill_card_information()
    app.payment.click_pay_and_confirm_order()

    app.payment_done.verify_success()

    app.header.click_delete_account()

    app.delete_account.verify_loaded()
    app.delete_account.click_continue()