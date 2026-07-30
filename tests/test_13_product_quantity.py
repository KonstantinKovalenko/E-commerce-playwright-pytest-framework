import allure

from playwright.sync_api import expect
from utils.test_data.products import QUANTITY
from utils.test_data.titles import TITLES

@allure.feature("Cart")
@allure.story("Quantity")
@allure.title("Product quantity in cart")
@allure.description("Verify product quantity in cart.")

def test_product_quantity(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    product = app.home.get_product_info(app.home.product_cards, 2)
    app.home.click_view_product(2)

    with allure.step(f'Verify page title "{TITLES['product_details']}"'):
        expect(app.product_details.page).to_have_title(TITLES["product_details"])

    app.product_details.set_quantity(QUANTITY["value"])

    app.product_details.click_add_to_cart()
    app.product_details.click_modal_view_cart()

    with allure.step(f'Verify URL "{app.cart.PATH}"'):
        expect(app.cart.page).to_have_url(app.cart.PATH)

    app.cart.verify_quantity(0, QUANTITY["value"])
    app.cart.verify_product(0, product)

    app.cart.remove_all_products()
    app.cart.verify_cart_empty()