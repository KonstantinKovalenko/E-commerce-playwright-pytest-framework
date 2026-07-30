import allure

from playwright.sync_api import expect
from utils.test_data.products import SEARCH
from utils.test_data.titles import TITLES

@allure.feature("Products")
@allure.story("Search")
@allure.title("Search products by name")
@allure.description("Verify search product can filter product list.")

def test_search_product(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_products()

    with allure.step(f'Verify page title "{TITLES['products']}"'):
        expect(app.products.page).to_have_title(TITLES["products"])
    
    app.products.search_by_product_name(SEARCH["product"])

    app.products.verify_search_result(SEARCH["product"])