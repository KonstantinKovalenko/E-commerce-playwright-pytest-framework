import allure

from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.test_data.products import BRANDS

class ProductsPage(BasePage):
    PATH = "/products"

    def __init__(self, page: Page):
        super().__init__(page)

        self.product_cards = page.locator(".features_items .col-sm-4 .productinfo")

        self.button_modal_continue_shopping = page.get_by_role("button", name="Continue Shopping")
        self.button_modal_view_cart = page.locator(".modal-body").get_by_role("link", name="View Cart")
        self.button_add_to_cart = page.locator(".features_items .productinfo a")

        self.view_products = page.locator(".features_items .choose a")
        self.product_frame = page.locator('.features_items .single-products')
        self.button_overlay_add_to_cart = page.locator('.features_items .product-overlay a')

        self.input_search_product = page.locator('#search_product')
        self.button_search_product = page.locator('#submit_search')

        self.title_searched_products = page.locator(".features_items > h2")
        self.product_names = page.locator('.features_items .productinfo p')

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

    def click_modal_continue_shopping(self):
        self.click(
            self.button_modal_continue_shopping,
            "Continue shopping"
        )

    def click_modal_view_cart(self):
        self.click(
            self.button_modal_view_cart,
            "View cart"
        )

    def click_first_view_product(self):
        self.click(
            self.view_products.nth(0),
            "First product - View Product"
        )

    def add_product_to_cart(self, index: int):
        self.click(
            self.button_overlay_add_to_cart.nth(index),
            f'Add product #{index + 1} to cart'
        )

    def add_results_to_cart(self):
        buttons = self.button_add_to_cart
        buttons_count = buttons.count()

        for i in range(buttons_count):
            self.click(buttons.nth(i), f"Add product #{i + 1} to cart")
            self.click(self.button_modal_continue_shopping, "Continue shopping")

    def search_by_product_name(self, product: str):
        self.fill(self.input_search_product, product, "Product")
        self.click(self.button_search_product, "Search Product")

    def first_product_name(self):
        return self.product_names.first

    def hover_over_product(self, index: int):
        with allure.step(f'Hover over product #{index + 1}'):
            self.product_frame.nth(index).hover()

    def get_product_info(self, index: int):
        with allure.step(f'Get information from product: #{index + 1}'):
            product = self.product_cards.nth(index)
            name = product.locator("p").inner_text()
            price = int(product.locator("h2").inner_text().replace("Rs. ", ""))

            return {
                "name": name,
                "price": price
            }

    def filter_by_brand(self, brand: str):
        with allure.step(f'Select brand: "{brand}"'):
            self.click(
                self.brand_buttons[brand],
                f"{brand} filter"
            )

    def get_products_count(self):
        return self.product_cards.count()