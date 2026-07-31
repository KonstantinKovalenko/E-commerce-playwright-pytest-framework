import allure

from playwright.sync_api import expect
from utils.test_data.products import BRANDS
from utils.test_data.titles import TITLES
from utils.assertions import expect_url_contains, expect_title, expect_visible, expect_text, expect_greater_than

@allure.feature("Products")
@allure.story("Brands")
@allure.title("Filter products by brands")
@allure.description("Verify products can be sorted by brands.")

def test_view_brand_products(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_products()
    expect_title(app.products.page, TITLES["products"])
    expect_visible(app.products.brands_filters, "Brands filters section")

    app.products.filter_by_brand(BRANDS["polo"])
    expect_url_contains(app.brand_products.page, app.brand_products.PATH)
    expect_text(app.brand_products.title_filtered_products, f'Brand - {BRANDS["polo"]} Products')

    count = app.brand_products.get_products_count()
    expect_greater_than(count, 0, "brand products are displayed")

    app.brand_products.filter_by_brand(BRANDS["kookie_kids"])
    expect_text(app.brand_products.title_filtered_products, f'Brand - {BRANDS["kookie_kids"]} Products')

    count = app.brand_products.get_products_count()
    expect_greater_than(count, 0, "brand products are displayed")