import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES

@allure.feature("Products")
@allure.story("Browsing")
@allure.title("All products and product details pages content")
@allure.description("Verify all products and product details pages contain expected content.")

def test_all_products_and_product_detail_content(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_products()

    with allure.step(f'Verify page title "{TITLES['products']}"'):
        expect(app.products.page).to_have_title(TITLES["products"])
    
    app.products.click_first_view_product()

    with allure.step(f'Verify page title "{TITLES['product_details']}"'):
        expect(app.product_details.page).to_have_title(TITLES["product_details"])

    with allure.step(f'Verify "Product name" is visible'):
        expect(app.product_details.product_name).to_be_visible()
    
    app.product_details.verify_product_details_visible()    