from playwright.sync_api import Page
from pages.base_page import BasePage

class Header(BasePage):
    PRODUCTS_BUTTON = 'a[href="/products"]'
    CART_BUTTON = '.shop-menu a[href="/view_cart"]'
    SIGNUP_LOGIN_BUTTON = '.shop-menu a[href="/login"]'
    LOGOUT_BUTTON = 'a[href="/logout"]'
    DELETE_ACCOUNT_BUTTON = 'a[href="/delete_account"]'
    CONTACT_US_BUTTON = 'a[href="/contact_us"]'
    TEST_CASES_BUTTON = '.shop-menu a[href="/test_cases"]'
    LOGGED_IN_USER = 'a:has-text("Logged in as")'

    def __init__(self, page: Page):
        super().__init__(page)

    def click_signup_login(self):
        self.click(
            self.page.locator(self.SIGNUP_LOGIN_BUTTON),
            "Signup / Login button"
        )

    def verify_logged_in(self):
        self.verify_visible(
            self.page.locator(self.LOGGED_IN_USER),
            "Logged in user"
        )

    def click_delete_account(self):
        self.click(
            self.page.locator(self.DELETE_ACCOUNT_BUTTON),
            "Delete Account button"
        )

    def click_logout(self):
        self.click(
            self.page.locator(self.LOGOUT_BUTTON),
            "Logout button"
        )

    def click_contact_us(self):
        self.click(
            self.page.locator(self.CONTACT_US_BUTTON),
            "Contact us button"
        )

    def click_test_cases(self):
        self.click(
            self.page.locator(self.TEST_CASES_BUTTON),
            "Test Cases button"
        )

    def click_products(self):
        self.click(
            self.page.locator(self.PRODUCTS_BUTTON),
            "Products button"
        )

    def click_cart(self):
        self.click(
            self.page.locator(self.CART_BUTTON),
            "Cart button"
        )