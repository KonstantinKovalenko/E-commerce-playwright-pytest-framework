import allure

from utils.test_data.products import CATEGORIES, WOMEN_CATEGORIES, MEN_CATEGORIES, KIDS_CATEGORIES

@allure.feature("Products")
@allure.story("Categories")
@allure.title("Filter products by categories")
@allure.description("Verify products can be sorted by categories.")

def test_view_category_products(app):
    app.home.open()
    app.home.verify_loaded()

    app.home.verify_categories_visible()

    app.home.select_category(CATEGORIES["women"], WOMEN_CATEGORIES["dress"])
    app.category_products.verify_loaded()
    app.category_products.verify_filtered_title(CATEGORIES["women"], WOMEN_CATEGORIES["dress"])

    app.category_products.select_category(CATEGORIES["men"], MEN_CATEGORIES["jeans"])
    app.category_products.verify_filtered_title(CATEGORIES["men"], MEN_CATEGORIES["jeans"])

    app.category_products.select_category(CATEGORIES["kids"], KIDS_CATEGORIES["tops_shirts"])
    app.category_products.verify_filtered_title(CATEGORIES["kids"], KIDS_CATEGORIES["tops_shirts"])