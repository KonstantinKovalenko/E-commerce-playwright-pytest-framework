import allure

from utils.test_data.products import BRANDS

@allure.feature("Products")
@allure.story("Brands")
@allure.title("Filter products by brands")
@allure.description("Verify products can be sorted by brands.")

def test_view_brand_products(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_products()
    app.products.verify_loaded()

    app.products.verify_brands_visible()

    app.products.filter_by_brand(BRANDS["polo"])
    app.brand_products.verify_loaded()
    app.brand_products.verify_filtered_title(BRANDS["polo"])
    app.brand_products.verify_products_exist()

    app.brand_products.filter_by_brand(BRANDS["kookie_kids"])
    app.brand_products.verify_filtered_title(BRANDS["kookie_kids"])
    app.brand_products.verify_products_exist()