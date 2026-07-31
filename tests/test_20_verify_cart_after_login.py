import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.products import SEARCH
from utils.test_data.titles import TITLES
from utils.assertions import expect_url, expect_title, expect_visible, expect_text, expect_greater_than, expect_equal

@allure.feature("Cart")
@allure.story("Persistence")
@allure.title("Verify cart after user login")
@allure.description("Verify cart do not change after user login.")

def test_verify_cart_after_login(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_products()
    expect_title(app.products.page, TITLES["products"])

    app.products.search_by_product_name(SEARCH["jeans"])
    count = app.products.get_products_count()
    expect_greater_than(count, 0, "search returned products")

    app.products.add_results_to_cart()

    app.header.click_cart()
    expect_url(app.cart.page, app.cart.PATH)

    expected_products = app.cart.get_cart_products()

    app.header.click_signup_login()
    expect_visible(app.signup.title_login_to_account, "Login to your account section")

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    expect_title(app.home.page, TITLES["home"])
    expect_visible(app.header.logged_in_user, "Logged in user")

    app.header.click_cart()
    expect_url(app.cart.page, app.cart.PATH)

    actual_products = app.cart.get_cart_products()
    expect_equal(actual_products, expected_products, "cart contents remain unchanged after login")

    app.cart.remove_all_products()
    expect_text(app.cart.cart_empty, "Cart is empty!")