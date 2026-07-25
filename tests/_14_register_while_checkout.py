import allure

from utils.data_generator import generate_email
from utils.test_data import TEST_USER

@allure.feature("Checkout")
@allure.story("Register while checkout")
@allure.title("Register user while checkout")
@allure.description("Verify user can register an account while try to checkout and then complete checkout.")

def test_register_while_checkout(home_page, products_page, cart_page, signup_login_page, checkout_page, payment_page, payment_done_page, registration_page, account_created_page, delete_account_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_products()
    products_page.verify_loaded()
    
    product = products_page.get_product_info(3)
    products_page.hover_over_product(3)
    products_page.add_product_to_cart(3)
    
    products_page.click_modal_view_cart()
    cart_page.verify_loaded()

    cart_page.click_proceed_to_checkout()
    cart_page.click_modal_register_login()

    signup_login_page.verify_new_user_signup_visible()

    email = generate_email()
    signup_login_page.signup(TEST_USER["name"], email)

    registration_page.verify_loaded()

    registration_page.fill_account_information(TEST_USER["password"])
    registration_page.fill_address_information()
    registration_page.click_create_account()

    account_created_page.verify_loaded()
    account_created_page.click_continue()

    home_page.header.verify_logged_in()

    home_page.header.click_cart()

    cart_page.click_proceed_to_checkout()
    checkout_page.verify_loaded()

    checkout_page.verify_delivery_address()
    checkout_page.verify_product(0, product)
    checkout_page.verify_total_amount()

    checkout_page.add_comment()
    checkout_page.click_place_order()
    payment_page.verify_loaded()

    payment_page.fill_card_information()
    payment_page.click_pay_and_confirm_order()

    payment_done_page.verify_success()

    home_page.header.click_delete_account()

    delete_account_page.verify_loaded()
    delete_account_page.click_continue()