import allure
from playwright.sync_api import Locator, Page, expect
from config.settings import BASE_URL

class BasePage:

    BASE_URL = BASE_URL
    PATH = ""

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        with allure.step(f'Open "{self.PATH}"'):
            self.page.goto(f"{self.BASE_URL}{self.PATH}")

    def click(self, locator: Locator, name: str):
        with allure.step(f'Click "{name}"'):
            locator.click()

    def fill(self, locator: Locator, value: str, name: str):
        with allure.step(f'Fill "{name}" with "{value}"'):
            locator.fill(value)

    def type(self, locator: Locator, value: str, name: str):
        with allure.step(f'Type "{value}" into "{name}"'):
            locator.press_sequentially(value)

    def get_text(self, locator: Locator):
        return locator.inner_text()

    def is_visible(self, locator: Locator):
        return locator.is_visible()

    def verify_visible(self, locator: Locator, name: str):
        with allure.step(f'Verify "{name}" is visible'):
            expect(locator).to_be_visible()

    def verify_text(self, locator: Locator, expected: str):
        with allure.step(f'Verify text "{expected}"'):
            expect(locator).to_have_text(expected)

    def verify_title(self, expected: str):
        with allure.step(f'Verify page title "{expected}"'):
            expect(self.page).to_have_title(expected)

    def verify_url(self, expected: str):
        with allure.step(f'Verify URL "{expected}"'):
            expect(self.page).to_have_url(expected)

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")