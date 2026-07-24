import allure
import pytest

from config.settings import BASE_URL
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_life_cycle.registration_page import RegistrationPage
from pages.account_life_cycle.account_created_page import AccountCreatedPage
from pages.account_life_cycle.delete_account_page import DeleteAccountPage

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