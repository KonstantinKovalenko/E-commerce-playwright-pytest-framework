import allure

from components.footer import Footer
from pages.base_page import BasePage

class CartPage(BasePage):
    PATH = "/view_cart"

    CART_ITEMS = "tbody tr"
    ITEM_NAME = ".cart_description a"
    ITEM_PRICE = ".cart_price p"
    ITEM_QUANTITY = ".cart_quantity button"
    ITEM_TOTAL_PRICE = ".cart_total p"

    PROCEED_TO_CHECHOUT_BUTTON = "#do_action .check_out"
    
    MODAL_REGISTER_LOGIN_BUTTON = '.modal-body a[href="/login"]'

    def __init__(self, page):
        super().__init__(page)
        self.footer = Footer(page)

    def verify_loaded(self):
        self.verify_title("Automation Exercise - Checkout")

    def click_proceed_to_checkout(self):
        self.click(
            self.page.locator(self.PROCEED_TO_CHECHOUT_BUTTON),
            "Proceed To Checkout"
        )

    def click_modal_register_login(self):
        self.click(
            self.page.locator(self.MODAL_REGISTER_LOGIN_BUTTON),
            "Register / Login"
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

    def verify_quantity(self, index: int, expected: int):
        with allure.step(f'Verify quantity equals expected value'):
            product = self.page.locator(self.CART_ITEMS).nth(index)

            self.verify_text(
                product.locator(self.ITEM_QUANTITY),
                str(expected)
            )