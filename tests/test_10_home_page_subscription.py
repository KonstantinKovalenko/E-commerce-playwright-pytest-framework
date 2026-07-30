import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.titles import TITLES

@allure.feature("Subscript")
@allure.story("Home page subscription")
@allure.title("Home page footer subscription")
@allure.description("Verify user can subscript on the footer of the home page.")

def test_home_page_footer_subscription(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.footer.scroll_down_to_footer()

    app.footer.verify_subscription_visible()

    email = generate_email()
    app.footer.subscribe(email)

    with allure.step(f'Verify "You have been successfully subscribed!" is visible'):
        expect(app.footer.subscribe_success).to_be_visible()