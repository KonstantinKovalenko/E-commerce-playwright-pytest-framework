import allure

from pages.base_page import BasePage
from pages.locators.home_locators import HomeLocators as L

class HomePage(BasePage):
    def verify_loaded(self):
        self.verify_title("Automation Exercise")

    def verify_carousel_title_visible(self):
        self.verify_text(self.page.locator(L.SLIDE_CAROUSEL_TITLES).first, "Full-Fledged practice website for Automation Engineers")

    def verify_categories_visible(self):
        self.verify_visible(
            self.page.locator(L.CATEGORIES_SECTION),
            "Category section"
        )

    def verify_recommended_visible(self):
        self.verify_visible(
            self.page.locator(L.RECOMMENDED_SECTION),
            "Recommended section"
        )

    def scroll_down_to_recommended(self):
        self.scroll_to(
            self.page.locator(L.RECOMMENDED_SECTION),
            "Site recommended"
        )

    def click_view_product(self, index: int):
        self.click(
            self.page.locator(L.VIEW_PRODUCT).nth(index),
            f"#{index + 1} product's View Product" 
        )

    def click_scroll_up(self):
        self.click(
            self.page.locator(L.BUTTON_SCROLL_UP),
            "Scroll Up arrow button" 
        )

    def click_modal_view_cart(self):
        self.click(
            self.page.locator(L.BUTTON_MODAL_VIEW_CART),
            "View cart"
        )

    def click_modal_continue_shopping(self):
        self.click(
            self.page.locator(L.BUTTON_MODAL_CONTINUE_SHOPPING),
            "Continue shopping"
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