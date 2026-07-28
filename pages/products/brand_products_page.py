import allure

from pages.base_page import BasePage
from pages.locators.products.brand_products_locators import BrandProductsLocators as L

class BrandProductsPage(BasePage):
    def verify_loaded(self):
        self.verify_url_contains(L.PATH)

    def verify_filtered_title(self, expected_brand: str):
        self.verify_text(
            self.page.locator(L.TITLE_FILTERED_PRODUCTS),
            f'Brand - {expected_brand} Products'
        )

    def filter_by_brand(self, brand: str):
        with allure.step(f'Select brand: "{brand}"'):
            brand_button = L.BRANDS_BUTTONS[brand]
            self.click(
                self.page.locator(brand_button),
                f"{brand} filter"
            )

    def verify_products_exist(self):
        count = self.page.locator(L.PRODUCTS_LIST).count()
        with allure.step(f"Verify products are displayed ({count} found)"):
            assert count > 0, "No products found"