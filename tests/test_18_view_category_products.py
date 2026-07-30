import allure

from playwright.sync_api import expect
from utils.test_data.products import CATEGORIES, WOMEN_CATEGORIES, MEN_CATEGORIES, KIDS_CATEGORIES
from utils.test_data.titles import TITLES

@allure.feature("Products")
@allure.story("Categories")
@allure.title("Filter products by categories")
@allure.description("Verify products can be sorted by categories.")

def test_view_category_products(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    with allure.step(f'Verify "Category" section is visible'):
        expect(app.home.categories_section).to_be_visible()

    app.home.select_category(CATEGORIES["women"], WOMEN_CATEGORIES["dress"])

    app.category_products.verify_loaded()
    
    app.category_products.verify_filtered_title(CATEGORIES["women"], WOMEN_CATEGORIES["dress"])

    app.category_products.select_category(CATEGORIES["men"], MEN_CATEGORIES["jeans"])
    app.category_products.verify_filtered_title(CATEGORIES["men"], MEN_CATEGORIES["jeans"])

    app.category_products.select_category(CATEGORIES["kids"], KIDS_CATEGORIES["tops_shirts"])
    app.category_products.verify_filtered_title(CATEGORIES["kids"], KIDS_CATEGORIES["tops_shirts"])