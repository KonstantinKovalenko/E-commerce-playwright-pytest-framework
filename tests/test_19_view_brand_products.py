import allure

from playwright.sync_api import expect
from utils.test_data.products import BRANDS
from utils.test_data.titles import TITLES

@allure.feature("Products")
@allure.story("Brands")
@allure.title("Filter products by brands")
@allure.description("Verify products can be sorted by brands.")

def test_view_brand_products(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_products()
    
    with allure.step(f'Verify page title "{TITLES['products']}"'):
        expect(app.products.page).to_have_title(TITLES["products"])

    with allure.step(f'Verify "Brands filters" section is visible'):
        expect(app.products.brands_filters).to_be_visible()

    app.products.filter_by_brand(BRANDS["polo"])
    app.brand_products.verify_loaded()
    app.brand_products.verify_filtered_title(BRANDS["polo"])
    app.brand_products.verify_products_exist()

    app.brand_products.filter_by_brand(BRANDS["kookie_kids"])
    app.brand_products.verify_filtered_title(BRANDS["kookie_kids"])
    app.brand_products.verify_products_exist()