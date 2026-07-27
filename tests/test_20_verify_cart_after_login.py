import allure

from utils.test_data import SEARCH
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD

@allure.feature("Cart")
@allure.story("Verify cart after login")
@allure.title("Verify cart after user login")
@allure.description("Verify cart do not change after user login.")

def test_verify_cart_after_login(home_page, products_page, cart_page, signup_login_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_products()
    products_page.verify_loaded()

    products_page.search_by_product_name(SEARCH["jeans"])
    products_page.verify_multiple_search_results()

    products_page.add_results_to_cart()

    home_page.header.click_cart()
    cart_page.verify_loaded()

    expected_products = cart_page.get_cart_products()

    home_page.header.click_signup_login()
    signup_login_page.verify_login_to_account_visible()
    signup_login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    home_page.verify_loaded()
    home_page.header.verify_logged_in()

    home_page.header.click_cart()
    cart_page.verify_loaded()

    actual_products = cart_page.get_cart_products()

    cart_page.verify_cart_contents_unchanged(actual_products, expected_products)

    cart_page.remove_all_products()
    cart_page.verify_cart_empty()