import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES

@allure.feature("Navigation")
@allure.story("Manual scrolling")
@allure.title("Scroll page down then up")
@allure.description("Verify user can scroll page down and up.")

def test_manual_scroll_down_and_up(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.footer.scroll_down_to_footer()
    
    app.footer.verify_subscription_visible()

    app.header.scroll_up_to_header()

    app.home.verify_carousel_title_visible()