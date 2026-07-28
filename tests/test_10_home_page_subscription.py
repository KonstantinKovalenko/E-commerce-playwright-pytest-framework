import allure

from utils.data_generator import generate_email

@allure.feature("Subscript")
@allure.story("Home page subscription")
@allure.title("Home page footer subscription")
@allure.description("Verify user can subscript on the footer of the home page.")

def test_home_page_footer_subscription(app):
    app.home.open()
    app.home.verify_loaded()

    app.footer.scroll_down_to_footer()
    app.footer.verify_subscription_visible()

    email = generate_email()
    app.footer.subscribe(email)

    app.footer.verify_subscribe_success_visible()