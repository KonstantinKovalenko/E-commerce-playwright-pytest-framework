import allure

from utils.data_generator import generate_email
from utils.test_data.users import TEST_USER

@allure.feature("Checkout")
@allure.story("Address verification")
@allure.title("Verify delivery and billing address")
@allure.description("Verify delivery and billing address match entered data during registration.")

def test_verify_address_details(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_signup_login()
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
  
    product = app.home.get_product_info(app.home.product_cards, 12)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 12)
    
    app.home.click_modal_view_cart()
    app.cart.verify_loaded()

    app.cart.click_proceed_to_checkout()
    app.checkout.verify_loaded()

    app.checkout.verify_address(app.checkout.delivery_address, TEST_USER)
    app.checkout.verify_address(app.checkout.billing_address, TEST_USER)

    app.header.click_delete_account()

    app.delete_account.verify_loaded()
    app.delete_account.click_continue()