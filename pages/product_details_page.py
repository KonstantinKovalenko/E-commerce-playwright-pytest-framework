from pages.base_page import BasePage

class ProductDetailsPage(BasePage):
    PRODUCT_INFORMATION = ".product-information"

    PRODUCT_NAME = ".product-information h2"
    CATEGORY = '.product-information p:has-text("Category:")'
    PRICE = ".product-information span > span"
    AVAILABILITY = '.product-information p:has-text("Availability:")'
    CONDITION = '.product-information p:has-text("Condition:")'
    BRAND = '.product-information p:has-text("Brand:")'

    def verify_loaded(self):
        self.verify_title("Automation Exercise - Product Details")

    def verify_product_details_visible(self):
        self.verify_visible(self.page.locator(self.PRODUCT_NAME), "Product name")

        self.verify_text_contains(self.page.locator(self.CATEGORY), "Category:")
        self.verify_text_contains(self.page.locator(self.PRICE), "Rs.")
        self.verify_text_contains(self.page.locator(self.AVAILABILITY), "Availability:")
        self.verify_text_contains(self.page.locator(self.CONDITION), "Condition:")
        self.verify_text_contains(self.page.locator(self.BRAND), "Brand:")