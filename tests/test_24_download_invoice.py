import allure

from utils.data_generator import generate_email
from utils.test_data.users import TEST_USER

@allure.feature("Checkout")
@allure.story("Invoice")
@allure.title("Download invoice after checkout")
@allure.description("Verify user can download an invoice after successful checkout.")

def test_download_invoice(app):
    app.home.open()
    app.home.verify_loaded()
   
    product = app.home.get_product_info(app.home.product_cards, 14)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 14)
    
    app.home.click_modal_view_cart()
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

    app.checkout.verify_address(app.checkout.delivery_address, TEST_USER)
    app.checkout.verify_product(0, product)
    app.checkout.verify_total_amount()

    app.checkout.add_comment()
    app.checkout.click_place_order()
    app.payment.verify_loaded()

    app.payment.fill_card_information()
    app.payment.click_pay_and_confirm_order()

    app.payment_done.verify_success()

    app.payment_done.click_download_invoice()
    app.payment_done.verify_file_downloaded()

    app.payment_done.click_continue()

    app.header.click_delete_account()

    app.delete_account.verify_loaded()
    app.delete_account.click_continue()