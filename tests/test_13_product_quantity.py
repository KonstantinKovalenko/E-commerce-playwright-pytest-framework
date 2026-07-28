import allure

from utils.test_data.products import QUANTITY
from pages.locators.home_locators import HomeLocators as h_L

@allure.feature("Cart")
@allure.story("Quantity")
@allure.title("Product quantity in cart")
@allure.description("Verify product quantity in cart.")

def test_product_quantity(app):
    app.home.open()
    app.home.verify_loaded()

    product = app.home.get_product_info(h_L.PRODUCT_CARDS, 2)
    app.home.click_view_product(2)

    app.product_details.verify_loaded()

    app.product_details.set_quantity(QUANTITY["value"])

    app.product_details.click_add_to_cart()
    app.product_details.click_modal_view_cart()

    app.cart.verify_loaded()

    app.cart.verify_quantity(0, QUANTITY["value"])
    app.cart.verify_product(0, product)

    app.cart.remove_all_products()
    app.cart.verify_cart_empty()