from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.test_data.products import REVIEW

class ProductDetailsPage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_information = page.locator(".product-information")
        self.title_review = page.get_by_role("link", name="Write Your Review")

        self.product_info = page.locator(".product-information")

        self.product_name = self.product_info.locator("h2")
        self.category = self.product_info.get_by_text("Category:")
        self.price = self.product_info.locator("span > span")
        self.availability = self.product_info.get_by_text("Availability:")
        self.condition = self.product_info.get_by_text("Condition:")
        self.brand = self.product_info.get_by_text("Brand:")

        self.input_quantity = page.locator('#quantity')

        self.button_add_to_cart = page.get_by_role("button", name="Add to cart")
        self.button_modal_view_cart = page.locator(".modal-body").get_by_role("link", name="View Cart")

        self.input_name = page.locator('#name')
        self.input_email = page.locator('#email')
        self.input_review = page.locator('#review')

        self.button_submit_review = page.get_by_role("button", name="Submit")

        self.review_success_message = page.locator(".alert-success").get_by_text("Thank you for your review.")

    def click_add_to_cart(self):
        self.click(
            self.button_add_to_cart,
            "Add to cart"
        )

    def click_modal_view_cart(self):
        self.click(
            self.button_modal_view_cart,
            "View cart"
        )

    def click_submit_review(self):
        self.click(
            self.button_submit_review,
            "Submit"
        )

    def verify_product_details_visible(self):
        self.verify_text_contains(self.category, "Category:")
        self.verify_text_contains(self.price, "Rs.")
        self.verify_text_contains(self.availability, "Availability:")
        self.verify_text_contains(self.condition, "Condition:")
        self.verify_text_contains(self.brand, "Brand:")

    def verify_submit_success(self):
        self.verify_text(self.review_success_message, "Thank you for your review.")

    def set_quantity(self, quantity: int):
        self.fill(self.input_quantity, str(quantity), "Quantity")

    def fill_review_form(self, email: str):
        self.fill(self.input_name, REVIEW["name"], "Name")
        self.fill(self.input_email, email, "Email")
        self.fill(self.input_review, REVIEW["message"], "Review")   