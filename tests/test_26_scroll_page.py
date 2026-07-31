import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_text

@allure.feature("Navigation")
@allure.story("Manual scrolling")
@allure.title("Scroll page down then up")
@allure.description("Verify user can scroll page down and up.")

def test_manual_scroll_down_and_up(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.footer.scroll_down_to_footer()
    expect_text(app.footer.title_subscription, "Subscription")

    app.header.scroll_up_to_header()
    expect_text(app.home.first_carousel_slide(), "Full-Fledged practice website for Automation Engineers")