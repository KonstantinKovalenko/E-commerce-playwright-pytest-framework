from pages.base_page import BasePage

class ProductsPage(BasePage):
    PATH = "/products"

    PRODUCTS_LIST = ".features_items"
    FIRST_VIEW_PRODUCT = ".features_items .choose a"

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