import allure

from utils.data_generator import generate_email

@allure.feature("Subscription")
@allure.story("Subscription")
@allure.title("Home page footer subscription")
@allure.description("Verify user can subscript on the footer of the home page.")

def test_home_page_footer_subscription(home_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.footer.scroll_down_to_footer()
    
    home_page.footer.verify_subscription_visible()

    email = generate_email()
    home_page.footer.subscribe(email)

    home_page.footer.verify_subscribe_success_visible()