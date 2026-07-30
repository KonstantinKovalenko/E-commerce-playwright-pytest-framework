import allure

@allure.feature("Cart")
@allure.story("Recommended products")
@allure.title("Add to cart from recommended")
@allure.description("Verify user can add product to cart from recommended items.")

def test_add_to_cart_from_recommended(app):
    app.home.open()
    app.home.verify_loaded()

    app.home.scroll_down_to_recommended()
    app.home.verify_recommended_visible()

    product = app.home.get_product_info(app.home.recommended_items, 3)
    app.home.add_product_to_cart(app.home.button_recommended_add_to_cart, 3)

    app.home.click_modal_view_cart()
    app.cart.verify_loaded()

    app.cart.verify_product(0, product)

    app.cart.remove_all_products()
    app.cart.verify_cart_empty()