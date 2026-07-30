import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES

@allure.feature("Cart")
@allure.story("Add products")
@allure.title("Add products to cart")
@allure.description("Verify products can be added to cart and cart page will contain added products.")

def test_add_products_to_cart(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_products()
    
    with allure.step(f'Verify page title "{TITLES['products']}"'):
        expect(app.products.page).to_have_title(TITLES["products"])
    
    product_1 = app.products.get_product_info(0)
    app.products.hover_over_product(0)
    app.products.add_product_to_cart(0)

    app.products.click_modal_continue_shopping()

    product_2 = app.products.get_product_info(1)
    app.products.hover_over_product(1)
    app.products.add_product_to_cart(1)

    app.products.click_modal_view_cart()

    with allure.step(f'Verify URL "{app.cart.PATH}"'):
        expect(app.cart.page).to_have_url(app.cart.PATH)

    app.cart.verify_product(0, product_1)
    app.cart.verify_product(1, product_2)

    app.cart.remove_all_products()
    app.cart.verify_cart_empty()