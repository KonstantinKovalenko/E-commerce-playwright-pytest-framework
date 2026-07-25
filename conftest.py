import allure
import pytest

from config.settings import BASE_URL
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_life_cycle.registration_page import RegistrationPage
from pages.account_life_cycle.account_created_page import AccountCreatedPage
from pages.account_life_cycle.delete_account_page import DeleteAccountPage
from pages.contact_us_page import ContactUsPage
from pages.test_cases_page import TestCasesPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.payment_done_page import PaymentDonePage

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def signup_login_page(page):
    return SignupLoginPage(page)

@pytest.fixture(scope="function")
def registration_page(page):
    return RegistrationPage(page)

@pytest.fixture(scope="function")
def account_created_page(page):
    return AccountCreatedPage(page)

@pytest.fixture(scope="function")
def delete_account_page(page):
    return DeleteAccountPage(page)

@pytest.fixture(scope="function")
def contact_us_page(page):
    return ContactUsPage(page)

@pytest.fixture(scope="function")
def test_cases_page(page):
    return TestCasesPage(page)

@pytest.fixture(scope="function")
def products_page(page):
    return ProductsPage(page)

@pytest.fixture(scope="function")
def product_details_page(page):
    return ProductDetailsPage(page)

@pytest.fixture(scope="function")
def cart_page(page):
    return CartPage(page)

@pytest.fixture(scope="function")
def checkout_page(page):
    return CheckoutPage(page)

@pytest.fixture(scope="function")
def payment_page(page):
    return PaymentPage(page)

@pytest.fixture(scope="function")
def payment_done_page(page):
    return PaymentDonePage(page)

# ----------------------------
# Allure screenshot on failure
# ----------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.passed:
        return

    page = item.funcargs.get("page")

    if page:
        allure.attach(
            page.screenshot(),
            name=f"{item.name}_failure",
            attachment_type=allure.attachment_type.PNG,
        )

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()

    page.route(
        "**/*",
        lambda route: route.abort()
        if any(domain in route.request.url for domain in [
            "doubleclick.net",
            "googlesyndication.com",
            "googleadservices.com",
            "adservice.google.com",
            "ads-twitter.com",
            "amazon-adsystem.com",
            "googleads.g.doubleclick.net",
            "tpc.googlesyndication.com",
        ])
        else route.continue_()
    )

    page.set_viewport_size({"width": 1920, "height": 1080})

    yield page

    page.close()