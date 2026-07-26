import allure

from utils.test_data import BRANDS

@allure.feature("Categories")
@allure.story("Products categories")
@allure.title("Filter products by brands")
@allure.description("Verify products can be sorted by brands.")

def test_view_brand_products(home_page, products_page, brand_products_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_products()
    products_page.verify_loaded()

    products_page.verify_brands_visible()

    products_page.filter_by_brand(BRANDS["polo"])
    brand_products_page.verify_loaded()
    brand_products_page.verify_filtered_title(BRANDS["polo"])
    brand_products_page.verify_products_exist()

    brand_products_page.filter_by_brand(BRANDS["kookie_kids"])
    brand_products_page.verify_filtered_title(BRANDS["kookie_kids"])
    brand_products_page.verify_products_exist()