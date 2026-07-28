from pages.base_page import BasePage
from utils.test_data.products import REVIEW
from pages.locators.products.product_details_locators import ProductDetailsLocators as L

class ProductDetailsPage(BasePage):
    def verify_loaded(self):
        self.verify_title("Automation Exercise - Product Details")

    def click_add_to_cart(self):
        self.click(
            self.page.locator(L.BUTTON_ADD_TO_CART),
            "Add to cart"
        )

    def click_modal_view_cart(self):
        self.click(
            self.page.locator(L.BUTTON_MODAL_VIEW_CART),
            "View cart"
        )

    def click_submit_review(self):
        self.click(
            self.page.locator(L.BUTTON_SUBMIT_REVIEW),
            "Submit"
        )

    def verify_product_details_visible(self):
        self.verify_visible(self.page.locator(L.PRODUCT_NAME), "Product name")
        self.verify_text_contains(self.page.locator(L.CATEGORY), "Category:")
        self.verify_text_contains(self.page.locator(L.PRICE), "Rs.")
        self.verify_text_contains(self.page.locator(L.AVAILABILITY), "Availability:")
        self.verify_text_contains(self.page.locator(L.CONDITION), "Condition:")
        self.verify_text_contains(self.page.locator(L.BRAND), "Brand:")

    def verify_review_title_visible(self):
        self.verify_visible(self.page.locator(L.TITLE_REVIEW), "Write Your Review")

    def verify_submit_success(self):
        self.verify_text(self.page.locator(L.REVIEW_SUCCESS_MESSAGE), "Thank you for your review.")

    def set_quantity(self, quantity: int):
        self.fill(self.page.locator(L.INPUT_QUANTITY), str(quantity), "Quantity")

    def fill_review_form(self, email: str):
        self.fill(self.page.locator(L.INPUT_NAME), REVIEW["name"], "Name")
        self.fill(self.page.locator(L.INPUT_EMAIL), email, "Email")
        self.fill(self.page.locator(L.INPUT_REVIEW), REVIEW["message"], "Review")   