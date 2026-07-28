import allure

@allure.feature("Navigation")
@allure.story("Scrolling elements")
@allure.title("Scroll up arrow functionality")
@allure.description("Verify user can faster scroll up using Arrow Up button.")

def test_scroll_up_using_arrow(app):
    app.home.open()
    app.home.verify_loaded()

    app.footer.scroll_down_to_footer()
    
    app.footer.verify_subscription_visible()

    app.home.click_scroll_up()

    app.home.verify_carousel_title_visible()