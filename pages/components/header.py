from playwright.sync_api import Page
from pages.base_page import BasePage

class Header(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.site_header = page.locator('#header')

        self.links = page.locator('.shop-menu')

        self.button_products = self.links.get_by_role("link", name="Products")
        self.button_cart = self.links.get_by_role("link", name="Cart")
        self.button_signup_login = self.links.get_by_role("link", name="Signup / Login")
        self.button_logout = self.links.get_by_role("link", name="Logout")
        self.button_delete_account = self.links.get_by_role("link", name="Delete Account")
        self.button_test_cases = self.links.get_by_role("link", name="Test Cases")
        self.button_contact_us = self.links.get_by_role("link", name="Contact us")

        self.logged_in_user = self.links.get_by_text("Logged in as")

    def verify_logged_in(self):
        self.verify_visible(
            self.logged_in_user,
            "Logged in user"
        )

    def scroll_up_to_header(self):
        self.scroll_to(
            self.site_header,
            "Site header"
        )

    def click_signup_login(self):
        self.click(
            self.button_signup_login,
            "Signup / Login button"
        )    

    def click_delete_account(self):
        self.click(
            self.button_delete_account,
            "Delete Account button"
        )

    def click_logout(self):
        self.click(
            self.button_logout,
            "Logout button"
        )

    def click_contact_us(self):
        self.click(
            self.button_contact_us,
            "Contact us button"
        )

    def click_test_cases(self):
        self.click(
            self.button_test_cases,
            "Test Cases button"
        )

    def click_products(self):
        self.click(
            self.button_products,
            "Products button"
        )

    def click_cart(self):
        self.click(
            self.button_cart,
            "Cart button"
        )