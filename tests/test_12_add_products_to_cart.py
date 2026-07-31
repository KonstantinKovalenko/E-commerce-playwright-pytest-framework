import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES
from utils.assertions import expect_url, expect_title, expect_product, expect_text

@allure.feature("Cart")
@allure.story("Add products")
@allure.title("Add products to cart")
@allure.description("Verify products can be added to cart and cart page will contain added products.")

def test_add_products_to_cart(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_products()
    expect_title(app.products.page, TITLES["products"])
    
    added_product_1 = app.products.get_product_info(0)
    app.products.hover_over_product(0)
    app.products.add_product_to_cart(0)

    app.products.click_modal_continue_shopping()

    added_product_2 = app.products.get_product_info(1)
    app.products.hover_over_product(1)
    app.products.add_product_to_cart(1)

    app.products.click_modal_view_cart()
    expect_url(app.cart.page, app.cart.PATH)

    cart_product_1 = app.cart.get_product(0)
    cart_product_2 = app.cart.get_product(1)
    expect_product(cart_product_1, added_product_1)
    expect_product(cart_product_2, added_product_2)

    app.cart.remove_all_products()
    expect_text(app.cart.cart_empty, "Cart is empty!")