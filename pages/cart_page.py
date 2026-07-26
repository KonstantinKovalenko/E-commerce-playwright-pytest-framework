import allure

from components.footer import Footer
from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    PATH = "/view_cart"

    CART_ITEMS = "tbody tr"
    ITEM_NAME = ".cart_description a"
    ITEM_PRICE = ".cart_price p"
    ITEM_QUANTITY = ".cart_quantity button"
    ITEM_TOTAL_PRICE = ".cart_total p"

    PROCEED_TO_CHECHOUT_BUTTON = "#do_action .check_out"
    MODAL_REGISTER_LOGIN_BUTTON = '.modal-body a[href="/login"]'

    REMOVE_PRODUCT_BUTTON = ".cart_quantity_delete"

    EMPTY_CART = "#empty_cart b"

    def __init__(self, page):
        super().__init__(page)
        self.footer = Footer(page)

    def verify_loaded(self):
        self.verify_url(self.PATH)

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

    def verify_cart_empty(self):
            self.verify_text(
                self.page.locator(self.EMPTY_CART),
                "Cart is empty!"
            )

    def remove_all_products(self):
        with allure.step(f'Remove all products from cart'):
            while self.page.locator(self.CART_ITEMS).count() > 0:
                rows = self.page.locator(self.CART_ITEMS)
                previous = rows.count()

                rows.last.locator(self.REMOVE_PRODUCT_BUTTON).click()

                expect(rows).to_have_count(previous - 1)

    def get_cart_products(self):
        with allure.step(f'Get contents of the cart'):
            products = []
            rows = self.page.locator(self.CART_ITEMS)

            for i in range(rows.count()):
                row = rows.nth(i)

                products.append({
                    "name": row.locator(self.ITEM_NAME).inner_text(),
                    "price": int(
                        row.locator(self.ITEM_PRICE).inner_text().replace("Rs. ", "")
                    ),
                    "quantity": int(
                        row.locator(self.ITEM_QUANTITY).inner_text()
                    ),
                    "total": int(
                        row.locator(self.ITEM_TOTAL_PRICE).inner_text().replace("Rs. ", "")
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