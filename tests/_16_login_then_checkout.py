import allure

from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data import EXISTING_USER

@allure.feature("Checkout")
@allure.story("Login and checkout")
@allure.title("Login and then checkout")
@allure.description("Verify user can login and then successfully complete checkout.")

def test_register_while_checkout(home_page, products_page, cart_page, signup_login_page, checkout_page, payment_page, payment_done_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_signup_login()

    signup_login_page.verify_login_to_account_visible()
    signup_login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    home_page.verify_loaded()
    home_page.header.verify_logged_in()

    product1 = home_page.get_product_info(home_page.PRODUCT_CARDS, 5)
    home_page.add_product_to_cart(home_page.ADD_TO_CART_BUTTON, 5)

    home_page.click_modal_continue_shopping()

    product2 = home_page.get_product_info(home_page.PRODUCT_CARDS, 6)
    home_page.add_product_to_cart(home_page.ADD_TO_CART_BUTTON, 6)

    home_page.click_modal_view_cart()
    cart_page.verify_loaded()

    cart_page.click_proceed_to_checkout()
    checkout_page.verify_loaded()

    checkout_page.verify_address(checkout_page.DELIVERY_ADDRESS, EXISTING_USER)
    checkout_page.verify_product(0, product_1)
    checkout_page.verify_product(1, product_2)
    checkout_page.verify_total_amount()

    checkout_page.add_comment()
    checkout_page.click_place_order()
    payment_page.verify_loaded()

    payment_page.fill_card_information()
    payment_page.click_pay_and_confirm_order()

    payment_done_page.verify_success()

    home_page.header.click_logout()

    signup_login_page.verify_loaded()