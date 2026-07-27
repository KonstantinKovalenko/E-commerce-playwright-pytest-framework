import allure

@allure.feature("Page navigation")
@allure.story("Scroll down and up")
@allure.title("Scroll page down then up")
@allure.description("Verify user can scroll page down and up.")

def test_manual_scroll_down_and_up(home_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.footer.scroll_down_to_footer()
    
    home_page.footer.verify_subscription_visible()

    home_page.header.scroll_up_to_header()

    home_page.verify_carousel_title_visible()