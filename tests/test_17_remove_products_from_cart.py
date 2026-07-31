import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES
from utils.assertions import expect_url, expect_title, expect_text

@allure.feature("Cart")
@allure.story("Remove products")
@allure.title("Remove products from cart")
@allure.description("Verify products can be removed from cart.")

def test_remove_products_from_cart(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.home.add_product_to_cart(app.home.button_add_to_cart, 18)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(app.home.button_add_to_cart, 19)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(app.home.button_add_to_cart, 20)
    app.home.click_modal_continue_shopping()

    app.home.add_product_to_cart(app.home.button_add_to_cart, 21)
    app.home.click_modal_view_cart()
    expect_url(app.cart.page, app.cart.PATH)

    app.cart.remove_all_products()
    expect_text(app.cart.cart_empty, "Cart is empty!")