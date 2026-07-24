import allure

from utils.test_data import SEARCH

@allure.feature("Products")
@allure.story("Search products")
@allure.title("Search products by name")
@allure.description("Verify search product can filter product list.")

def test_search_product(home_page, products_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_products()

    products_page.verify_loaded()
    
    products_page.search_by_product_name(SEARCH["product"])

    products_page.verify_search_result(SEARCH["product"])