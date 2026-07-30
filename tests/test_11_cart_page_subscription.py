import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.titles import TITLES

@allure.feature("Subscript")
@allure.story("Cart page subscription")
@allure.title("Cart page footer subscription")
@allure.description("Verify user can subscript on the footer of the cart page.")

def test_cart_page_footer_subscription(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_cart()

    with allure.step(f'Verify URL "{app.cart.PATH}"'):
        expect(app.cart.page).to_have_url(app.cart.PATH)

    app.footer.scroll_down_to_footer()
    app.footer.verify_subscription_visible()

    email = generate_email()
    app.footer.subscribe(email)

    with allure.step(f'Verify "You have been successfully subscribed!" is visible'):
        expect(app.footer.subscribe_success).to_be_visible()