import allure

@allure.feature("Cart")
@allure.story("Remove products")
@allure.title("Remove products from cart")
@allure.description("Verify products can be removed from cart.")

def test_remove_products_from_cart(app):
    app.home.open()
    app.home.verify_loaded()

    app.home.add_product_to_cart(app.home.button_add_to_cart, 18)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(app.home.button_add_to_cart, 19)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(app.home.button_add_to_cart, 20)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(app.home.button_add_to_cart, 21)
    app.home.click_modal_view_cart()

    app.cart.verify_loaded()

    app.cart.remove_all_products()

    app.cart.verify_cart_empty()