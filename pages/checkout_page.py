import allure

from pages.base_page import BasePage
from utils.test_data import TEST_USER, CONTACT_US

class CheckoutPage(BasePage):
    PATH = "/checkout"

    CART_ITEMS = "tbody tr"
    ITEM_NAME = ".cart_description a"
    ITEM_PRICE = ".cart_price p"
    ITEM_QUANTITY = ".cart_quantity button"
    ITEM_TOTAL_PRICE = ".cart_total p"

    DELIVERY_ADDRESS = "#address_delivery"
    COMMENT_TEXT_AREA = ".form-control"
    PLACE_ORDER_BUTTON = 'a[href="/payment"]'
    TOTAL_PRICES = ".cart_total_price"

    def verify_loaded(self):
        self.verify_url(self.PATH)

    def click_place_order(self):
        self.click(
            self.page.locator(self.PLACE_ORDER_BUTTON),
            "Place Order"
        )

    def verify_product(self, index: int, expected: dict):
        with allure.step(f'Compare #{index + 1} added product with #{index + 1} item in the cart'):
            product = self.page.locator(self.CART_ITEMS).nth(index)
            
            self.verify_text(
                product.locator(self.ITEM_NAME),
                expected["name"]
            )

            self.verify_text(
                product.locator(self.ITEM_PRICE),
                f'Rs. {expected["price"]}'
            )

            quantity = int(
                product.locator(self.ITEM_QUANTITY).inner_text()
            )

            expected_total = expected["price"] * quantity

            self.verify_text(
                product.locator(self.ITEM_TOTAL_PRICE),
                f"Rs. {expected_total}"
            )

    def verify_delivery_address(self):
        address = self.page.locator(self.DELIVERY_ADDRESS)
        self.verify_text_contains(address, f'{TEST_USER["first_name"]} {TEST_USER["last_name"]}')
        self.verify_text_contains(address, TEST_USER["address"])
        self.verify_text_contains(address, f'{TEST_USER["city"]} {TEST_USER["state"]} {TEST_USER["zipcode"]}')
        self.verify_text_contains(address, TEST_USER["country"])
        self.verify_text_contains(address, TEST_USER["mobile"])

    def verify_delivery_address2(self):
        address = self.page.locator(self.DELIVERY_ADDRESS)

        self.verify_text_contains(address, "Mr. Good User")
        self.verify_text_contains(address, "Baker street")
        self.verify_text_contains(address, "New York Ohio 12000")
        self.verify_text_contains(address, "United States")
        self.verify_text_contains(address, "+123456789")

    def add_comment(self):
        self.fill(self.page.locator(self.COMMENT_TEXT_AREA), CONTACT_US["message"], "Comment")

    def verify_total_amount(self):
        with allure.step("Verify total amount equals sum of product totals"):
            totals = self.page.locator(self.TOTAL_PRICES)

            expected_total = 0

            for i in range(totals.count() - 1):
                text = totals.nth(i).inner_text()
                expected_total += int(text.replace("Rs. ", ""))

            self.verify_text(totals.last, f"Rs. {expected_total}")