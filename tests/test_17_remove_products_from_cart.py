import allure

@allure.feature("Cart")
@allure.story("Remove from cart")
@allure.title("Remove products from cart")
@allure.description("Verify products can be removed from cart.")

def test_remove_products_from_cart(home_page, cart_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.add_product_to_cart(home_page.ADD_TO_CART_BUTTON, 18)
    home_page.click_modal_continue_shopping()

    home_page.add_product_to_cart(home_page.ADD_TO_CART_BUTTON, 19)
    home_page.click_modal_continue_shopping()

    home_page.add_product_to_cart(home_page.ADD_TO_CART_BUTTON, 20)
    home_page.click_modal_continue_shopping()

    home_page.add_product_to_cart(home_page.ADD_TO_CART_BUTTON, 21)
    home_page.click_modal_view_cart()

    cart_page.verify_loaded()

    cart_page.remove_all_products()

    cart_page.verify_cart_empty()