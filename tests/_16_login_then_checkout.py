import allure

from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD

@allure.feature("Checkout")
@allure.story("Register and checkout")
@allure.title("Register user while checkout")
@allure.description("Verify user can register an account while try to checkout and then complete checkout.")

def test_register_while_checkout(home_page, products_page, cart_page, signup_login_page, checkout_page, payment_page):
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


    signup_login_page.verify_login_to_account_visible()
    signup_login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    home_page.verify_loaded()
    home_page.header.verify_logged_in()


    home_page.header.click_cart()

    cart_page.click_proceed_to_checkout()
    checkout_page.verify_loaded()

    checkout_page.verify_delivery_address2
    checkout_page.verify_product(0, product)
    checkout_page.verify_total_amount()

    checkout_page.add_comment()
    checkout_page.click_place_order()
    payment_page.verify_loaded()

    payment_page.fill_card_information()
    payment_page.click_pay_and_confirm_order()

    payment_page.verify_success()
