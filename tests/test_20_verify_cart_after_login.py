import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.products import SEARCH
from utils.test_data.titles import TITLES

@allure.feature("Cart")
@allure.story("Persistence")
@allure.title("Verify cart after user login")
@allure.description("Verify cart do not change after user login.")

def test_verify_cart_after_login(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_products()

    with allure.step(f'Verify page title "{TITLES['products']}"'):
        expect(app.products.page).to_have_title(TITLES["products"])

    app.products.search_by_product_name(SEARCH["jeans"])
    app.products.verify_multiple_search_results()

    app.products.add_results_to_cart()

    app.header.click_cart()

    with allure.step(f'Verify URL "{app.cart.PATH}"'):
        expect(app.cart.page).to_have_url(app.cart.PATH)

    expected_products = app.cart.get_cart_products()

    app.header.click_signup_login()

    with allure.step(f'Verify "Login to your account" section is visible'):
        expect(app.signup.title_login_to_account).to_be_visible()

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    with allure.step(f'Verify "Logged in user" is visible'):
        expect(app.header.logged_in_user).to_be_visible()

    app.header.click_cart()

    with allure.step(f'Verify URL "{app.cart.PATH}"'):
        expect(app.cart.page).to_have_url(app.cart.PATH)

    actual_products = app.cart.get_cart_products()

    app.cart.verify_cart_contents_unchanged(actual_products, expected_products)

    app.cart.remove_all_products()
    app.cart.verify_cart_empty()