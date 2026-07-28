import allure

from pages.base_page import BasePage
from playwright.sync_api import expect
from pages.locators.checkout.cart_locators import CartLocators as L

class CartPage(BasePage):
    def verify_loaded(self):
        self.verify_url(L.PATH)

    def click_proceed_to_checkout(self):
        self.click(
            self.page.locator(L.BUTTON_PROCEED_TO_CHECKOUT),
            "Proceed To Checkout"
        )

    def click_modal_register_login(self):
        self.click(
            self.page.locator(L.BUTTON_MODAL_REGISTER_LOGIN),
            "Register / Login"
        )

    def verify_product(self, index: int, expected: dict):
        with allure.step(f'Compare #{index + 1} added product with #{index + 1} item in the cart'):
            product = self.page.locator(L.CART_ITEMS).nth(index)
            self.verify_text(product.locator(L.ITEM_NAME), expected["name"])
            self.verify_text(product.locator(L.ITEM_PRICE), f'Rs. {expected["price"]}')

            quantity = int(product.locator(L.ITEM_QUANTITY).inner_text())
            expected_total = expected["price"] * quantity

            self.verify_text(product.locator(L.ITEM_TOTAL_PRICE), f"Rs. {expected_total}")

    def verify_quantity(self, index: int, expected: int):
        with allure.step(f'Verify quantity equals expected value'):
            product = self.page.locator(L.CART_ITEMS).nth(index)
            self.verify_text(product.locator(L.ITEM_QUANTITY), str(expected))

    def verify_cart_empty(self):
            self.verify_text(
                self.page.locator(L.CART_EMPTY),
                "Cart is empty!"
            )

    def remove_all_products(self):
        with allure.step(f'Remove all products from cart'):
            while self.page.locator(L.CART_ITEMS).count() > 0:
                rows = self.page.locator(L.CART_ITEMS)
                previous = rows.count()
                rows.last.locator(L.BUTTON_REMOVE_PRODUCT).click()

                expect(rows).to_have_count(previous - 1)

    def get_cart_products(self):
        with allure.step(f'Get contents of the cart'):
            products = []
            rows = self.page.locator(L.CART_ITEMS)

            for i in range(rows.count()):
                row = rows.nth(i)
                products.append({
                    "name": row.locator(L.ITEM_NAME).inner_text(),
                    "price": int(
                        row.locator(L.ITEM_PRICE).inner_text().replace("Rs. ", "")
                    ),
                    "quantity": int(
                        row.locator(L.ITEM_QUANTITY).inner_text()
                    ),
                    "total": int(
                        row.locator(L.ITEM_TOTAL_PRICE).inner_text().replace("Rs. ", "")
                    )
                })
            return products

    def verify_cart_contents_unchanged(self, actual_products: list[dict], expected_products: list[dict]):
        with allure.step(f'Verify remembered products in the cart remain unchanged'):
            assert actual_products == expected_products, (
                f"Cart contents changed.\n"
                f"Expected: {expected_products}\n"
                f"Actual: {actual_products}"
            )