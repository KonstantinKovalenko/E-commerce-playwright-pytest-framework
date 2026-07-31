import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES
from utils.assertions import expect_contains, expect_title, expect_visible

@allure.feature("Products")
@allure.story("Browsing")
@allure.title("All products and product details pages content")
@allure.description("Verify all products and product details pages contain expected content.")

def test_all_products_and_product_detail_content(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_products()
    expect_title(app.products.page, TITLES["products"])
    
    app.products.click_first_view_product()
    expect_title(app.product_details.page, TITLES["product_details"])

    expect_visible(app.product_details.product_name, "Product name")
    expect_contains(app.product_details.category, "Category:")
    expect_contains(app.product_details.price, "Rs.")
    expect_contains(app.product_details.availability, "Availability:")
    expect_contains(app.product_details.condition, "Condition:")
    expect_contains(app.product_details.brand, "Brand:")