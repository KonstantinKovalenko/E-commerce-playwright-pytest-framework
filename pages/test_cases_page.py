from pages.base_page import BasePage
from playwright.sync_api import Page

class TestCasesPage(BasePage):
    PATH = "/test_cases"

    def __init__(self, page: Page):
        super().__init__(page)
        self.title_test_cases = page.get_by_role("heading", level=2, name="Test Cases")