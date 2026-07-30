import allure

from playwright.sync_api import expect
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data.users import EXISTING_USER
from utils.test_data.titles import TITLES

@allure.feature("Checkout")
@allure.story("Payment")
@allure.title("Login and then checkout")
@allure.description("Verify user can login and then successfully complete checkout.")

def test_login_then_checkout(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_signup_login()

    with allure.step(f'Verify "Login to your account" section is visible'):
        expect(app.signup.title_login_to_account).to_be_visible()

    app.signup.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    with allure.step(f'Verify "Logged in user" is visible'):
        expect(app.header.logged_in_user).to_be_visible()

    product_1 = app.home.get_product_info(app.home.product_cards, 5)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 5)

    app.home.click_modal_continue_shopping()

    product_2 = app.home.get_product_info(app.home.product_cards, 6)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 6)

    app.home.click_modal_view_cart()
    
    with allure.step(f'Verify URL "{app.cart.PATH}"'):
        expect(app.cart.page).to_have_url(app.cart.PATH)

    app.cart.click_proceed_to_checkout()
    
    with allure.step(f'Verify URL "{app.checkout.PATH}"'):
        expect(app.checkout.page).to_have_url(app.checkout.PATH)

    app.checkout.verify_address(app.checkout.delivery_address, EXISTING_USER)
    app.checkout.verify_product(0, product_1)
    app.checkout.verify_product(1, product_2)
    app.checkout.verify_total_amount()

    app.checkout.add_comment()
    app.checkout.click_place_order()

    with allure.step(f'Verify URL "{app.payment.PATH}"'):
        expect(app.payment.page).to_have_url(app.payment.PATH)

    app.payment.fill_card_information()
    app.payment.click_pay_and_confirm_order()

    app.payment_done.verify_success()

    app.header.click_logout()

    with allure.step(f'Verify page title "{TITLES['signup']}"'):
        expect(app.signup.page).to_have_title(TITLES["signup"])