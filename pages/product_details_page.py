from pages.base_page import BasePage

class ProductDetailsPage(BasePage):
    PRODUCT_INFORMATION = ".product-information"

    PRODUCT_NAME = ".product-information h2"
    CATEGORY = '.product-information p:has-text("Category:")'
    PRICE = ".product-information span > span"
    AVAILABILITY = '.product-information p:has-text("Availability:")'
    CONDITION = '.product-information p:has-text("Condition:")'
    BRAND = '.product-information p:has-text("Brand:")'

    QUANTITY_INPUT = "#quantity"
    ADD_TO_CART_BUTTON = '[type="button"]'
    MODAL_VIEW_CART_BUTTON = '.modal-body a[href="/view_cart"]'

    def verify_loaded(self):
        self.verify_title("Automation Exercise - Product Details")

    def verify_product_details_visible(self):
        self.verify_visible(self.page.locator(self.PRODUCT_NAME), "Product name")

        self.verify_text_contains(self.page.locator(self.CATEGORY), "Category:")
        self.verify_text_contains(self.page.locator(self.PRICE), "Rs.")
        self.verify_text_contains(self.page.locator(self.AVAILABILITY), "Availability:")
        self.verify_text_contains(self.page.locator(self.CONDITION), "Condition:")
        self.verify_text_contains(self.page.locator(self.BRAND), "Brand:")

    def set_quantity(self, quantity: int):
        self.fill(self.page.locator(self.QUANTITY_INPUT), str(quantity), "Quantity")

    def click_add_to_cart(self):
        self.click(
            self.page.locator(self.ADD_TO_CART_BUTTON),
            "Add to cart"
        )

    def click_modal_view_cart(self):
        self.click(
            self.page.locator(self.MODAL_VIEW_CART_BUTTON),
            "View cart"
        )