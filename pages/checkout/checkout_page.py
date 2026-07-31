import allure

from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.test_data.contact import CONTACT_US

class CheckoutPage(BasePage):
    PATH = "/checkout"

    def __init__(self, page: Page):
        super().__init__(page)

        self.checkout_items = page.locator('tbody tr')
        self.item_name = page.locator('.cart_description a')
        self.item_price = page.locator('.cart_price p')
        self.item_quantity = page.locator('.cart_quantity button')
        self.item_total_price = page.locator('.cart_total p')

        self.delivery_address = page.locator('#address_delivery')
        self.billing_address = page.locator('#address_invoice')
        self.total_prices = page.locator('.cart_total_price')

        self.text_area_comment = page.locator('.form-control')
        self.button_place_order = page.get_by_role('link', name="Place Order")

    def click_place_order(self):
        self.click(
            self.button_place_order,
            "Place Order"
        )

    def get_product(self, index: int):
        product = self.checkout_items.nth(index)

        return {
            "name": product.locator(self.item_name),
            "price": product.locator(self.item_price),
            "quantity": int(product.locator(self.item_quantity).inner_text()),
            "total": product.locator(self.item_total_price),
        }

    def add_comment(self):
        self.fill(self.text_area_comment, CONTACT_US["message"], "Comment")

    def total_amount(self):
        return self.total_prices.last

    def calculate_total_amount(self):
        totals = self.total_prices
        expected_total = 0

        for i in range(totals.count() - 1):
            text = totals.nth(i).inner_text()
            expected_total += int(text.replace("Rs. ", ""))

        with allure.step(f"Calculated total amount: {expected_total}"):
            return f"Rs. {expected_total}"