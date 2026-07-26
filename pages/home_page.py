import allure

from components.header import Header
from components.footer import Footer
from pages.base_page import BasePage

from utils.test_data import CATEGORIES

class HomePage(BasePage):
    PATH = "/"

    VIEW_PRODUCT = ".features_items .choose a"
    PRODUCT_CARDS = ".features_items .col-sm-4 .productinfo"

    MODAL_CONTINUE_SHOPPING_BUTTON = ".modal-footer button"
    MODAL_VIEW_CART_BUTTON = '.modal-body a[href="/view_cart"]'
    ADD_TO_CART_BUTTON = ".features_items .productinfo a"

    CATEGORIES_SECTION = "#accordian"

    CATEGORY_BUTTONS = {
        CATEGORIES["women"]: ('a[href="#Women"]', "#Women li"),
        CATEGORIES["men"]: ('a[href="#Men"]', "#Men li"),
        CATEGORIES["kids"]: ('a[href="#Kids"]', "#Kids li"),
    }

    RECOMMENDED_SECTION = ".recommended_items"
    RECOMMENDED_ITEMS = ".recommended_items .productinfo"
    RECOMMENDED_ADD_TO_CART_BUTTON = ".recommended_items .productinfo a"

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)
        self.footer = Footer(page)

    def verify_loaded(self):
        self.verify_title("Automation Exercise")

    def verify_categories_visible(self):
        self.verify_visible(
            self.page.locator(self.CATEGORIES_SECTION),
            "Category section"
        )

    def verify_recommended_visible(self):
        self.verify_visible(
            self.page.locator(self.RECOMMENDED_SECTION),
            "Recommended section"
        )

    def click_view_product(self, index: int):
        self.click(
            self.page.locator(self.VIEW_PRODUCT).nth(index),
            f"#{index + 1} product's View Product" 
        )

    def get_product_info(self, locator: str, index: int):
        with allure.step(f'Get information from product #{index + 1}'):
            product = self.page.locator(locator).nth(index)

            return {
                "name": product.locator("p").inner_text(),
                "price": int(product.locator("h2").inner_text().replace("Rs. ", ""))
            }

    def add_product_to_cart(self, locator: str, index: int):
        self.click(
            self.page.locator(locator).nth(index),
            f"Add product #{index + 1} to cart"
        )

    def click_modal_view_cart(self):
        self.click(
            self.page.locator(self.MODAL_VIEW_CART_BUTTON),
            "View cart"
        )

    def click_modal_continue_shopping(self):
        self.click(
            self.page.locator(self.MODAL_CONTINUE_SHOPPING_BUTTON),
            "Continue shopping"
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

    def scroll_down_to_recommended(self):
        self.scroll_to(
            self.page.locator(self.RECOMMENDED_SECTION),
            "Site recommended"
        )