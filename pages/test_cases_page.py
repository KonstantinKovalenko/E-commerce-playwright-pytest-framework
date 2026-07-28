from pages.base_page import BasePage
from pages.locators.test_cases_locators import TestCasesLocators as L

class TestCasesPage(BasePage):
    def verify_loaded(self):
        self.verify_title("Automation Practice Website for UI Testing - Test Cases")

    def verify_test_cases_visible(self):
        self.verify_visible(
            self.page.locator(L.TITLE_TEST_CASES),
            "Test Cases section"
        )