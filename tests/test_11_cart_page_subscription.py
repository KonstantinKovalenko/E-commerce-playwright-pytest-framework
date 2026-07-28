import allure

from utils.data_generator import generate_email

@allure.feature("Subscript")
@allure.story("Cart page subscription")
@allure.title("Cart page footer subscription")
@allure.description("Verify user can subscript on the footer of the cart page.")

def test_cart_page_footer_subscription(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_cart()

    app.cart.verify_loaded()

    app.footer.scroll_down_to_footer()
    app.footer.verify_subscription_visible()

    email = generate_email()
    app.footer.subscribe(email)

    app.footer.verify_subscribe_success_visible()