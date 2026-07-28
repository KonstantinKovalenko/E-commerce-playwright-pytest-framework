import allure

from pages.base_page import BasePage
from pages.locators.products.products_locators import ProductsLocators as L

class ProductsPage(BasePage):
    def verify_loaded(self):
        self.verify_title("Automation Exercise - All Products")

    def verify_products_list_visible(self):
        self.verify_visible(
            self.page.locator(L.PRODUCTS_LIST),
            "All Products section"
        )

    def verify_brands_visible(self):
        self.verify_visible(
            self.page.locator(L.BRANDS_FILTERS),
            "Brands filters section"
        )

    def click_modal_continue_shopping(self):
        self.click(
            self.page.locator(L.BUTTON_MODAL_CONTINUE_SHOPPING),
            "Continue shopping"
        )

    def click_modal_view_cart(self):
        self.click(
            self.page.locator(L.BUTTON_MODAL_VIEW_CART),
            "View cart"
        )

    def click_first_view_product(self):
        self.click(
            self.page.locator(L.VIEW_PRODUCT).nth(0),
            "First product - View Product"
        )

    def add_product_to_cart(self, index: int):
        self.click(
            self.page.locator(L.BUTTON_OVERLAY_ADD_TO_CART).nth(index),
            f'Add product #{index + 1} to cart'
        )

    def add_results_to_cart(self):
        buttons = self.page.locator(L.BUTTON_ADD_TO_CART)
        buttons_count = buttons.count()

        for i in range(buttons_count):
            self.click(buttons.nth(i), f"Add product #{i + 1} to cart")
            self.click(self.page.locator(L.BUTTON_MODAL_CONTINUE_SHOPPING), "Continue shopping")

    def search_by_product_name(self, product: str):
        self.fill(self.page.locator(L.INPUT_SEARCH_PRODUCT), product, "Product")
        self.click(self.page.locator(L.BUTTON_SEARCH_PRODUCT), "First product - View Product")

    def verify_search_result(self, expected_name: str):
        self.verify_text(self.page.locator(L.TITLE_SEARCHED_PRODUCTS), "Searched Products")
        self.verify_text(self.page.locator(L.PRODUCT_NAME).first, expected_name)

    def hover_over_product(self, index: int):
        with allure.step(f'Hover over product #{index + 1}'):
            self.page.locator(L.PRODUCT_FRAME).nth(index).hover()

    def get_product_info(self, index: int):
        with allure.step(f'Get information from product: #{index + 1}'):
            product = self.page.locator(L.PRODUCTS_ARRAY).nth(index)
            name = product.locator("p").inner_text()
            price = int(product.locator("h2").inner_text().replace("Rs. ", ""))

            return {
                "name": name,
                "price": price
            }

    def filter_by_brand(self, brand: str):
        with allure.step(f'Select brand: "{brand}"'):
            brand_button = L.BRANDS_BUTTONS[brand]
            self.click(
                self.page.locator(brand_button),
                f"{brand} filter"
            )

    def verify_multiple_search_results(self):
        count = self.page.locator(L.PRODUCTS_ARRAY).count()
        with allure.step(f"Verify multiple results are displayed ({count} found)"):
            assert count > 0, "No products found"