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
        display_value = "********" if "password" in name.lower() else value
        
        with allure.step(f'Fill "{name}" with "{display_value}"'):
            locator.fill(value)

    def scroll_to(self, locator: Locator, name: str):
        with allure.step(f'Scroll to "{name}"'):
            locator.scroll_into_view_if_needed()