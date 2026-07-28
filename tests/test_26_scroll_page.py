import allure

@allure.feature("Navigation")
@allure.story("Manual scrolling")
@allure.title("Scroll page down then up")
@allure.description("Verify user can scroll page down and up.")

def test_manual_scroll_down_and_up(app):
    app.home.open()
    app.home.verify_loaded()

    app.footer.scroll_down_to_footer()
    
    app.footer.verify_subscription_visible()

    app.header.scroll_up_to_header()

    app.home.verify_carousel_title_visible()