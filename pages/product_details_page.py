from pages.base_page import BasePage
from utils.test_data import REVIEW

class ProductDetailsPage(BasePage):
    PRODUCT_INFORMATION = ".product-information"
    REVIEW_TITLE = 'a[href="#reviews"]'

    PRODUCT_NAME = ".product-information h2"
    CATEGORY = '.product-information p:has-text("Category:")'
    PRICE = ".product-information span > span"
    AVAILABILITY = '.product-information p:has-text("Availability:")'
    CONDITION = '.product-information p:has-text("Condition:")'
    BRAND = '.product-information p:has-text("Brand:")'

    QUANTITY_INPUT = "#quantity"
    ADD_TO_CART_BUTTON = '[type="button"]'
    MODAL_VIEW_CART_BUTTON = '.modal-body a[href="/view_cart"]'

    NAME_INPUT = "#name"
    EMAIL_INPUT = "#email"
    REVIEW_INPUT = "#review"
    SUBMIT_REVIEW_BUTTON = "#button-review"
    REVIEW_SUCCESS_MESSAGE = ".alert-success span"

    def verify_loaded(self):
        self.verify_title("Automation Exercise - Product Details")

    def verify_product_details_visible(self):
        self.verify_visible(self.page.locator(self.PRODUCT_NAME), "Product name")
        self.verify_text_contains(self.page.locator(self.CATEGORY), "Category:")
        self.verify_text_contains(self.page.locator(self.PRICE), "Rs.")
        self.verify_text_contains(self.page.locator(self.AVAILABILITY), "Availability:")
        self.verify_text_contains(self.page.locator(self.CONDITION), "Condition:")
        self.verify_text_contains(self.page.locator(self.BRAND), "Brand:")

    def verify_review_title_visible(self):
        self.verify_visible(self.page.locator(self.REVIEW_TITLE), "Write Your Review")

    def verify_submit_success(self):
        self.verify_text(self.page.locator(self.REVIEW_SUCCESS_MESSAGE), "Thank you for your review.")

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

    def click_submit_review(self):
        self.click(
            self.page.locator(self.SUBMIT_REVIEW_BUTTON),
            "Submit"
        )

    def fill_review_form(self, email: str):
        self.fill(self.page.locator(self.NAME_INPUT), REVIEW["name"], "Name")
        self.fill(self.page.locator(self.EMAIL_INPUT), email, "Email")
        self.fill(self.page.locator(self.REVIEW_INPUT), REVIEW["message"], "Review")

    