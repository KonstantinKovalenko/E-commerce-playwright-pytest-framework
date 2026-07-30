import allure
import re

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
        display_value = "********" if "password" in name.lower() else value
        
        with allure.step(f'Fill "{name}" with "{display_value}"'):
            locator.fill(value)

    def type_text(self, locator: Locator, value: str, name: str):
        with allure.step(f'Type "{value}" into "{name}"'):
            locator.press_sequentially(value)

    def get_text(self, locator: Locator):
        return locator.inner_text()

    def is_visible(self, locator: Locator):
        return locator.is_visible()

    def verify_text(self, locator: Locator, expected: str):
        with allure.step(f'Verify text "{expected}"'):
            expect(locator).to_have_text(expected)

    def verify_url_contains(self, text: str):
        with allure.step(f'Verify URL contains "{text}"'):
            expect(self.page).to_have_url(re.compile(f".*{re.escape(text)}.*"))

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")

    def verify_text_contains(self, locator: Locator, expected: str):
        with allure.step(f'Verify text contains "{expected}"'):
            expect(locator).to_contain_text(expected)

    def scroll_to(self, locator: Locator, name: str):
        with allure.step(f'Scroll to "{name}"'):
            locator.scroll_into_view_if_needed()