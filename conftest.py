import allure
import pytest

from config.settings import BASE_URL
from pages.home_page import HomePage


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