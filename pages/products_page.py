from pages.base_page import BasePage

class ProductsPage(BasePage):
    PATH = "/products"

    PRODUCTS_LIST = ".features_items"
    FIRST_VIEW_PRODUCT = ".features_items .choose a"

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

    def click_first_view_product(self):
        self.click(
            self.page.locator(self.FIRST_VIEW_PRODUCT).first,
            "First product - View Product"
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