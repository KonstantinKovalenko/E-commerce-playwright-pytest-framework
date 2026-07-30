import allure
import re

from pages.base_page import BasePage
from utils.test_data.products import CATEGORIES

class HomePage(BasePage):
    PATH = "/"

    def __init__(self, page: Page):
        super().__init__(page)

        self.view_products = page.locator(".features_items .choose a")
        self.product_cards = page.locator(".features_items .col-sm-4 .productinfo")

        self.button_modal_continue_shopping = page.get_by_role("button", name="Continue Shopping")
        self.button_modal_view_cart = page.locator(".modal-body").get_by_role("link", name="View Cart")
        self.button_add_to_cart = page.locator(".features_items .productinfo a")
        self.button_scroll_up = page.locator("#scrollUp")

        self.categories_section = page.locator("#accordian")

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

        self.recommended_section = page.locator(".recommended_items")
        self.recommended_items = page.locator("#recommended-item-carousel .productinfo")
        self.button_recommended_add_to_cart = page.locator("#recommended-item-carousel .productinfo a")

        self.slide_carousel_titles = page.locator("#slider-carousel .carousel-inner").get_by_role("heading", level=2, name="Full-Fledged practice website for Automation Engineers")

    def verify_loaded(self):
        self.verify_title("Automation Exercise")

    def verify_carousel_title_visible(self):
        self.verify_text(self.slide_carousel_titles.first, "Full-Fledged practice website for Automation Engineers")

    def verify_categories_visible(self):
        self.verify_visible(
            self.categories_section,
            "Category section"
        )

    def verify_recommended_visible(self):
        self.verify_visible(
            self.recommended_section,
            "Recommended section"
        )

    def scroll_down_to_recommended(self):
        self.scroll_to(
            self.recommended_section,
            "Site recommended"
        )

    def click_view_product(self, index: int):
        self.click(
            self.view_products.nth(index),
            f"#{index + 1} product's View Product" 
        )

    def click_scroll_up(self):
        self.click(
            self.button_scroll_up,
            "Scroll Up arrow button" 
        )

    def click_modal_view_cart(self):
        self.click(
            self.button_modal_view_cart,
            "View cart"
        )

    def click_modal_continue_shopping(self):
        self.click(
            self.button_modal_continue_shopping,
            "Continue shopping"
        )

    def get_product_info(self, locator: str, index: int):
        with allure.step(f'Get information from product #{index + 1}'):
            product = locator.nth(index)

            return {
                "name": product.locator("p").inner_text(),
                "price": int(product.locator("h2").inner_text().replace("Rs. ", ""))
            }

    def add_product_to_cart(self, locator: str, index: int):
        self.click(
            locator.nth(index),
            f"Add product #{index + 1} to cart"
        )

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