import allure
import re

from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.test_data.products import CATEGORIES

class CategoryProductsPage(BasePage):
    PATH = "/category_products"

    def __init__(self, page: Page):
        super().__init__(page)

        self.products_list = page.locator(".features_items")
        self.title_filtered_products = page.locator(".features_items > h2")

        self.category_women = page.get_by_role("link", name=re.compile("Women"))
        self.category_men = page.get_by_role("link", name=re.compile("Men"))
        self.category_kids = page.locator("#accordian").get_by_role("link", name=re.compile("Kids"))
        self.categories = {
            CATEGORIES["women"]: self.category_women,
            CATEGORIES["men"]: self.category_men,
            CATEGORIES["kids"]: self.category_kids,
        }
        self.women_items = page.locator("#Women li")
        self.men_items = page.locator("#Men li")
        self.kids_items = page.locator("#Kids li")
        self.subcategories = {
            CATEGORIES["women"]: self.women_items,
            CATEGORIES["men"]: self.men_items,
            CATEGORIES["kids"]: self.kids_items,
        }

    def verify_loaded(self):
        self.verify_url_contains(self.PATH)

    def select_category(self, category: str, subcategory: str):
        with allure.step(f'Select category: "{category}" > "{subcategory}"'):
            self.click(
                self.categories[category],
                f"{category} category"
            )

            self.click(
                self.subcategories[category]
                    .filter(has_text=subcategory)
                    .locator("a"),
                f"{subcategory} filter"
            )