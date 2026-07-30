from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.contact_us_page import ContactUsPage
from pages.test_cases_page import TestCasesPage

from pages.account.registration_page import RegistrationPage
from pages.account.account_created_page import AccountCreatedPage
from pages.account.delete_account_page import DeleteAccountPage

from pages.checkout.cart_page import CartPage
from pages.checkout.checkout_page import CheckoutPage
from pages.checkout.payment_page import PaymentPage
from pages.checkout.payment_done_page import PaymentDonePage

from pages.products.products_page import ProductsPage
from pages.products.product_details_page import ProductDetailsPage
from pages.products.category_products_page import CategoryProductsPage
from pages.products.brand_products_page import BrandProductsPage

from pages.components.header import Header
from pages.components.footer import Footer

class PageManager:
    def __init__(self, page):
        self.page = page

        self._home = None
        self._signup = None
        self._contact_us = None
        self._test_cases = None
        self._registration = None
        self._account_created = None
        self._delete_account = None
        self._cart = None
        self._checkout = None
        self._payment = None
        self._payment_done = None
        self._products = None
        self._product_details = None
        self._category_products = None
        self._brand_products = None
        self._header = None
        self._footer = None

    @property
    def home(self):
        if self._home is None:
            self._home = HomePage(self.page)
        return self._home

    @property
    def signup(self):
        if self._signup is None:
            self._signup = SignupLoginPage(self.page)
        return self._signup

    @property
    def contact_us(self):
        if self._contact_us is None:
            self._contact_us = ContactUsPage(self.page)
        return self._contact_us
    
    @property
    def test_cases(self):
        if self._test_cases is None:
            self._test_cases = TestCasesPage(self.page)
        return self._test_cases

    @property
    def registration(self):
        if self._registration is None:
            self._registration = RegistrationPage(self.page)
        return self._registration

    @property
    def account_created(self):
        if self._account_created is None:
            self._account_created = AccountCreatedPage(self.page)
        return self._account_created

    @property
    def delete_account(self):
        if self._delete_account is None:
            self._delete_account = DeleteAccountPage(self.page)
        return self._delete_account

    @property
    def cart(self):
        if self._cart is None:
            self._cart = CartPage(self.page)
        return self._cart

    @property
    def checkout(self):
        if self._checkout is None:
            self._checkout = CheckoutPage(self.page)
        return self._checkout

    @property
    def payment(self):
        if self._payment is None:
            self._payment = PaymentPage(self.page)
        return self._payment

    @property
    def payment_done(self):
        if self._payment_done is None:
            self._payment_done = PaymentDonePage(self.page)
        return self._payment_done

    @property
    def products(self):
        if self._products is None:
            self._products = ProductsPage(self.page)
        return self._products

    @property
    def product_details(self):
        if self._product_details is None:
            self._product_details = ProductDetailsPage(self.page)
        return self._product_details

    @property
    def category_products(self):
        if self._category_products is None:
            self._category_products = CategoryProductsPage(self.page)
        return self._category_products

    @property
    def brand_products(self):
        if self._category_products is None:
            self._category_products = BrandProductsPage(self.page)
        return self._category_products

    @property
    def header(self):
        if self._header is None:
            self._header = Header(self.page)
        return self._header

    @property
    def footer(self):
        if self._footer is None:
            self._footer = Footer(self.page)
        return self._footer