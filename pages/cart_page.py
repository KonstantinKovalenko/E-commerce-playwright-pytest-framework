from components.footer import Footer
from pages.base_page import BasePage

class CartPage(BasePage):
    PATH = "/view_cart"

    def __init__(self, page):
        super().__init__(page)
        self.footer = Footer(page)

    def verify_loaded(self):
        self.verify_title("Automation Exercise - Checkout")