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
        self.home = HomePage(page)
        self.signup = SignupLoginPage(page)
        self.contact_us = ContactUsPage(page)
        self.test_cases = TestCasesPage(page)
        self.registration = RegistrationPage(page)
        self.account_created = AccountCreatedPage(page)
        self.delete_account = DeleteAccountPage(page)
        self.cart = CartPage(page)
        self.checkout = CheckoutPage(page)
        self.payment = PaymentPage(page)
        self.payment_done = PaymentDonePage(page)
        self.products = ProductsPage(page)
        self.product_details = ProductDetailsPage(page)
        self.category_products = CategoryProductsPage(page)
        self.brand_products = BrandProductsPage(page)
        self.header = Header(page)
        self.footer = Footer(page)