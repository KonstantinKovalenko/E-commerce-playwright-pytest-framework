import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES

@allure.feature("Cart")
@allure.story("Recommended products")
@allure.title("Add to cart from recommended")
@allure.description("Verify user can add product to cart from recommended items.")

def test_add_to_cart_from_recommended(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.home.scroll_down_to_recommended()

    with allure.step(f'Verify "Recommended" section is visible'):
        expect(app.home.recommended_section).to_be_visible()

    product = app.home.get_product_info(app.home.recommended_items, 3)
    app.home.add_product_to_cart(app.home.button_recommended_add_to_cart, 3)

    app.home.click_modal_view_cart()

    with allure.step(f'Verify URL "{app.cart.PATH}"'):
        expect(app.cart.page).to_have_url(app.cart.PATH)

    app.cart.verify_product(0, product)

    app.cart.remove_all_products()
    app.cart.verify_cart_empty()