import allure

from utils.data_generator import generate_email

@allure.feature("Subscription")
@allure.story("Subscription")
@allure.title("Cart page footer subscription")
@allure.description("Verify user can subscript on the footer of the cart page.")

def test_cart_page_footer_subscription(home_page, cart_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_cart()

    cart_page.verify_loaded()

    cart_page.footer.scroll_down_to_footer()
    
    cart_page.footer.verify_subscription_visible()

    email = generate_email()
    cart_page.footer.subscribe(email)

    cart_page.footer.verify_subscribe_success_visible()