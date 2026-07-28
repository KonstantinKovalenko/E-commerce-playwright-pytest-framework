import allure

from utils.test_data.products import SEARCH

@allure.feature("Products")
@allure.story("Search")
@allure.title("Search products by name")
@allure.description("Verify search product can filter product list.")

def test_search_product(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_products()

    app.products.verify_loaded()
    
    app.products.search_by_product_name(SEARCH["product"])

    app.products.verify_search_result(SEARCH["product"])