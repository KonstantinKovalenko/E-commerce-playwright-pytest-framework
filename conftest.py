import allure
import pytest

from config.settings import BASE_URL

from pages.page_manager import PageManager

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

@pytest.fixture
def app(page):
    return PageManager(page)

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
def page(request, context):
    page = context.new_page()

    if "no_ads_block" not in request.keywords:
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

    yield page

    page.close()