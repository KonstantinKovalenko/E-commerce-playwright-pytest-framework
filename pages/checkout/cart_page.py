import allure

from pages.base_page import BasePage
from playwright.sync_api import Page
from playwright.sync_api import expect

class CartPage(BasePage):
    PATH = "/view_cart"

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_empty = page.locator('#empty_cart b')
        self.cart_items = page.locator('tbody tr')
        self.item_name = page.locator('.cart_description a')
        self.item_price = page.locator('.cart_price p')
        self.item_quantity = page.locator('.cart_quantity button')
        self.item_total_price = page.locator('.cart_total p')

        self.button_proceed_to_checkout = page.locator('#do_action .check_out')
        self.button_modal_register_login = page.locator(".modal-body").get_by_role("link", name="Register / Login")
        self.button_remove_product = page.locator('.cart_quantity_delete')

    def click_proceed_to_checkout(self):
        self.click(
            self.button_proceed_to_checkout,
            "Proceed To Checkout"
        )

    def click_modal_register_login(self):
        self.click(
            self.button_modal_register_login,
            "Register / Login"
        )

    def get_product(self, index: int):
        product = self.cart_items.nth(index)

        return {
            "name": product.locator(self.item_name),
            "price": product.locator(self.item_price),
            "quantity": int(product.locator(self.item_quantity).inner_text()),
            "total": product.locator(self.item_total_price),
        }

    def quantity_by_index(self, index: int):
        product = self.cart_items.nth(index)
        with allure.step(f'Get quantity locator by index: {index}'):
            return product.locator(self.item_quantity)

    def remove_all_products(self):
        with allure.step(f'Remove all products from cart'):
            while self.cart_items.count() > 0:
                rows = self.cart_items
                previous = rows.count()
                rows.last.locator(self.button_remove_product).click()

                expect(rows).to_have_count(previous - 1)

    def get_cart_products(self):
        with allure.step(f'Get contents of the cart'):
            products = []
            rows = self.cart_items

            for i in range(rows.count()):
                row = rows.nth(i)
                products.append({
                    "name": row.locator(self.item_name).inner_text(),
                    "price": int(
                        row.locator(self.item_price).inner_text().replace("Rs. ", "")
                    ),
                    "quantity": int(
                        row.locator(self.item_quantity).inner_text()
                    ),
                    "total": int(
                        row.locator(self.item_total_price).inner_text().replace("Rs. ", "")
                    )
                })
            return products