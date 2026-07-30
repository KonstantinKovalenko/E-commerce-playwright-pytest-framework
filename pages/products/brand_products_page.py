import allure

from pages.base_page import BasePage
from utils.test_data.products import BRANDS

class BrandProductsPage(BasePage):
    PATH = "/brand_products"

    def __init__(self, page: Page):
        super().__init__(page)

        self.products_list = page.locator(".features_items .col-sm-4")
        self.title_filtered_products = page.locator(".features_items > h2")

        self.brands_filters = page.locator('.brands-name')
        self.brand_buttons = {
            BRANDS["polo"]: page.get_by_role("link", name="Polo"),
            BRANDS["h_m"]: page.get_by_role("link", name="H&M"),
            BRANDS["madame"]: page.get_by_role("link", name="Madame"),
            BRANDS["mast_harbour"]: page.get_by_role("link", name="Mast & Harbour"),
            BRANDS["babyhug"]: page.get_by_role("link", name="Babyhug"),
            BRANDS["allen_solly_junior"]: page.get_by_role("link", name="Allen Solly Junior"),
            BRANDS["kookie_kids"]: page.get_by_role("link", name="Kookie Kids"),
            BRANDS["biba"]: page.get_by_role("link", name="Biba"),
        }

    def verify_loaded(self):
        self.verify_url_contains(self.PATH)

    def verify_filtered_title(self, expected_brand: str):
        self.verify_text(
            self.title_filtered_products,
            f'Brand - {expected_brand} Products'
        )

    def filter_by_brand(self, brand: str):
        with allure.step(f'Select brand: "{brand}"'):
            self.click(
                self.brand_buttons[brand],
                f"{brand} filter"
            )

    def verify_products_exist(self):
        count = self.products_list.count()
        with allure.step(f"Verify products are displayed ({count} found)"):
            assert count > 0, "No products found"