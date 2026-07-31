import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_visible, expect_text

@allure.feature("Subscript")
@allure.story("Home page subscription")
@allure.title("Home page footer subscription")
@allure.description("Verify user can subscript on the footer of the home page.")

def test_home_page_footer_subscription(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.footer.scroll_down_to_footer()
    expect_text(app.footer.title_subscription, "Subscription")

    email = generate_email()
    app.footer.subscribe(email)
    expect_visible(app.footer.subscribe_success, "You have been successfully subscribed!")