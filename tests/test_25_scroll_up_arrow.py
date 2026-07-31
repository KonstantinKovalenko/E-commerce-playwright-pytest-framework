import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_text

@allure.feature("Navigation")
@allure.story("Scrolling elements")
@allure.title("Scroll up arrow functionality")
@allure.description("Verify user can faster scroll up using Arrow Up button.")

def test_scroll_up_using_arrow(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.footer.scroll_down_to_footer()
    expect_text(app.footer.title_subscription, "Subscription")

    app.home.click_scroll_up()
    expect_text(app.home.first_carousel_slide(), "Full-Fledged practice website for Automation Engineers")