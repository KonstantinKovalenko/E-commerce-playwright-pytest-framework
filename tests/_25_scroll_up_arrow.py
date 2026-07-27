import allure

@allure.feature("Page elements")
@allure.story("Scroll up arrow")
@allure.title("Scroll up arrow functionality")
@allure.description("Verify user can faster scroll up using Arrow Up button.")

def test_scroll_up_using_arrow(home_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.footer.scroll_down_to_footer()
    
    home_page.footer.verify_subscription_visible()

    home_page.click_scroll_up()

    home_page.verify_carousel_title_visible()