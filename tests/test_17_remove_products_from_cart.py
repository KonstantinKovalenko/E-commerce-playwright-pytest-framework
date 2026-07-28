import allure

from pages.locators.home_locators import HomeLocators as h_L

@allure.feature("Cart")
@allure.story("Remove products")
@allure.title("Remove products from cart")
@allure.description("Verify products can be removed from cart.")

def test_remove_products_from_cart(app):
    app.home.open()
    app.home.verify_loaded()

    app.home.add_product_to_cart(h_L.BUTTON_ADD_TO_CART, 18)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(h_L.BUTTON_ADD_TO_CART, 19)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(h_L.BUTTON_ADD_TO_CART, 20)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(h_L.BUTTON_ADD_TO_CART, 21)
    app.home.click_modal_view_cart()

    app.cart.verify_loaded()

    app.cart.remove_all_products()

    app.cart.verify_cart_empty()