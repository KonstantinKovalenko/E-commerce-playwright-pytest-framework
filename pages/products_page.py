import allure

from pages.base_page import BasePage

class ProductsPage(BasePage):
    PATH = "/products"

    PRODUCTS_LIST = ".features_items"
    PRODUCTS_ARRAY = ".features_items .col-sm-4 .productinfo"
    MODAL_CONTINUE_SHOPPING_BUTTON = ".modal-footer button"
    MODAL_VIEW_CART_BUTTON = '.modal-body a[href="/view_cart"]'

    VIEW_PRODUCT = ".features_items .choose a"
    PRODUCT_FRAME = ".features_items .single-products"
    OVERLAY_ADD_TO_CART_BUTTON = ".features_items .product-overlay a"

    SEARCH_PRODUCT_INPUT = "#search_product"
    SEARCH_PRODUCT_BUTTON = "#submit_search"

    SEARCHED_PRODUCTS_TITLE = '.features_items > h2.title'
    PRODUCT_NAME = '.features_items .productinfo p'

    def verify_loaded(self):
        self.verify_title("Automation Exercise - All Products")

    def verify_products_list_visible(self):
        self.verify_visible(
            self.page.locator(self.PRODUCTS_LIST),
            "All Products section"
        )

    def click_modal_continue_shopping(self):
        self.click(
            self.page.locator(self.MODAL_CONTINUE_SHOPPING_BUTTON),
            "Continue shopping"
        )

    def click_modal_view_cart(self):
        self.click(
            self.page.locator(self.MODAL_VIEW_CART_BUTTON),
            "View cart"
        )

    def click_first_view_product(self):
        self.click(
            self.page.locator(self.VIEW_PRODUCT).nth(0),
            "First product - View Product"
        )

    def add_product_to_cart(self, index: int):
        self.click(
            self.page.locator(self.OVERLAY_ADD_TO_CART_BUTTON).nth(index),
            f'Add product #{index + 1} to cart'
        )

    def search_by_product_name(self, product: str):
        self.fill(self.page.locator(self.SEARCH_PRODUCT_INPUT), product, "Product")

        self.click(
            self.page.locator(self.SEARCH_PRODUCT_BUTTON),
            "First product - View Product"
        )

    def verify_search_result(self, expected_name: str):
        self.verify_text(
            self.page.locator(self.SEARCHED_PRODUCTS_TITLE),
            "Searched Products"
        )

        self.verify_text(
            self.page.locator(self.PRODUCT_NAME).first,
            expected_name
        )

    def hover_over_product(self, index: int):
        with allure.step(f'Hover over product #{index + 1}'):
            self.page.locator(self.PRODUCT_FRAME).nth(index).hover()

    def get_product_info(self, index: int):
        with allure.step(f'Get information from product: #{index + 1}'):
            product = self.page.locator(self.PRODUCTS_ARRAY).nth(index)
            name = product.locator("p").inner_text()
            price = int(product.locator("h2").inner_text().replace("Rs. ", ""))

            return {
                "name": name,
                "price": price
            }