import allure

@allure.feature("Cart")
@allure.story("Add to cart")
@allure.title("Add to cart from recommended")
@allure.description("Verify user can add product to cart from recommended items.")

def test_add_to_cart_from_recommended(home_page, cart_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.scroll_down_to_recommended()
    home_page.verify_recommended_visible()

    product = home_page.get_product_info(home_page.RECOMMENDED_ITEMS, 3)
    home_page.add_product_to_cart(home_page.RECOMMENDED_ADD_TO_CART_BUTTON, 3)

    home_page.click_modal_view_cart()
    cart_page.verify_loaded()

    cart_page.verify_product(0, product)

    cart_page.remove_all_products()
    cart_page.verify_cart_empty()