from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.locators.components.header_locators import HeaderLocators as L

class Header(BasePage):
    def verify_logged_in(self):
        self.verify_visible(
            self.page.locator(L.LOGGED_IN_USER),
            "Logged in user"
        )

    def scroll_up_to_header(self):
        self.scroll_to(
            self.page.locator(L.SITE_HEADER),
            "Site header"
        )

    def click_signup_login(self):
        self.click(
            self.page.locator(L.BUTTON_SIGNUP_LOGIN),
            "Signup / Login button"
        )    

    def click_delete_account(self):
        self.click(
            self.page.locator(L.BUTTON_DELETE_ACCOUNT),
            "Delete Account button"
        )

    def click_logout(self):
        self.click(
            self.page.locator(L.BUTTON_LOGOUT),
            "Logout button"
        )

    def click_contact_us(self):
        self.click(
            self.page.locator(L.BUTTON_CONTACT_US),
            "Contact us button"
        )

    def click_test_cases(self):
        self.click(
            self.page.locator(L.BUTTON_TEST_CASES),
            "Test Cases button"
        )

    def click_products(self):
        self.click(
            self.page.locator(L.BUTTON_PRODUCTS),
            "Products button"
        )

    def click_cart(self):
        self.click(
            self.page.locator(L.BUTTON_CART),
            "Cart button"
        )