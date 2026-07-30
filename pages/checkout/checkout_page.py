import allure

from pages.base_page import BasePage
from utils.test_data.contact import CONTACT_US

class CheckoutPage(BasePage):
    PATH = "/checkout"

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_items = page.locator('tbody tr')
        self.item_name = page.locator('.cart_description a')
        self.item_price = page.locator('.cart_price p')
        self.item_quantity = page.locator('.cart_quantity button')
        self.item_total_price = page.locator('.cart_total p')

        self.delivery_address = page.locator('#address_delivery')
        self.billing_address = page.locator('#address_invoice')
        self.total_prices = page.locator('.cart_total_price')

        self.text_area_comment = page.locator('.form-control')
        self.button_place_order = page.get_by_role('link', name="Place Order")

    def verify_loaded(self):
        self.verify_url(self.PATH)

    def click_place_order(self):
        self.click(
            self.button_place_order,
            "Place Order"
        )

    def verify_product(self, index: int, expected: dict):
        with allure.step(f'Compare #{index + 1} added product with #{index + 1} item in the cart'):
            product = self.cart_items.nth(index)
            
            self.verify_text(
                product.locator(self.item_name),
                expected["name"]
            )

            self.verify_text(
                product.locator(self.item_price),
                f'Rs. {expected["price"]}'
            )

            quantity = int(
                product.locator(self.item_quantity).inner_text()
            )

            expected_total = expected["price"] * quantity

            self.verify_text(
                product.locator(self.item_total_price),
                f"Rs. {expected_total}"
            )

    def verify_address(self, locator: str, user: dict):
        with allure.step(f"Verify address: {locator}"):
            self.verify_text_contains(locator, f'{user["first_name"]} {user["last_name"]}')
            self.verify_text_contains(locator, user["address"])
            self.verify_text_contains(locator, f'{user["city"]} {user["state"]} {user["zipcode"]}')
            self.verify_text_contains(locator, user["country"])
            self.verify_text_contains(locator, user["mobile"])

    def add_comment(self):
        self.fill(self.text_area_comment, CONTACT_US["message"], "Comment")

    def verify_total_amount(self):
        with allure.step("Verify total amount equals sum of product totals"):
            totals = self.total_prices

            expected_total = 0

            for i in range(totals.count() - 1):
                text = totals.nth(i).inner_text()
                expected_total += int(text.replace("Rs. ", ""))

            self.verify_text(totals.last, f"Rs. {expected_total}")