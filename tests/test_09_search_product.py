import allure

from playwright.sync_api import expect
from utils.test_data.products import SEARCH
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_text

@allure.feature("Products")
@allure.story("Search")
@allure.title("Search products by name")
@allure.description("Verify search product can filter product list.")

def test_search_product(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_products()
    expect_title(app.products.page, TITLES["products"])
    
    app.products.search_by_product_name(SEARCH["product"])
    expect_text(app.products.title_searched_products, "Searched Products")
    expect_text(app.products.first_product_name(), SEARCH["product"])