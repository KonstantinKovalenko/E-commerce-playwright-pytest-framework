import allure

from playwright.sync_api import expect
from utils.test_data.products import QUANTITY
from utils.test_data.titles import TITLES
from utils.assertions import expect_url, expect_title, expect_text, expect_product

@allure.feature("Cart")
@allure.story("Quantity")
@allure.title("Product quantity in cart")
@allure.description("Verify product quantity in cart.")

def test_product_quantity(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    added_product = app.home.get_product_info(app.home.product_cards, 2)
    app.home.click_view_product(2)
    expect_title(app.product_details.page, TITLES["product_details"])

    app.product_details.set_quantity(QUANTITY["value"])
    app.product_details.click_add_to_cart()
    app.product_details.click_modal_view_cart()
    expect_url(app.cart.page, app.cart.PATH)

    quantity_locator = app.cart.quantity_by_index(0)
    expect_text(quantity_locator, str(QUANTITY["value"]))

    cart_product = app.cart.get_product(0)
    expect_product(cart_product, added_product)

    app.cart.remove_all_products()
    expect_text(app.cart.cart_empty, "Cart is empty!")