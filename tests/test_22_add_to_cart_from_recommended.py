import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES
from utils.assertions import expect_url, expect_title, expect_visible, expect_text, expect_product

@allure.feature("Cart")
@allure.story("Recommended products")
@allure.title("Add to cart from recommended")
@allure.description("Verify user can add product to cart from recommended items.")

def test_add_to_cart_from_recommended(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.home.scroll_down_to_recommended()
    expect_visible(app.home.recommended_section, "Recommended section")

    added_product = app.home.get_product_info(app.home.recommended_items, 3)
    app.home.add_product_to_cart(app.home.button_recommended_add_to_cart, 3)

    app.home.click_modal_view_cart()
    expect_url(app.cart.page, app.cart.PATH)

    cart_product = app.cart.get_product(0)
    expect_product(cart_product, added_product)

    app.cart.remove_all_products()
    expect_text(app.cart.cart_empty, "Cart is empty!")