import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.users import TEST_USER
from utils.test_data.titles import TITLES

@allure.feature("Checkout")
@allure.story("Invoice")
@allure.title("Download invoice after checkout")
@allure.description("Verify user can download an invoice after successful checkout.")

def test_download_invoice(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])
   
    product = app.home.get_product_info(app.home.product_cards, 14)
    app.home.add_product_to_cart(app.home.button_add_to_cart, 14)
    
    app.home.click_modal_view_cart()

    with allure.step(f'Verify URL "{app.cart.PATH}"'):
        expect(app.cart.page).to_have_url(app.cart.PATH)

    app.cart.click_proceed_to_checkout()
    app.cart.click_modal_register_login()

    with allure.step(f'Verify "New User Signup" section is visible'):
        expect(app.signup.title_new_user_signup).to_be_visible()

    email = generate_email()
    app.signup.signup(TEST_USER["name"], email)

    with allure.step(f'Verify "Enter Account Information" section is visible'):
        expect(app.registration.title_account_information).to_be_visible()

    app.registration.fill_account_information(TEST_USER["password"])
    app.registration.fill_address_information()
    app.registration.click_create_account()

    with allure.step(f'Verify Account Created page is visible'):
        expect(app.account_created.title_account_created).to_be_visible()

    app.account_created.click_continue()

    with allure.step(f'Verify "Logged in user" is visible'):
        expect(app.header.logged_in_user).to_be_visible()

    app.header.click_cart()

    app.cart.click_proceed_to_checkout()
    
    with allure.step(f'Verify URL "{app.checkout.PATH}"'):
        expect(app.checkout.page).to_have_url(app.checkout.PATH)

    app.checkout.verify_address(app.checkout.delivery_address, TEST_USER)
    app.checkout.verify_product(0, product)
    app.checkout.verify_total_amount()

    app.checkout.add_comment()
    app.checkout.click_place_order()
    
    with allure.step(f'Verify URL "{app.payment.PATH}"'):
        expect(app.payment.page).to_have_url(app.payment.PATH)

    app.payment.fill_card_information()
    app.payment.click_pay_and_confirm_order()

    app.payment_done.verify_success()

    app.payment_done.click_download_invoice()
    app.payment_done.verify_file_downloaded()

    app.payment_done.click_continue()

    app.header.click_delete_account()

    with allure.step(f'Verify Account Deleted page is visible'):
        expect(app.delete_account.title_account_deleted).to_be_visible()

    app.delete_account.click_continue()