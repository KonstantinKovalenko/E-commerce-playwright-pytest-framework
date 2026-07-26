import allure

from pages.base_page import BasePage
from utils.test_data import CATEGORIES

class CategoryProductsPage(BasePage):
    PATH = "/category_products"

    PRODUCTS_LIST = ".features_items"
    FILTERED_PRODUCTS_TITLE = '.features_items > h2'

    CATEGORY_WOMEN_BUTTON = 'a[href="#Women"]'
    CATEGORY_BUTTONS = {
        CATEGORIES["women"]: ('a[href="#Women"]', "#Women li"),
        CATEGORIES["men"]: ('a[href="#Men"]', "#Men li"),
        CATEGORIES["kids"]: ('a[href="#Kids"]', "#Kids li"),
    }

    def verify_loaded(self):
        self.verify_url_contains(self.PATH)

    def verify_filtered_title(self, expected_category, expected_filter: str):
        self.verify_text(
            self.page.locator(self.FILTERED_PRODUCTS_TITLE),
            f'{expected_category} - {expected_filter} Products'
        )

    def select_category(self, category: str, filter: str):
        with allure.step(f'Select category: "{category}" > "{filter}"'):
            category_button, category_list = self.CATEGORY_BUTTONS[category]

            self.click(
                self.page.locator(category_button),
                f"{category} category"
            )

            self.click(
                self.page.locator(category_list)
                    .filter(has_text=filter)
                    .locator("a"),
                f"{filter} filter"
            )