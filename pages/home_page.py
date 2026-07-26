import allure

from components.header import Header
from components.footer import Footer
from pages.base_page import BasePage

class HomePage(BasePage):
    PATH = "/"

    VIEW_PRODUCT = ".features_items .choose a"
    PRODUCT_CARDS = ".features_items .col-sm-4 .productinfo"

    MODAL_CONTINUE_SHOPPING_BUTTON = ".modal-footer button"
    MODAL_VIEW_CART_BUTTON = '.modal-body a[href="/view_cart"]'
    ADD_TO_CART_BUTTON = ".features_items .productinfo a"

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)
        self.footer = Footer(page)

    def verify_loaded(self):
        self.verify_title("Automation Exercise")

    def click_view_product(self, index: int):
        self.click(
            self.page.locator(self.VIEW_PRODUCT).nth(index),
            f"#{index + 1} product's View Product" 
        )

    def get_product_info(self, index: int):
        with allure.step(f'Get information from product: #{index + 1}'):
            product = self.page.locator(self.PRODUCT_CARDS).nth(index)
            name = product.locator("p").inner_text()
            price = int(product.locator("h2").inner_text().replace("Rs. ", ""))

            return {
                "name": name,
                "price": price
            }

    def add_product_to_cart(self, index: int):
        self.click(
            self.page.locator(self.ADD_TO_CART_BUTTON).nth(index),
            f'Add product #{index + 1} to cart'
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