import allure

from pages.base_page import BasePage
from pages.locators.products.category_products_locators import CategoryProductsLocators as L

class CategoryProductsPage(BasePage):
    def verify_loaded(self):
        self.verify_url_contains(L.PATH)

    def verify_filtered_title(self, expected_category, expected_filter: str):
        self.verify_text(
            self.page.locator(L.TITLE_FILTERED_PRODUCTS),
            f'{expected_category} - {expected_filter} Products'
        )

    def select_category(self, category: str, filter: str):
        with allure.step(f'Select category: "{category}" > "{filter}"'):
            category_button, category_list = L.CATEGORY_BUTTONS[category]

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