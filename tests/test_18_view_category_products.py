import allure

from playwright.sync_api import expect
from utils.test_data.products import CATEGORIES, WOMEN_CATEGORIES, MEN_CATEGORIES, KIDS_CATEGORIES
from utils.test_data.titles import TITLES
from utils.assertions import expect_url_contains, expect_title, expect_visible, expect_text

@allure.feature("Products")
@allure.story("Categories")
@allure.title("Filter products by categories")
@allure.description("Verify products can be sorted by categories.")

def test_view_category_products(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])
    expect_visible(app.home.categories_section, "Category section")

    app.home.select_category(CATEGORIES["women"], WOMEN_CATEGORIES["dress"])
    expect_url_contains(app.category_products.page, app.category_products.PATH)
    expect_text(app.category_products.title_filtered_products, f'{CATEGORIES["women"]} - {WOMEN_CATEGORIES["dress"]} Products')

    app.category_products.select_category(CATEGORIES["men"], MEN_CATEGORIES["jeans"])
    expect_text(app.category_products.title_filtered_products, f'{CATEGORIES["men"]} - {MEN_CATEGORIES["jeans"]} Products')

    app.category_products.select_category(CATEGORIES["kids"], KIDS_CATEGORIES["tops_shirts"])
    expect_text(app.category_products.title_filtered_products, f'{CATEGORIES["kids"]} - {KIDS_CATEGORIES["tops_shirts"]} Products')