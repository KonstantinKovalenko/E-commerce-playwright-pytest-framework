import allure

from pages.base_page import BasePage
from utils.test_data import BRANDS

class BrandProductsPage(BasePage):
    PATH = "/brand_products"

    PRODUCTS_LIST = ".features_items .col-sm-4"
    FILTERED_PRODUCTS_TITLE = '.features_items > h2'

    BRANDS_FILTERS = ".brands-name"
    BRANDS_BUTTONS = {
        BRANDS["polo"]: 'a[href="/brand_products/Polo"]',
        BRANDS["h_m"]: 'a[href="/brand_products/H&M"]',
        BRANDS["madame"]: 'a[href="/brand_products/Madame"]',
        BRANDS["mast_harbour"]: 'a[href="/brand_products/Mast & Harbour"]',
        BRANDS["babyhug"]: 'a[href="/brand_products/Babyhug"]',
        BRANDS["allen_solly_junior"]: 'a[href="/brand_products/Allen Solly Junior"]',
        BRANDS["kookie_kids"]: 'a[href="/brand_products/Kookie Kids"]',
        BRANDS["biba"]: 'a[href="/brand_products/Biba"]'
    }

    def verify_loaded(self):
        self.verify_url_contains(self.PATH)

    def verify_filtered_title(self, expected_brand: str):
        self.verify_text(
            self.page.locator(self.FILTERED_PRODUCTS_TITLE),
            f'Brand - {expected_brand} Products'
        )

    def filter_by_brand(self, brand: str):
        with allure.step(f'Select brand: "{brand}"'):
            brand_button = self.BRANDS_BUTTONS[brand]

            self.click(
                self.page.locator(brand_button),
                f"{brand} filter"
            )

    def verify_products_exist(self):
        count = self.page.locator(self.PRODUCTS_LIST).count()

        with allure.step(f"Verify products are displayed ({count} found)"):
            assert count > 0, "No products found"