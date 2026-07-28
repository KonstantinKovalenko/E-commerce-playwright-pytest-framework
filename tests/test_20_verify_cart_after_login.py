import allure

from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.products import SEARCH

@allure.feature("Cart")
@allure.story("Persistence")
@allure.title("Verify cart after user login")
@allure.description("Verify cart do not change after user login.")

def test_verify_cart_after_login(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_products()
    app.products.verify_loaded()

    app.products.search_by_product_name(SEARCH["jeans"])
    app.products.verify_multiple_search_results()

    app.products.add_results_to_cart()

    app.header.click_cart()
    app.cart.verify_loaded()

    expected_products = app.cart.get_cart_products()

    app.header.click_signup_login()
    app.signup.verify_login_to_account_visible()
    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    app.home.verify_loaded()
    app.header.verify_logged_in()

    app.header.click_cart()
    app.cart.verify_loaded()

    actual_products = app.cart.get_cart_products()

    app.cart.verify_cart_contents_unchanged(actual_products, expected_products)

    app.cart.remove_all_products()
    app.cart.verify_cart_empty()