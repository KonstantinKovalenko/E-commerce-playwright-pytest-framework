import allure

from pages.base_page import BasePage
from utils.test_data.contact import CONTACT_US
from pages.locators.checkout.checkout_locators import CheckoutLocators as L

class CheckoutPage(BasePage):
    def verify_loaded(self):
        self.verify_url(L.PATH)

    def click_place_order(self):
        self.click(
            self.page.locator(L.BUTTON_PLACE_ORDER),
            "Place Order"
        )

    def verify_product(self, index: int, expected: dict):
        with allure.step(f'Compare #{index + 1} added product with #{index + 1} item in the cart'):
            product = self.page.locator(L.CART_ITEMS).nth(index)
            
            self.verify_text(
                product.locator(L.ITEM_NAME),
                expected["name"]
            )

            self.verify_text(
                product.locator(L.ITEM_PRICE),
                f'Rs. {expected["price"]}'
            )

            quantity = int(
                product.locator(L.ITEM_QUANTITY).inner_text()
            )

            expected_total = expected["price"] * quantity

            self.verify_text(
                product.locator(L.ITEM_TOTAL_PRICE),
                f"Rs. {expected_total}"
            )

    def verify_address(self, locator: str, user: dict):
        with allure.step(f"Verify address: {locator}"):
            address = self.page.locator(locator)
            self.verify_text_contains(address, f'{user["first_name"]} {user["last_name"]}')
            self.verify_text_contains(address, user["address"])
            self.verify_text_contains(address, f'{user["city"]} {user["state"]} {user["zipcode"]}')
            self.verify_text_contains(address, user["country"])
            self.verify_text_contains(address, user["mobile"])

    def add_comment(self):
        self.fill(self.page.locator(L.TEXT_AREA_COMMENT), CONTACT_US["message"], "Comment")

    def verify_total_amount(self):
        with allure.step("Verify total amount equals sum of product totals"):
            totals = self.page.locator(L.TOTAL_PRICES)

            expected_total = 0

            for i in range(totals.count() - 1):
                text = totals.nth(i).inner_text()
                expected_total += int(text.replace("Rs. ", ""))

            self.verify_text(totals.last, f"Rs. {expected_total}")