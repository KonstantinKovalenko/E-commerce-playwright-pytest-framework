import allure

from utils.test_data import CATEGORIES, WOMEN_CATEGORIES, MEN_CATEGORIES, KIDS_CATEGORIES

@allure.feature("Categories")
@allure.story("Products categories")
@allure.title("Filter products by categories")
@allure.description("Verify products can be sorted by categories.")

def test_view_category_products(home_page, category_products_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.verify_categories_visible()

    home_page.select_category(CATEGORIES["women"], WOMEN_CATEGORIES["dress"])
    category_products_page.verify_loaded()
    category_products_page.verify_filtered_title(CATEGORIES["women"], WOMEN_CATEGORIES["dress"])

    category_products_page.select_category(CATEGORIES["men"], MEN_CATEGORIES["jeans"])
    category_products_page.verify_filtered_title(CATEGORIES["men"], MEN_CATEGORIES["jeans"])

    category_products_page.select_category(CATEGORIES["kids"], KIDS_CATEGORIES["tops_shirts"])
    category_products_page.verify_filtered_title(CATEGORIES["kids"], KIDS_CATEGORIES["tops_shirts"])